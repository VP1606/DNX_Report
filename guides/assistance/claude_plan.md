# Dissertation Report Plan
## Spiking Neural Networks for Object Detection on the ETRAM Dataset
### COMP30040 — Third Year Project, University of Manchester

---

> **How to use this plan**: Each section lists the *purpose*, *key points to cover*, suggested *figures/tables*, and a *word budget*. Placeholder technique names (e.g. `PREPROCESSING TECHNIQUE`) must be replaced with the real names when writing. Do not start writing prose until you have run all experiments and have results in hand.

---

## Meta-notes (read before starting)

### Word Count Budget
The guidance document recommends targeting approximately **12,000 words** for the main body (excluding front matter, bibliography, and appendices). The table below distributes this across chapters, consistent with both the official guidance and the exemplar reports reviewed.

| Chapter | Proportion | Target Words |
|---|---|---|
| 1 — Introduction | 10% | 1,200 |
| 2 — Background and Literature Review | 30% | 3,600 |
| 3 — Methodology and System Design | 25% | 3,000 |
| 4 — Results and Evaluation | 25% | 3,000 |
| 5 — Conclusions and Future Work | 10% | 1,200 |
| **Total** | **100%** | **~12,000** |

### Key Formatting Reminders (from official guidance)
- **Formal tone**: no contractions (write "does not", not "doesn't"), no shorthand ("and" not "&").
- **Abbreviations**: define every abbreviation on first use in the text (e.g., "Spiking Neural Network (SNN)"), and maintain the **Abbreviations and Acronyms** list at the front.
- **Figures and tables**: always refer to them in the text before they appear (e.g., "As shown in Figure 3.2, …"). Every figure and table needs a descriptive caption that can be read in isolation.
- **Citations**: use short numeric format [n] throughout. Sort bibliography alphabetically by author surname.
- **Numbers**: spell out small numbers in prose ("two models were trained"), use digits for measurements ("640 ms").
- **Spell-check and proofread** before submission; consider swapping with a peer for cross-review.

### Lessons from Exemplar Reports
- **Strength to emulate (Robert Chiru)**: Explicit *success criteria* in the Introduction and a dedicated *Literature Review* chapter that is clearly distinct from the design chapter. The Introduction also contains a *Dissertation Structure* subsection that road-maps the report for the reader.
- **Strength to emulate (Yi Wu)**: Very thorough Background with well-scoped subsections that each build logically on the previous one. Combined Results and Evaluation chapter prevents duplication.
- **Weakness to avoid (Yi Wu)**: Background chapter was proportionally oversized (~35% of the ToC), crowding out the Results chapter. Keep Background disciplined — every subsection must serve a purpose needed later.
- **Weakness to avoid (both)**: Some subsections read as lists of facts rather than structured arguments. Each subsection should end with a sentence connecting the material back to *this* project.

---

## Full Table of Contents

### Front Matter
- Title Page
- Abstract
- Declaration of Originality
- Intellectual Property Statement (Copyright)
- Acknowledgements
- Table of Contents
- List of Figures
- List of Tables
- Abbreviations and Acronyms

### Main Body
1. Introduction
   - 1.1 Motivation and Context
     - 1.1.1 The Energy Cost of Deep Learning
     - 1.1.2 Neuromorphic Computing as a Solution
   - 1.2 Problem Statement
   - 1.3 Project Aims and Objectives
   - 1.4 Success Criteria
   - 1.5 Report Structure

2. Background and Literature Review
   - 2.1 Artificial Neural Networks and Deep Learning
     - 2.1.1 FEEDFORWARD NETWORK ARCHITECTURE TYPE
     - 2.1.2 GRADIENT-BASED TRAINING ALGORITHM
   - 2.2 Convolutional Neural Networks for Object Detection
     - 2.2.1 Convolutional Feature Extraction
     - 2.2.2 OBJECT DETECTION FRAMEWORK
     - 2.2.3 Evaluation Metrics for Object Detection
   - 2.3 Spiking Neural Networks
     - 2.3.1 Biological Motivation and Neuron Dynamics
     - 2.3.2 NEURON MODEL
     - 2.3.3 SPIKE ENCODING SCHEME
     - 2.3.4 SURROGATE GRADIENT TRAINING METHOD
     - 2.3.5 Energy Efficiency of SNNs
   - 2.4 Event-Based Vision
     - 2.4.1 How Event Cameras Work
     - 2.4.2 EVENT FRAME REPRESENTATION TECHNIQUE
     - 2.4.3 Suitability for Neuromorphic Processing
   - 2.5 The ETRAM Dataset
     - 2.5.1 Dataset Overview and Motivation
     - 2.5.2 Data Characteristics and Annotation Scheme
   - 2.6 Related Work
     - 2.6.1 SNNs Applied to Computer Vision
     - 2.6.2 Event-Based Object Detection
     - 2.6.3 SNN versus CNN Comparative Studies
   - 2.7 Neuromorphic Hardware and Energy Modelling
     - 2.7.1 Neuromorphic Processor Architectures
     - 2.7.2 Theoretical Energy Consumption Model

