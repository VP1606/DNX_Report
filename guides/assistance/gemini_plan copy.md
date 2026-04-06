# Dissertation Project Plan: Spiking Neural Networks for Object Detection

This plan outlines the structure and content for your 3rd-year Computer Science dissertation report, based on the official University of Manchester guidance (COMP30040). The target word count is approximately 12,000 words.

## Front Matter
*   **Title Page** (2-line title, student ID, year, etc. - use `muthesis` class with BSc option)
*   **Abstract:** Summary of the project and key outcomes (write this last).
*   **Declaration:** Standard university declaration.
*   **Copyright:** Standard university copyright statement.
*   **Acknowledgements:** Thanks to supervisor, friends, family.
*   **Contents**
*   **List of Figures:** (Ensure short captions are used for the list)
*   **List of Tables:** (Ensure short captions are used for the list)
*   **Abbreviations (and Acronyms):** Define terms like SNN, CNN, ETRAM, ANN, etc.

---

## 1. Introduction (~1,200 words / 10%)
*   **1.1 Context & Motivation:** Introduce the problem of power-efficient object detection and the shift towards neuromorphic computing.
*   **1.2 Project Aims & Objectives:** Clearly state the goals: implementing and comparing SNN and CNN architectures for object detection on the ETRAM dataset.
*   **1.3 Scope & Constraints:** Define the boundaries of the project (e.g., using a specific dataset, local vs. neuromorphic hardware limits).
*   **1.4 Report Roadmap:** A brief paragraph outlining the structure of the remaining chapters.

## 2. Background & Literature Review (~3,600 words / 30%)
*   **2.1 Artificial Neural Networks (ANNs):** Brief overview of traditional CNNs used in object detection.
*   **2.2 Spiking Neural Networks (SNNs):** Explain the core concepts of SNNs, spiking neurons, and how they differ from standard ANNs (event-driven, biologically inspired).
*   **2.3 Object Detection & The ETRAM Dataset:** Discuss object detection principles and the specific characteristics of the ETRAM dataset.
*   **2.4 Hardware Considerations:** Explain the differences between local hardware (GPUs/CPUs) and Neuromorphic Hardware, focusing on power consumption and inference time.
*   **2.5 Similar Systems & Related Work:** Review existing literature on SNNs vs CNNs for object detection. Highlight advantages, disadvantages, and the specific problem your project addresses.

## 3. Design & Methodology (~3,000 words / 25%)
*   **3.1 System Architecture:** High-level overview of the models.
*   **3.2 Model Design:**
    *   *3.2.1 CNN Architecture:* Detail the layers, parameters, and design choices.
    *   *3.2.2 SNN Architecture:* Detail how the CNN architecture is adapted for SNN (ensuring parameter counts match), encoding techniques (e.g., rate coding, temporal coding).
*   **3.3 Data Processing (PREPROCESSING TECHNIQUE):** Abstracted steps for preparing the ETRAM dataset for both CNN and SNN training.
*   **3.4 Experimental Setup & Testing Methodology:**
    *   Metrics definitions (Power Consumption, Inference Time, Accuracy/mAP).
    *   Design of tests for local hardware.
    *   Simulation/Estimation methodology for Neuromorphic hardware inference time.

## 4. Results (~1,500 words)
*   **4.1 Training Metrics:** Graphs showing loss and accuracy during training for both models.
*   **4.2 Inference Time (Local Hardware):** Tables/Charts comparing the execution time.
*   **4.3 Predicted Inference Time (Neuromorphic HW):** Present the calculated/simulated expectations.
*   **4.4 Power Consumption Analysis:**
    *   *4.4.1 Overall Power Savings:* Comparison of energy used per inference.
    *   *4.4.2 Dynamic Power Scatter Plot:* Visual representation of power usage over time/events.
*   *Note: Keep raw, extensive data for appendices.*

## 5. Evaluation & Discussion (~1,500 words)
*(Note: Combined Results & Evaluation is 25% ~ 3000 words)*
*   **5.1 Performance vs. Efficiency Trade-off:** Discuss the results. Does the SNN sacrifice accuracy for power savings compared to the CNN?
*   **5.2 Hardware Implications:** Evaluate what the results mean for real-world deployment on neuromorphic chips vs standard accelerators.
*   **5.3 Critical Analysis:** Did the system meet the initial aims? What were the limitations of the methodology or the ETRAM dataset?

## 6. Conclusions & Further Work (~1,200 words / 10%)
*   **6.1 Summary of Outcomes:** Briefly restate the main findings from the comparison.
*   **6.2 Aims Achieved:** Explicitly state whether the objectives from Section 1.2 were met.
*   **6.3 Future Work:**
    *   Suggest testing on physical neuromorphic hardware (e.g., Intel Loihi).
    *   Suggest exploring different SNN encoding schemes or more complex datasets.
    *   *Suggested Extra Experiment:* Analyze the impact of sparsity in the ETRAM dataset on the SNN's dynamic power consumption.

---

## Back Matter
*   **Bibliography:** Ensure consistent citation style (e.g., IEEE/LaTeX `abbrv` or `alpha`), sorted alphabetically.
*   **Appendices:**
    *   Full test result tables (if too large for the Results section).
    *   Additional diagrams or configuration details.
    *   *(Do not include large dumps of source code).*