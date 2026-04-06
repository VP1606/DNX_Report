# Dissertation Project Plan: Spiking Neural Networks for Object Detection

This plan outlines the structure and content for your 3rd-year Computer Science dissertation report, based on the official University of Manchester guidance (COMP30040) and the Project Assessment Rubric. The strict target word limit is between 10,000 and 15,000 words.

## Front Matter
*   **Title Page** (2-line title, student ID, year, etc. - use `muthesis` class with BSc option)
*   **Abstract:** A precise and concise summary of the project's achievements, setting, and key outcomes. (Write this last).
*   **Declaration:** Standard university declaration.
*   **Copyright:** Standard university copyright statement.
*   **Acknowledgements:** Thanks to supervisor, friends, family.
*   **Contents**
*   **List of Figures:** (Ensure short captions are used for the list)
*   **List of Tables:** (Ensure short captions are used for the list)
*   **Abbreviations (and Acronyms):** Define terms like SNN, CNN, ETRAM, ANN, IoU, SEBlock, etc.

---

## 1. Introduction (15% of Report Grade) (~1,500 words)
*   **1.1 Context & Motivation:** Introduce the problem of power-efficient object detection and the shift towards neuromorphic computing. Set the scene firmly based on peer-reviewed literature.
*   **1.2 Project Aims & Objectives:** Clearly state challenging, substantial goals: implementing and rigorously comparing SNN and CNN architectures (specifically SNN_MAX_REPLICA_SE) for object detection on the high-definition ETRAM dataset.
*   **1.3 Scope & Constraints:** Define the boundaries of the project (e.g., local execution vs. neuromorphic hardware modeling).
*   **1.4 Evaluation Strategy:** **[CRITICAL FOR RUBRIC]** Explicitly state how the project will be evaluated (e.g., empirical comparison of dynamic power, confidence calibration, and quantization error against a CNN baseline). Explain *why* this strategy was chosen.
*   **1.5 Report Roadmap:** A brief paragraph outlining the structure of the remaining chapters.

## 2. Background & Theory (25% of Report Grade) (~3,500 words)
*   **2.1 Artificial Neural Networks (ANNs):** Brief overview of traditional CNNs used in object detection.
*   **2.2 Spiking Neural Networks (SNNs):** Exhaustive description of the core concepts of SNNs, spiking neurons, temporal dynamics, and event-driven computing, based entirely on peer-reviewed literature.
*   **2.3 Object Detection & The ETRAM Dataset:** Discuss object detection principles, Mean Intersection over Union (IoU) metrics, and the specific characteristics of the high-definition ETRAM dataset.
*   **2.4 Hardware Considerations:** Explain the differences between local hardware (GPUs/CPUs) and Neuromorphic Hardware, focusing on power consumption and inference time.
*   **2.5 Similar Systems & Related Work:** Comprehensive review of existing literature on SNNs vs CNNs for object detection. Highlight the gap in rigorous empirical comparisons of learning dynamics, confidence calibration, and temporal evidence to justify your project's originality.

## 3. Technical Quality, Methodology & Evaluation (35% of Report Grade) (~4,500 words)
*(Note: This section combines Design, Implementation, and Results per the rubric structure)*
*   **3.1 Requirements Analysis:** **[CRITICAL FOR RUBRIC]** Formal analysis of what the system needed to achieve (e.g., equivalent parameter counts, handling 1280x720 HD inputs, real-time power tracking).
*   **3.2 System Architecture Overview:** High-level overview of the models and the overall pipeline from raw data to inference, using standard design diagrams (e.g., UML, block diagrams).
*   **3.3 Model Design (Formalized):**
    *   *3.3.1 CNN Baseline Architecture:* Detail the layers, parameters, and design choices.
    *   *3.3.2 SNN Architecture (SNN_MAX_REPLICA_SE):* Detail the Enhanced MAX-SE architecture. Discuss the incorporation of Squeeze-and-Excitation (SE) blocks, Spike-Element-Wise Residual blocks (SEWResBlock), and the 16x total downsampling mechanism.
*   **3.4 Data Processing (The REPLICA Pipeline):**
    *   Detail the `PRECOMPUTED_10K_HD_REPLICA_V2` pipeline. Include spatiotemporal noise filtering, bilinear temporal interpolation (10 bins), and spatial downsampling (ds=2 -> 640x360).
*   **3.5 Experimental Setup & Testing Methodology:** Design of the five core experiments. Justify the testing decisions.
*   **3.6 Results & Evaluation:**
    *   *3.6.1 Dynamic Power vs. Scene Activity:* Results mapping input event counts to real-time SNN energy consumption per frame vs. CNN fixed energy.
    *   *3.6.2 Accuracy vs. Object Size:* Investigation of "quantization error" in SNNs by categorizing detected objects by pixel area.
    *   *3.6.3 Confidence Calibration:* Reliability Diagrams (Confidence vs. actual IoU) comparing model overconfidence.
    *   *3.6.4 Temporal Evidence Accumulation:* Analysis of bounding box sharpening from t=20ms to t=100ms.
    *   *3.6.5 Hardware Implications:* Tables/Charts comparing local execution time and simulated expectations for Neuromorphic hardware.

## 4. Summary and Conclusions (15% of Report Grade) (~1,500 words)
*   **4.1 Summary of Outcomes:** Precise and excellent summary of the main findings from the empirical comparison.
*   **4.2 Aims Achieved:** Explicitly and honestly state whether the challenging objectives from Section 1.2 were met. Provide compelling reasons if any were not fully met.
*   **4.3 Critical Reflection:** **[CRITICAL FOR RUBRIC]** A thorough and honest critical analysis of your own work. What were the weaknesses in the methodology, the model, or the dataset? How could the testing have been improved?
*   **4.4 Future Work:** Provide ambitious, relevant, and well-thought-out ideas for future work that could realistically take the project further (e.g., deployment on physical Intel Loihi chips, solving the small-object quantization error).

## 5. Presentation, Structure and Language (10% of Report Grade)
*(This is an assessment criteria applied to the whole document, not a specific chapter. Ensure:*
*   *Length is strictly between 10,000 and 15,000 words.*
*   *References are perfectly formatted and consistent.*
*   *High-quality, correctly numbered figures and tables with readable text.*
*   *Professional grammar, spelling, and academic tone.*
*   *Technical terms and abbreviations are always defined.)*

---

## Back Matter (Not included in word count)
*   **Bibliography:** Ensure consistent citation style (e.g., IEEE/LaTeX `abbrv` or `alpha`), sorted alphabetically by author's surname.
*   **Appendices:**
    *   Full Validation Visual Audit (Failure mode images for validation samples).
    *   Full test result tables (if too large for the Results section).
    *   Additional diagrams (e.g., SEBlock and SEWResBlock internal architecture).
    *   *(Do not include large dumps of source code).*