3. Methodology and System Design
   - 3.1 Design Overview and Guiding Principles
   - 3.2 Dataset Preparation
     - 3.2.1 PREPROCESSING TECHNIQUE (Event-to-Frame Conversion)
     - 3.2.2 NORMALISATION AND AUGMENTATION TECHNIQUE
     - 3.2.3 Train and Validation Split
   - 3.3 Shared Model Architecture
     - 3.3.1 BACKBONE ARCHITECTURE DESIGN
     - 3.3.2 DETECTION HEAD DESIGN
     - 3.3.3 Parameter Count and Fairness Constraint
   - 3.4 Spiking Neural Network Implementation
     - 3.4.1 NEURON MODEL Selection and Configuration
     - 3.4.2 SPIKE ENCODING SCHEME
     - 3.4.3 Temporal Timestep Configuration
     - 3.4.4 SURROGATE GRADIENT TRAINING ALGORITHM
   - 3.5 CNN Baseline Implementation
     - 3.5.1 Architectural Mapping from SNN to CNN
     - 3.5.2 Training Procedure and Hyperparameters
   - 3.6 Training Configuration
     - 3.6.1 OPTIMISER AND LEARNING RATE SCHEDULE
     - 3.6.2 LOSS FUNCTION
     - 3.6.3 Hardware Environment (HPC Setup)
   - 3.7 Evaluation and Benchmarking Framework
     - 3.7.1 Detection Accuracy Metrics
     - 3.7.2 Inference Latency Measurement Protocol
     - 3.7.3 Theoretical Energy Efficiency Model
     - 3.7.4 Projected Neuromorphic Hardware Latency Methodology

4. Results and Evaluation
   - 4.1 Detection Accuracy
     - 4.1.1 Overall IoU Performance: SNN versus CNN
     - 4.1.2 Accuracy versus Object Size
     - 4.1.3 Confidence Calibration Comparison
   - 4.2 Inference Latency
     - 4.2.1 GPU Hardware Benchmarks
     - 4.2.2 Projected Neuromorphic Hardware Latency
   - 4.3 Energy Efficiency
     - 4.3.1 Theoretical Power Consumption
     - 4.3.2 Dynamic Power Scatter Plot Analysis
     - 4.3.3 Estimated Energy Savings Relative to CNN
   - 4.4 Temporal Dynamics
     - 4.4.1 Temporal Accumulation Behaviour
     - 4.4.2 Spike Activity and Sparsity
   - 4.5 Qualitative Evaluation
     - 4.5.1 Visual Detection Audit
     - 4.5.2 Failure Mode Analysis
   - 4.6 Discussion
     - 4.6.1 Accuracy Trade-off: SNN versus CNN
     - 4.6.2 Efficiency Trade-off: SNN versus CNN
     - 4.6.3 Suitability for Neuromorphic Deployment
     - 4.6.4 Limitations of This Study

5. Conclusions and Future Work
   - 5.1 Summary of Contributions
   - 5.2 Reflection on Aims and Success Criteria
   - 5.3 Future Work
     - 5.3.1 Additional Experiments to Strengthen the Study
     - 5.3.2 Architectural and Training Improvements
     - 5.3.3 Deployment and Scalability Directions

### Back Matter
- Bibliography
- Appendix A — Full Validation Set Results
- Appendix B — HPC Experimental Configuration
- Appendix C — Additional Visualisations

---

## Front Matter — Detailed Notes

### Title Page
Follow the standard UoM muthesis template. Must include: full dissertation title, degree programme (BSc Computer Science), year, student name, supervisor name, and "Department of Computer Science, The University of Manchester." Note that `muthesis.cls` requires a one-line patch to recognise BSc — add `\DeclareOption{BSc}{\def\degreetitle{Bachelor of Science}\def\@thesis{report}}` as shown in the lecture slides.

### Abstract
Write this **last**, after all other chapters are complete. Aim for 200–250 words. Summarise: (1) the motivation and problem, (2) the approach taken (SNN and CNN with matched architecture on ETRAM), (3) the key experimental results (accuracy, latency, energy), and (4) the main conclusion. Do not include citations or undefined abbreviations. Study the Robert Chiru and Yi Wu abstracts as style references — both provide a concise problem-approach-result-conclusion flow.

### Declaration of Originality
Boilerplate. Copy from the sample report provided on Blackboard. Affirms the work is original and has not been submitted elsewhere.

### Intellectual Property Statement (Copyright)
Boilerplate. Copy verbatim from the sample report (the lecture slides confirm this is acceptable).

### Acknowledgements
Optional but conventional. Thank your supervisor and any lab/HPC support staff. Keep it brief (3–5 sentences).

### Table of Contents, List of Figures, List of Tables
Generated automatically by LaTeX. Ensure all figures and tables have short captions for the lists (use `\caption[Short version]{Long descriptive version}`). Number all pages. The Table of Contents should show sections and subsections.

### Abbreviations and Acronyms
Compile at the end, once the report is drafted. Include all abbreviations used in the main body. Do **not** title this section "Acronyms" — the correct title is "Abbreviations and Acronyms" or simply "Abbreviations." See the guidance document for the distinction between an abbreviation and an acronym.

---

## Chapter 1 — Introduction
**Target: ~1,200 words**

The Introduction gets the reader up to speed without assuming specialist knowledge. It should make someone unfamiliar with neuromorphic computing understand *why this project matters* and *what you set out to do*. Every chapter that follows should feel like a logical consequence of what is established here.

### 1.1 Motivation and Context (~300 words)

#### 1.1.1 The Energy Cost of Deep Learning
- Open with a compelling hook: the exponential growth in compute required to train and deploy large neural networks, and the environmental and financial cost this entails.
- Cite published figures on the energy consumption of state-of-the-art deep learning models (GPU training costs, inference at scale).
- Establish that object detection — the specific task of this project — is deployed in energy-constrained settings (autonomous vehicles, edge cameras, traffic monitoring), making efficiency a first-class concern.
- **Suggested figure**: a bar chart or graph showing energy cost trends in deep learning over recent years (cite source from a published survey).

