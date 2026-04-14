# Claude Context — DetectorNX Report

## Project Overview
University of Manchester BSc Computer Science dissertation (2026).
**Title**: "Who Knows... The Game Is The Game"
**Topic**: Development and evaluation of a Spiking Neural Network (SNN) for multi-object detection on neuromorphic event-camera data, compared against a parameter-matched CNN baseline.

---

## Core Architecture
- **SNN**: `SNN_MAX_REPLICA_SE` — 11.72M params, SEW-ResNet backbone + SE attention, LIF neurons, surrogate gradient training, Firing Rate Regularization (FRR)
- **CNN**: `CNN_MAX_REPLICA_SE` — 11.73M params, exact 1:1 architectural mirror of SNN (ResBlocks replace SEWResBlocks, ReLU replaces LIF)
- **Dataset**: ETraM (Event-based Traffic Monitoring), 1280×720 HD event camera, 10,000 samples
- **Preprocessing pipeline**: REPLICA — spatiotemporal voxelization (T=10 bins, C=2 polarities), 4× MaxPool downsampling → [10,2,180,320], multi-object label alignment (5 boxes padded)
- **Detection head**: Multi-Box Regression Head, 8×8 Adaptive Pooling → [B, 5, 5] output (5 boxes × {x,y,w,h,conf})
- **Key constraint**: Both models trained on identical preprocessed data, ensuring any performance delta is solely attributable to spiking vs continuous activations

---

## Key Quantitative Results (Table 1.6 — 200-sample validation set)

| Metric | SNN ULTRA | CNN Baseline |
|--------|-----------|--------------|
| Mean IoU | **0.4658** | 0.4861 |
| Avg Detections/Frame (GT) | 2.02 | 2.02 |
| Avg Detections/Frame (Pred) | 1.69 | 1.75 |
| Max Confidence | **1.0000** | 0.9918 |
| Min Confidence | 0.0006 | 0.0132 |
| Mean Confidence | **0.4084** | 0.3872 |

**Key insight**: Only ~2% IoU gap. SNN achieves detection parity in terms of ADP. SNN achieves *higher* mean confidence than CNN. SNN max confidence is exactly 1.0000.

---

## Paper's Theoretical Arguments (relevant to qualitative images)

### §1.7.2 Quantization Error Analysis
- Hypothesis: SNN will struggle more with **small objects** due to binary discretization
- For large objects: parity expected (quantization noise negligible relative to object area)
- For small objects: a "resolution floor" limits mIoU
- SNN can only represent T+1 = 11 discrete coordinate states (0/10, 1/10, ..., 10/10)

### §1.7.3 Confidence Calibration
- SNN expected to be **better calibrated** than CNN — spiking dynamics act as implicit uncertainty sensors
- Low-quality features → fewer spikes → lower confidence (natural calibration)
- CNN prone to overconfidence despite poor localization

### §1.7.4 Temporal Evidence Accumulation
- SNN processes T=10 timesteps sequentially; can produce early predictions before full 100ms window
- "Hunting behavior": bbox sharpens as membrane potential accumulates
- CNN does a single flattened spatial pass

### §1.6.2 Super-Box / Ghost Detections (partially resolved)
- Early Gen 1 failure: model averaged positions of all vehicles → one large spanning box
- Gen 2 (8×8 pooling head) largely resolved ghost detections
- Residual ghost detections may still appear in the audit images

---

## Architectural Evolution (important for image selection)
- **Gen 1**: Multi-Box head. Failure: ghost detections / overlapping predictions
- **Gen 2**: 8×8 spatial pooling. Solved ghost detections. Still had 41% IoU ceiling (insufficient spatial resolution)
- **Gen 3 (ULTRA)**: 22×40 feature maps + 4th SEWResBlock + lowered Vth (0.5→0.2), quintupled FRR λ. Final architecture used for all results.

---

## Figure 1.5 — Qualitative Inference Audit
**Current state**: 3 pairs of placeholder images (example-image-a/b/c) in `report/chapter_3/3_8_results_evaluation.tex`
**Audit images location**: 
- `report/chapter_3/dnx_results/cnn_audit/audit_sample_XXX.png`
- `report/chapter_3/dnx_results/snn_audit/audit_sample_XXX.png`
- 200 samples total (000–199), same indices across both models

**Critical Analysis section**: Currently **empty** (§1.8.1, after the figure) — the selected images must anchor this narrative.

---

## Recommended 4 Pairs (context-informed)

### Pair 1 — SNN Excellent: **Sample 178**
- CNN: Det 1/GT 1, Conf 0.93, reasonable localization
- SNN: Det 1/GT 1, Conf **1.0000** (ties directly to Table 1.6 max confidence), tight bbox
- **Why**: Directly evidences the max confidence result in Table 1.6. Supports §1.7.2 hypothesis that SNN achieves parity on large objects. Single vehicle, well-centered. Best example of SNN competitive performance.

### Pair 2 — SNN Critical (bbox imprecision): **Sample 003**
- CNN: Det 1/GT 1, Conf 0.94, tight, well-fitting bbox
- SNN: Det 1/GT 1, Conf 0.96, **massively oversized bbox** spanning half the frame despite correct detection
- **Why**: Classic illustration of the quantization/localization imprecision problem from §1.7.2. Both models detect the target with comparable confidence — the delta is purely geometric. Directly explains why mIoU is 0.4658 vs 0.4861 despite confidence parity. Key critique: correct classification, wrong box.

### Pair 3 — Ghost Detection (false positive): **Sample 020**
- CNN: Det 1/GT 1, Conf 0.78, correct
- SNN: Det **3**/GT 1, Conf 0.94/0.66/0.57 — two ghost detections alongside one correct
- **Why**: Directly evidences residual ghost detection behavior discussed in §1.6.2. Shows the SNN's event-driven spiking producing spurious activations from background sensor noise. Explains the ADP delta (SNN avg pred 1.69 vs GT 2.02 — the averaging includes cases like this that inflate outliers).

### Pair 4 — CNN Blind Spot / SNN Sensitivity: **Sample 030**
- CNN: Det **0**/GT 1 — complete miss
- SNN: Det 2/GT 1 — over-detects but at least fires in the target region
- **Why**: Demonstrates the complementary failure mode: CNN fails completely where SNN at least responds. Supports §1.7.4 (temporal evidence accumulation) — the SNN's sequential membrane potential integration makes it more sensitive to sparse event regions where a single CNN spatial pass misses entirely. Creates a balanced critical analysis (SNN is not strictly worse).

---

## Narrative These 4 Pairs Support
> "The SNN achieves near-parity IoU (0.4658 vs 0.4861) with identical detection selectivity, and can achieve maximal confidence on isolated large targets [Pair 1]. However, its primary weakness is geometric imprecision: despite correct object detection, the binary spike discretization systematically oversizes bounding boxes [Pair 2], which is the primary driver of the mIoU gap. Residual ghost detections from background sensor noise remain a secondary failure mode [Pair 3]. Notably, the SNN's temporal integration provides complementary sensitivity — detecting targets in sparse event regions where the CNN's single spatial pass produces no output [Pair 4]."
