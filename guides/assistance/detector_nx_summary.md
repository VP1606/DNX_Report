# DetectorNX: Project Summary & Architectural Context

## Project Objective
Development and rigorous evaluation of a high-performance **Spiking Neural Network (SNN)** for multi-object detection using high-definition event-camera data (ETraM dataset). The project focuses on quantifying the **Accuracy vs. Energy Efficiency tradeoff** between bio-plausible spiking architectures and traditional Convolutional Neural Networks (CNNs).

---

## 1. Architectural Evolution (SNN_MAX_REPLICA_SE)

The SNN backbone evolved through three distinct generations to overcome specific limitations in spatial resolution and information flow:

### Generation 1: Base Multi-Box (5.43M Params)
*   **Goal:** Move from single-object regression to multi-object detection to handle multiple cars in a scene.
*   **Design:** [B, 5, 5] output head (5 boxes, 4 coords + 1 confidence).
*   **Bottleneck:** Plateaued at 41% IoU. Suffered from "Ghost Detections" due to limited 4x4 spatial pooling memory.

### Generation 2: Expanded Head (7.00M Params)
*   **Goal:** Solve the ambiguity problem and suppress false positives.
*   **Design:** Increased Adaptive Pool from (4, 4) to **(8, 8)**, providing 64 spatial blocks for the regression head.
*   **Result:** Effectively solved ambiguity (Avg Detections: 2.06 vs 2.02 GT).

### Generation 3: "Ultra" Super Run (11.72M Params)
*   **Goal:** Break the 41% IoU barrier and maximize geometric precision.
*   **Backbone:** Added a **4th SEWResBlock** for deeper semantic reasoning.
*   **Resolution:** Reduced stride in Block 3, increasing feature map resolution from 11x20 to **22x40**.
*   **Dynamics:** Lowered $V_{threshold}$ to 0.2 and quintupled Firing Rate Regularization (FRR) penalty to force higher information flow.

---

## 2. Technical Optimizations

To handle HD event data at 150-epoch scales, the following speed and stability optimizations were implemented:

1.  **Vectorized Multi-Box Loss:** A fully parallelized matching logic using broadcasted IoU matrices, removing all Python loops over batch and objects.
2.  **Multi-Step SNN Nodes:** Refactored the backbone to use SpikingJelly's `step_mode='m'`. This allows the temporal simulation ($T=10$) to run in optimized C++/CUDA kernels rather than sequential Python loops.
3.  **Automatic Mixed Precision (AMP):** Integrated `torch.amp` with a `GradScaler` to utilize GPU Tensor Cores, resulting in a ~1.8x speedup and halved memory usage.
4.  **Numerical Stability:** Switched the head to output raw **logits** used with `BCEWithLogitsLoss` to prevent gradient explosion in 16-bit precision.

---

## 3. The CNN Baseline
A 1:1 non-spiking counterpart (**CNN_MAX_REPLICA_SE**, 11.73M Params) was built to provide a "Gold Standard" baseline. It mirrors the Ultra SNN architecture exactly but replaces LIF nodes with ReLUs and flattens the 10 time bins into the channel dimension for a dense spatial pass.

---

## 4. Benchmarking & Findings Suite
Located in `rebase-v01/final_experiments/`, this suite generates the data for the dissertation findings:

### Quantitative Metrics
*   **Accuracy:** `evaluate_experiment.py` (Mean/Median IoU, Recall, False Positives).
*   **Latency:** `benchmark_latency.py` (Milliseconds per frame on actual GPU).
*   **Energy:** `benchmark_energy.py` (Theoretical energy in mJ based on Horowitz (2014) constants and extrapolations for Intel Loihi/IBM TrueNorth).

### Qualitative Analysis (Visuals)
*   **Dynamic Power:** `exp1_dynamic_power.py` (SNN energy vs scene activity scatter plot).
*   **Precision Gap:** `exp2_accuracy_vs_size.py` (IoU bar chart categorized by Small/Medium/Large objects).
*   **Calibration:** `exp3_confidence_calibration.py` (Reliability diagrams for SNN vs CNN).
*   **Temporal Logic:** `exp4_temporal_accumulation.py` (Visualization of evidence accumulation over 100ms).
*   **Visual Audit:** `exp5_full_validation_vis.py` (Frame-by-frame audit of all 200 validation samples).

---

## 5. Usage for Future Agents
All experiments and evaluations are designed to be run from the `rebase-v01/` directory.
Commands are consolidated in `rebase-v01/final_experiments/instruction.txt`.
HPC automation is provided via `rebase-v01/final_experiments/test_all_hpc.sh`.