#### 1.1.2 Neuromorphic Computing as a Solution
- Introduce the brain as an existence proof of energy-efficient intelligence (~20 W for the entire human brain).
- Explain that neuromorphic computing attempts to replicate the brain's sparse, event-driven computation in silicon.
- Mention that SNNs are the algorithmic counterpart to neuromorphic hardware, and that event-based cameras (which produce sparse, asynchronous output) are a natural sensor pairing.
- Close with the specific opportunity: *can an SNN match a CNN's object detection accuracy at a fraction of the energy cost?*

### 1.2 Problem Statement (~150 words)
State the problem precisely. The challenge is that SNNs are theoretically efficient but have historically lagged behind CNNs on accuracy-sensitive tasks. Prior work rarely controls for architecture and parameter count when comparing the two, making it difficult to isolate the effect of the spiking mechanism itself. This project addresses that gap by:
- Using the same backbone architecture and parameter count for both models.
- Evaluating on a real-world event-based traffic dataset (ETRAM).
- Measuring both accuracy *and* efficiency (energy, latency) to produce a fair, multi-dimensional comparison.

### 1.3 Project Aims and Objectives (~200 words)
Present as a numbered or structured list of aims. Suggested objectives:
1. Implement an SNN capable of performing object detection on event-based camera data.
2. Implement a CNN baseline using an identical architecture and parameter budget.
3. Train and evaluate both models on the ETRAM dataset.
4. Benchmark inference latency on GPU hardware.
5. Estimate theoretical energy consumption and project latency onto neuromorphic hardware.
6. Perform a fair, multi-dimensional comparison of SNN versus CNN on accuracy, latency, and energy.

### 1.4 Success Criteria (~150 words)
Define what "success" means for this project, so the Conclusions chapter can refer back to these explicitly. Examples:
- The SNN achieves an IoU score within an acceptable margin of the CNN (define the margin — e.g., within 5 percentage points).
- The SNN demonstrates measurable theoretical energy savings over the CNN baseline.
- Both models successfully produce bounding box predictions on the ETRAM validation set.
- A fair comparison is established: both models trained under identical conditions with matched parameter counts.

This section is strongly recommended based on the Robert Chiru exemplar, which used explicit success criteria to give the report a clear evaluation framework in the Conclusions.

### 1.5 Report Structure (~200 words)
Provide a brief paragraph-length description of each subsequent chapter. Do not simply list chapter titles — write one or two sentences explaining what the reader will find and why it is placed there. Example: "Chapter 2 provides the background theory required to understand the design decisions made in Chapter 3. It covers…". This is standard in both exemplar reports and is explicitly advised in the lecture slides.

---

## Chapter 2 — Background and Literature Review
**Target: ~3,600 words**

The Background chapter has two roles: (1) giving the reader the conceptual tools needed to understand your design decisions, and (2) situating your work within the existing literature. Every section should be curated — only include material that is needed later. At the end of each subsection, add one sentence connecting the theory back to this project. Cite everything.

### 2.1 Artificial Neural Networks and Deep Learning (~300 words)

#### 2.1.1 FEEDFORWARD NETWORK ARCHITECTURE TYPE
- Explain the concept of layers, neurons, weights, and activation functions at a high level.
- Cover the forward pass and how predictions are produced.
- This sets the baseline before introducing convolutional and spiking variants.
- **Suggested figure**: diagram of a simple feedforward network.

#### 2.1.2 GRADIENT-BASED TRAINING ALGORITHM
- Explain the loss function and the concept of gradient descent.
- Cover backpropagation at an intuitive level.
- Note that this standard training method is used for the CNN baseline, but that SNNs require a modified variant (bridge to Section 2.3.4).
- Cite foundational deep learning references (LeCun et al., Goodfellow et al. textbook).

### 2.2 Convolutional Neural Networks for Object Detection (~600 words)

#### 2.2.1 Convolutional Feature Extraction
- Explain convolution, pooling, and how spatial hierarchies of features are built.
- Note the inductive bias (translation invariance) that makes CNNs well-suited to image data.
- **Suggested figure**: visualisation of a convolutional layer applying filters.

#### 2.2.2 OBJECT DETECTION FRAMEWORK
- Describe the specific detection paradigm used (e.g., single-stage anchor-based or anchor-free detection, YOLO-style grid prediction, etc. — use the placeholder until you are writing).
- Cover the key components: backbone, neck (if used), detection head.
- Explain how bounding boxes and class scores are predicted.
- **Suggested figure**: diagram of the detection pipeline showing input → backbone → head → output boxes.

#### 2.2.3 Evaluation Metrics for Object Detection
- Define Intersection over Union (IoU) and explain why it is a better measure than raw classification accuracy for detection.
- Define mean Average Precision (mAP) if used.
- Explain confidence scores and their role in calibration (bridge to Experiment 3 in Chapter 4).
- **Suggested table**: summary of evaluation metrics with formulae.

### 2.3 Spiking Neural Networks (~900 words — the most technically dense section)

#### 2.3.1 Biological Motivation and Neuron Dynamics
- Motivate SNNs from neuroscience: the brain processes information through sparse, asynchronous spikes, not continuous floating-point values.
- Introduce the concept of the membrane potential, threshold, reset, and refractory period.
- Explain why this is computationally appealing: neurons only "fire" (and thus only consume energy) when the membrane potential exceeds threshold — most of the time they are silent.
- **Suggested figure**: a diagram showing membrane potential over time with a spike and reset.

#### 2.3.2 NEURON MODEL
- Introduce the specific neuron model used (e.g., Leaky Integrate-and-Fire — LIF — or similar). Use the placeholder name until writing.
- Give the governing differential equation or recurrence relation.
- Explain the leak term and its role in temporal dynamics.
- Discuss the hyperparameters of the model (membrane time constant, threshold).
- **Suggested figure**: a comparison diagram of a standard ReLU activation versus a spiking neuron output over time.

#### 2.3.3 SPIKE ENCODING SCHEME
- Explain that raw input data must be encoded into spike trains before being processed by an SNN.
- Describe the specific encoding scheme used (e.g., rate coding, temporal coding, direct frame encoding). Use placeholder until writing.
- Discuss the trade-offs between encoding schemes (e.g., rate coding is robust but slower; temporal coding is efficient but sensitive to noise).
- Explain how the ETRAM event frames fit into this encoding pipeline.

#### 2.3.4 SURROGATE GRADIENT TRAINING METHOD
- The fundamental challenge: the spike function is discontinuous (Heaviside step function), so standard backpropagation through it yields zero or undefined gradients.
- Explain the surrogate gradient approach: during the backward pass, a smooth differentiable function is substituted for the derivative of the spike function.
- Describe the specific surrogate function used (e.g., Sigmoid surrogate, Piecewise Linear, Arctan). Use placeholder.
- Note the connection to backpropagation through time (BPTT) for temporal unrolling over timesteps.
- Cite the key papers that introduced and validated surrogate gradient training.

#### 2.3.5 Energy Efficiency of SNNs
- Explain why SNNs are theoretically efficient: synaptic operations (SOPs) use simple accumulate operations instead of multiply-accumulate (MAC) operations.
- Present the theoretical energy model: energy ≈ firing rate × parameter count × energy-per-AC-operation.
- Note the contrast with CNNs, which perform a MAC for every connection on every forward pass regardless of activation sparsity.
- This section directly motivates the energy benchmarking in Chapter 4.

### 2.4 Event-Based Vision (~400 words)

#### 2.4.1 How Event Cameras Work
- Contrast event cameras with standard frame-based cameras: rather than capturing full frames at a fixed rate, event cameras output an asynchronous stream of events (x, y, polarity, timestamp) whenever a pixel detects a change in log-luminance.
- Highlight properties relevant to this project: high temporal resolution, low latency, low power consumption, high dynamic range.
- **Suggested figure**: a side-by-side comparison of a standard camera frame versus an event stream visualisation.

#### 2.4.2 EVENT FRAME REPRESENTATION TECHNIQUE
- Raw event streams must be converted into a format compatible with frame-based neural networks.
- Describe the specific representation used (e.g., event count frames, surface of active events, voxel grids, time surfaces). Use placeholder.
- Explain how the PRECOMPUTED_10K_HD_REPLICA dataset stores pre-converted frames, and what preprocessing was applied.
- Discuss any trade-offs: temporal resolution versus spatial resolution, information loss in the conversion.

#### 2.4.3 Suitability for Neuromorphic Processing
- Argue that event-based data and SNNs are a natural pairing: both are inherently sparse and temporal.
- Note that standard CNNs applied to event frames discard the sparsity advantage, while SNNs can preserve it.
- This motivates the specific combination of SNN + event camera data in this project.

### 2.5 The ETRAM Dataset (~350 words)

#### 2.5.1 Dataset Overview and Motivation
- Introduce the ETRAM (Event-based TRaffic Monitoring) dataset.
- Describe its purpose: traffic monitoring using event-based cameras in real-world conditions.
- Note why it is a good benchmark for this project: real-world complexity, diverse object classes (vehicles, pedestrians, cyclists), varied lighting and weather conditions.
- Cite the original ETRAM dataset paper.
- **Suggested table**: key dataset statistics (number of samples, classes, split sizes, resolution).

#### 2.5.2 Data Characteristics and Annotation Scheme
- Describe the annotation format (bounding boxes, class labels).
- Discuss class distribution — are some classes over-represented? (connects to the accuracy-vs-size analysis in Chapter 4).
- Note any notable challenges in the data: small objects, occlusion, fast motion.

### 2.6 Related Work (~600 words)

#### 2.6.1 SNNs Applied to Computer Vision
- Review key papers that have applied SNNs to image classification and object detection tasks.
- Note accuracy gaps relative to CNNs and how they have narrowed over time.
- Identify the specific architectural or training innovations that improved SNN performance.
- Note limitations: most prior SNN work targets static image datasets (MNIST, CIFAR-10), fewer studies target object detection on event-based data.

#### 2.6.2 Event-Based Object Detection
- Review prior work on object detection using event cameras (both SNN and CNN approaches).
- Discuss how different event representations affect detection performance.
- Situate ETRAM in the landscape of available event-based datasets.

#### 2.6.3 SNN versus CNN Comparative Studies
- Critically review existing comparisons between SNNs and CNNs.
- Note a common weakness in the literature: many comparisons do not control for parameter count or architecture, making it hard to attribute differences to the spiking mechanism alone.
- Explicitly position this project as addressing that gap.
- This is a strong motivating argument for the methodological choices in Chapter 3.

### 2.7 Neuromorphic Hardware and Energy Modelling (~450 words)

#### 2.7.1 Neuromorphic Processor Architectures
- Introduce prominent neuromorphic platforms (Intel Loihi, IBM TrueNorth, BrainScaleS) at a high level.
- Explain the key architectural differences from GPUs: massively parallel, event-driven, co-located memory and compute, native support for spike-based communication.
- Acknowledge that real deployment on neuromorphic hardware was outside the scope of this project; instead, latency and energy are projected analytically.

#### 2.7.2 Theoretical Energy Consumption Model
- Present the energy model formally: distinguish MAC operations (CNN) from AC operations (SNN).
- Cite published estimates for energy-per-MAC and energy-per-AC on neuromorphic hardware (e.g., from Loihi datasheets or published benchmarks).
- Explain how spike rate (firing rate) is the key SNN-specific variable: a lower firing rate means fewer AC operations and lower energy.
- Present the formula used to calculate theoretical energy savings. This model will be applied in Section 4.3.
- **Suggested figure**: a diagram contrasting CNN MAC operations with SNN AC operations.

---

## Chapter 3 — Methodology and System Design
**Target: ~3,000 words**

This chapter must give enough detail that a reader could reproduce your system. It describes *what* you built and *how* you built it — but not the results. Every design choice should be briefly justified by reference to the Background chapter.

### 3.1 Design Overview and Guiding Principles (~200 words)
- Open with a brief overview of the system: two models (SNN and CNN) sharing a common architecture, trained and evaluated on ETRAM.
- State the core design constraint: **parameter count parity**. Both models must have the same number of learnable parameters to ensure a fair comparison. All differences in performance can then be attributed to the spiking mechanism, not model capacity.
- Consider including a high-level system diagram showing the data flow: event data → preprocessing → SNN/CNN → detection output → evaluation metrics.
- **Suggested figure**: a system overview block diagram.

### 3.2 Dataset Preparation (~350 words)

#### 3.2.1 PREPROCESSING TECHNIQUE (Event-to-Frame Conversion)
- Describe in detail how raw event data (or pre-converted frames from PRECOMPUTED_10K_HD_REPLICA) was prepared for input.
- State the input resolution used (e.g., 640×640 based on the script arguments `replica_640`).
- If the dataset was pre-computed, explain what the precomputation entailed and why that approach was chosen.

#### 3.2.2 NORMALISATION AND AUGMENTATION TECHNIQUE
- Describe any normalisation applied (e.g., pixel intensity normalisation to [0, 1] or standardisation).
- Describe any data augmentation used during training (e.g., random horizontal flip, random crop, colour jitter). Note that augmentation strategies for event frames may differ from RGB images.
- Justify choices: augmentation should be carefully chosen so as not to violate the physical properties of event data.

#### 3.2.3 Train and Validation Split
- State the exact split used (e.g., the `val` directory of PRECOMPUTED_10K_HD_REPLICA was used for evaluation).
- State the total number of samples in each split.
- Note any class imbalance and how (if at all) it was addressed.

### 3.3 Shared Model Architecture (~400 words)

#### 3.3.1 BACKBONE ARCHITECTURE DESIGN
- Describe the backbone: the sequence of layers, their types (convolutional/spiking convolutional), and how they process the input spatially.
- Use a table or diagram to summarise the architecture (layer type, input size, output size, number of filters).
- Note the specific model variant used: `best_model_8x8.pt` suggests an 8×8 feature grid output — explain what this means in the context of the detection head.
- **Suggested figure**: architecture diagram showing the full model pipeline from input to output.
- **Suggested table**: layer-by-layer summary with dimensions.

#### 3.3.2 DETECTION HEAD DESIGN
- Describe how the backbone features are used to predict bounding boxes and class scores.
- Explain the output format (e.g., grid cells, anchor boxes, class probabilities, objectness scores).

#### 3.3.3 Parameter Count and Fairness Constraint
- State the total parameter count for both models and confirm they are equal (or quantify any small differences and justify them).
- Explain how parameter parity was enforced during architecture design.

### 3.4 Spiking Neural Network Implementation (~550 words)

#### 3.4.1 NEURON MODEL Selection and Configuration
- State which neuron model was selected (use placeholder).
- List the specific hyperparameter values chosen (membrane time constant, threshold, reset mechanism).
- Justify the choice: why this model over alternatives?

#### 3.4.2 SPIKE ENCODING SCHEME
- Describe how the event frames were encoded into spike inputs for the SNN.
- State the encoding method and its parameters.

#### 3.4.3 Temporal Timestep Configuration
- Explain the concept of timesteps in an SNN: the input is presented for T timesteps, and the SNN integrates information over time.
- State the value of T used and justify it (a larger T captures more temporal context but increases computation).
- Note the connection to the temporal accumulation experiment (Experiment 4 in Chapter 4).

#### 3.4.4 SURROGATE GRADIENT TRAINING ALGORITHM
- State the specific surrogate function used and its parameters.
- Describe the full training algorithm: forward pass through T timesteps, BPTT, weight update.
- Reference the framework or library used to implement the SNN (e.g., SpikingJelly, snnTorch, or custom).

### 3.5 CNN Baseline Implementation (~300 words)

#### 3.5.1 Architectural Mapping from SNN to CNN
- Explain exactly how the SNN architecture was converted to a CNN: spiking neurons replaced with standard activation functions (e.g., ReLU), membrane dynamics removed.
- Confirm that the number of layers, filter sizes, and parameter count are preserved.
- Justify the use of the same architecture rather than a separately optimised CNN — this is the critical design choice that enables a fair comparison.

#### 3.5.2 Training Procedure and Hyperparameters
- State the optimiser, learning rate, batch size, number of epochs, and any learning rate scheduling.
- These should mirror the SNN training settings wherever possible.

### 3.6 Training Configuration (~300 words)

#### 3.6.1 OPTIMISER AND LEARNING RATE SCHEDULE
- State the optimiser used (e.g., Adam, SGD with momentum) and all hyperparameter values.
- Describe the learning rate schedule (e.g., cosine annealing, step decay, warmup).

#### 3.6.2 LOSS FUNCTION
- Describe the detection loss: typically a combination of localisation loss (bounding box regression) and classification loss.
- State the specific loss function and any weighting between components.

#### 3.6.3 Hardware Environment (HPC Setup)
- Describe the HPC cluster configuration: GPU type, CUDA version, number of GPUs used, available memory.
- State the total training time for each model.
- This information allows readers to assess the practicality of replication.

### 3.7 Evaluation and Benchmarking Framework (~300 words)

#### 3.7.1 Detection Accuracy Metrics
- Define the exact metrics computed by `evaluate_experiment.py`: IoU threshold used, per-class breakdown if applicable.
- Reference the script and explain its output (IoU reports and visualisations from `SNN_FINAL/` and `CNN_FINAL/` directories).

#### 3.7.2 Inference Latency Measurement Protocol
- Explain the latency benchmarking methodology: 1,000 iterations on GPU, measuring milliseconds per frame (ms/f).
- Justify 1,000 iterations as sufficient for a stable mean estimate.
- Note any warm-up iterations discarded to avoid GPU initialisation effects.

#### 3.7.3 Theoretical Energy Efficiency Model
- Reference Section 2.7.2 and explain how the model from `benchmark_energy.py` operationalises it.
- Explain the role of `spike_diagnostic.txt`: this file captures firing rates per layer, which are the key input to the energy model.
- Present the formula clearly with all variables defined.

#### 3.7.4 Projected Neuromorphic Hardware Latency Methodology
- Explain the methodology for translating GPU latency into an estimated neuromorphic hardware latency.
- Reference published conversion factors or published benchmarks for neuromorphic hardware (e.g., latency-per-synaptic-event on Loihi).
- Be transparent about the approximations involved and their limitations.

---

## Chapter 4 — Results and Evaluation
**Target: ~3,000 words**

Present results clearly and evaluate them critically. Do not separate "Results" and "Evaluation" into two chapters — combine them (as Yi Wu does effectively) so that each result is immediately contextualised. Every figure and table must be referenced in the text. Avoid presenting numbers without interpretation.

### 4.1 Detection Accuracy (~500 words)

#### 4.1.1 Overall IoU Performance: SNN versus CNN
- Present the headline accuracy results from `evaluate_experiment.py` for both models.
- **Suggested table**: side-by-side comparison of SNN and CNN IoU scores (overall and per-class if available).
- Discuss whether the accuracy gap (if any) is within the success criteria defined in Section 1.4.
- Contextualise against published results on ETRAM or comparable event-based datasets.

#### 4.1.2 Accuracy versus Object Size (Experiment 2)
- Present the grouped bar chart from `exp2_accuracy_vs_size.py`.
- **Suggested figure**: grouped bar chart comparing SNN and CNN accuracy broken down by object size category (small, medium, large).
- Discuss whether the SNN is disproportionately affected by small objects (a common challenge due to limited spatial resolution in spike representations).
- Connect to the ETRAM dataset characteristics noted in Section 2.5.2.

#### 4.1.3 Confidence Calibration Comparison (Experiment 3)
- Present the reliability diagram from `exp3_confidence_calibration.py`.
- **Suggested figure**: reliability diagrams for SNN and CNN side by side.
- Explain what a well-calibrated model looks like (diagonal line) and how each model deviates.
- Discuss whether the SNN tends to be over- or under-confident relative to the CNN.
- A calibration analysis is relatively rare in SNN papers — this distinguishes the report.

### 4.2 Inference Latency (~300 words)

#### 4.2.1 GPU Hardware Benchmarks
- Present the ms/f results from `benchmark_latency.py` for SNN and CNN.
- **Suggested table**: latency comparison table (mean, standard deviation over 1,000 iterations).
- Discuss: on standard GPU hardware, SNNs are typically *slower* than CNNs due to the overhead of temporal unrolling over T timesteps. If this is the case, acknowledge it honestly — the energy advantage of SNNs is realised only on neuromorphic hardware.

#### 4.2.2 Projected Neuromorphic Hardware Latency
- Apply the projection methodology from Section 3.7.4.
- Present the estimated latency on a representative neuromorphic platform (e.g., Intel Loihi 2).
- **Suggested table or figure**: projected latency comparison showing GPU vs neuromorphic for SNN and CNN.
- Discuss the conditions under which the SNN achieves a latency advantage.

### 4.3 Energy Efficiency (~500 words)

#### 4.3.1 Theoretical Power Consumption
- Present the output of `benchmark_energy.py`: theoretical energy consumption per inference for the SNN.
- Show the derivation from firing rates (from `spike_diagnostic.txt`) through the energy model.
- **Suggested table**: energy breakdown by layer or by model, comparing AC operations (SNN) with MAC operations (CNN).

#### 4.3.2 Dynamic Power Scatter Plot Analysis (Experiment 1)
- Present the scatter plot from `exp1_dynamic_power.py`.
- **Suggested figure**: scatter plot of dynamic power versus a relevant variable (e.g., object count per frame, spike rate).
- Discuss the variance: does dynamic power fluctuate significantly across frames? What drives high-power frames?
- Highlight the advantage of the SNN: power scales with activity, not with model size — a frame with few objects consumes less power.

#### 4.3.3 Estimated Energy Savings Relative to CNN
- Summarise the total estimated energy saving of the SNN relative to the CNN baseline.
- **Suggested figure**: a simple bar chart or annotated comparison showing SNN energy vs CNN energy per inference.
- Contextualise: does the saving come primarily from sparse activations, or from the AC-vs-MAC difference?
- Be appropriately cautious: these are *theoretical* estimates, not measured power draws from real neuromorphic hardware.

### 4.4 Temporal Dynamics (~400 words)

#### 4.4.1 Temporal Accumulation Behaviour (Experiment 4)
- Present the temporal accumulation sequence from `exp4_temporal_accumulation.py`.
- **Suggested figure**: a sequence of frames (e.g., T = 1, 2, 4, 8) showing detection confidence building up over timesteps.
- Discuss: how quickly does the SNN "converge" on a confident detection? Does more temporal context improve accuracy?
- This is one of the most visually compelling results — ensure the figure is large and legible.

#### 4.4.2 Spike Activity and Sparsity
- If spike activity data is available from `spike_diagnostic.txt`, plot the firing rate per layer.
- **Suggested figure**: bar chart or heatmap of average firing rates per layer.
- Discuss the sparsity: a low average firing rate (e.g., <10%) validates the theoretical energy model — the SNN really is sparse in practice.
- If firing rates are high (e.g., >50%), discuss the implications for energy efficiency claims.

### 4.5 Qualitative Evaluation (~400 words)

#### 4.5.1 Visual Detection Audit (Experiment 5)
- Present a representative selection of detections from the 200-sample audit (`exp5_full_validation_vis.py`).
- **Suggested figure**: a grid of 4–6 images showing side-by-side SNN and CNN detections on the same input frames. Choose examples that illustrate both successes and failures.
- Comment on the visual quality: are the bounding boxes tight? Are objects missed? Are there false positives?

#### 4.5.2 Failure Mode Analysis
- Identify systematic failure patterns: does the SNN consistently fail on a specific object class, size, or scene type?
- Compare with CNN failure modes: are the failures correlated (both models fail on the same difficult cases) or are they distinct?
- Consider: does motion blur, extreme lighting, or occlusion disproportionately affect the SNN?
- **Suggested figure**: two or three illustrative failure cases with annotations explaining why the model failed.

### 4.6 Discussion (~500 words)

#### 4.6.1 Accuracy Trade-off: SNN versus CNN
- Synthesise the accuracy results holistically: overall IoU, object-size breakdown, calibration.
- Does the SNN close the accuracy gap that was noted in the literature review (Section 2.6.1)? To what degree?
- Refer back to the success criteria from Section 1.4.

#### 4.6.2 Efficiency Trade-off: SNN versus CNN
- Synthesise the efficiency results: GPU latency, projected neuromorphic latency, theoretical energy.
- Is the efficiency advantage sufficient to justify the accuracy trade-off for the target application (traffic monitoring)?
- Discuss the "Pareto frontier" argument: the SNN may not be the best choice for pure accuracy, but it may be the best choice for accuracy-per-watt.

#### 4.6.3 Suitability for Neuromorphic Deployment
- Argue, based on the results, whether this SNN architecture is ready for deployment on neuromorphic hardware.
- Identify the remaining gaps: real hardware measurements, optimised SNN toolchains, quantisation.

#### 4.6.4 Limitations of This Study
- Be honest about what the results cannot show: (1) the energy estimates are theoretical, not measured; (2) the neuromorphic latency projection relies on published benchmarks from different architectures; (3) only the ETRAM validation set was used, so generalisation to other datasets is unproven.
- Note any training instability or hyperparameter sensitivity observed.

---

## Chapter 5 — Conclusions and Future Work
**Target: ~1,200 words**

The Conclusions chapter must not introduce new results or arguments. Its job is to close the loop opened by the Introduction — revisiting the aims, reporting whether they were achieved, and identifying what comes next.

### 5.1 Summary of Contributions (~300 words)
- Summarise the project's main contributions in three to five concise paragraphs:
  1. A matched-architecture SNN/CNN comparison on ETRAM — the first such study with controlled parameter count (if true; verify against related work in Section 2.6.3).
  2. A multi-dimensional evaluation covering accuracy, latency, and theoretical energy efficiency.
  3. Novel analytical experiments: confidence calibration, temporal accumulation, and accuracy-vs-size breakdowns that are rarely presented in comparable SNN papers.
- Avoid repeating specific numbers here; save those for the Results chapter.

### 5.2 Reflection on Aims and Success Criteria (~300 words)
- Go back through each aim listed in Section 1.3 and each success criterion in Section 1.4.
- For each, state: was it met? Partially met? Not met? Give a brief justification.
- Be honest — if an aim was not fully achieved, explain why and what would be needed to achieve it.

### 5.3 Future Work (~600 words)

#### 5.3.1 Additional Experiments to Strengthen the Study
The following experiments are recommended as natural extensions of the current benchmarking suite:

- **Timestep Sensitivity Analysis**: Train and evaluate the SNN at multiple timestep values (T = 1, 2, 4, 8, 16) and plot accuracy versus estimated energy as a Pareto curve. This reveals the fundamental trade-off between temporal context and computational cost — a key design parameter for deployment.
- **Spike Sparsity per Layer Analysis**: Extend `spike_diagnostic.txt` to report per-layer firing rates and plot them as a heatmap. This validates the energy model and identifies bottleneck layers that dominate power consumption — targets for future optimisation.
- **Synaptic Operations (SOPs) Count**: Analytically count the number of multiply-accumulate (MAC) operations performed by the CNN versus the spike-accumulate (AC) operations performed by the SNN on a per-frame basis. This gives a hardware-agnostic efficiency measure that complements the energy model.
- **Robustness to Input Noise**: Systematically add Gaussian noise or randomly drop events from the input and measure the degradation curve for both SNN and CNN. SNNs are theoretically more robust to input noise due to their temporal integration mechanism — this experiment tests that hypothesis empirically.
- **Precision-Recall Curve Comparison**: Plot full precision-recall curves across all confidence thresholds for both models. This gives a more complete picture of detection quality than a single IoU threshold and reveals whether the SNN and CNN differ in how they trade off precision against recall.

#### 5.3.2 Architectural and Training Improvements
- Explore SNN-specific architectural optimisations: attention mechanisms adapted for spiking neurons, residual connections in spiking networks, or hybrid SNN/ANN architectures.
- Investigate more advanced training methods: online learning rules (STDP) as a complement to surrogate gradients, or knowledge distillation from a pre-trained CNN teacher to an SNN student.
- Explore alternative neuron models with richer dynamics (e.g., adaptive threshold neurons) that may improve accuracy without sacrificing sparsity.

#### 5.3.3 Deployment and Scalability Directions
- Deploy the trained SNN on real neuromorphic hardware (e.g., Intel Loihi 2) to obtain measured rather than theoretical energy and latency figures.
- Investigate quantisation and model compression to further reduce the memory and compute footprint for edge deployment.
- Test the system on a broader range of event-based datasets to assess generalisation beyond ETRAM.

---

## Bibliography Notes
- Sort alphabetically by first author surname.
- Use short numeric citation format [n] in the text.
- Ensure all figures sourced from external papers cite the source in the caption (e.g., "Source: [12]").
- Manage references using a BibTeX `.bib` file — do not manage manually.
- Protect capitalised abbreviations in BibTeX titles with braces (e.g., `{SNN}`, `{ETRAM}`, `{CNN}`).

---

## Appendices

### Appendix A — Full Validation Set Results
Include the complete per-class IoU breakdown table and any additional statistics too detailed for the main body. Reference from Section 4.1.

### Appendix B — HPC Experimental Configuration
Include a table of the full hyperparameter configuration used for training both models (learning rate, batch size, epochs, GPU type, CUDA version, framework versions). This enables reproducibility without cluttering Chapter 3.

### Appendix C — Additional Visualisations
Include the full 200-sample visual audit grid (or a representative subset) from Experiment 5. Reference from Section 4.5.1. Per the lecture guidance, *do not add loads of source code* to appendices — include only the minimum needed for reproducibility, or omit entirely.

---

## Suggested Figures and Tables Summary

| Location | Type | Description |
|---|---|---|
| Sec 1.1.1 | Figure | Energy cost trends in deep learning over time |
| Sec 2.1.1 | Figure | Simple feedforward network diagram |
| Sec 2.2.1 | Figure | Convolutional layer applying filters |
| Sec 2.2.2 | Figure | Object detection pipeline: backbone → head → boxes |
| Sec 2.2.3 | Table | Evaluation metrics with formulae |
| Sec 2.3.1 | Figure | Membrane potential over time with spike event |
| Sec 2.3.2 | Figure | ReLU activation vs spiking neuron output over time |
| Sec 2.5.1 | Table | ETRAM dataset statistics |
| Sec 2.7.2 | Figure | CNN MAC operations vs SNN AC operations diagram |
| Sec 3.1 | Figure | System overview block diagram |
| Sec 3.3.1 | Figure + Table | Architecture diagram and layer-by-layer summary |
| Sec 4.1.1 | Table | SNN vs CNN IoU scores side-by-side |
| Sec 4.1.2 | Figure | Accuracy vs object size grouped bar chart (Exp 2) |
| Sec 4.1.3 | Figure | Confidence calibration reliability diagrams (Exp 3) |
| Sec 4.2.1 | Table | GPU inference latency: SNN vs CNN |
| Sec 4.2.2 | Table/Figure | Projected neuromorphic latency comparison |
| Sec 4.3.1 | Table | Energy breakdown: AC ops vs MAC ops |
| Sec 4.3.2 | Figure | Dynamic power scatter plot (Exp 1) |
| Sec 4.3.3 | Figure | Energy per inference bar chart: SNN vs CNN |
| Sec 4.4.1 | Figure | Temporal accumulation sequence (Exp 4) |
| Sec 4.4.2 | Figure | Per-layer firing rates (sparsity heatmap/bar chart) |
| Sec 4.5.1 | Figure | 4–6 image grid: SNN and CNN detections side-by-side |
| Sec 4.5.2 | Figure | 2–3 failure case examples with annotations |

---

*Plan generated by Claude — University of Manchester, COMP30040, April 2026.*
