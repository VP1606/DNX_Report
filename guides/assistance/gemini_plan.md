# Dissertation Project Plan: Spiking Neural Networks for Object Detection

This plan outlines the structure and content for your 3rd-year Computer Science dissertation report, based on the official University of Manchester guidance (COMP30040) and the Project Assessment Rubric. The strict target word limit is between 10,000 and 15,000 words.

## Front Matter
*   **Title Page** (2-line title, student ID, year, etc. - use `muthesis` class with BSc option)
*   **Abstract:** 
    *   **Rubric Requirement:** *"The abstract gives a precise and comprehensive overview of the project's achievements in its proper context."*
    *   Summary of the project's achievements, setting, and key outcomes. (Write this last).
*   **Declaration:** Standard university declaration.
*   **Copyright:** Standard university copyright statement.
*   **Acknowledgements:** Thanks to supervisor, friends, family.
*   **Contents, List of Figures, List of Tables:** (Ensure short captions are used for the lists)
*   **Abbreviations (and Acronyms):** Define terms like SNN, CNN, ETRAM, ANN, IoU, SEBlock, etc.

---

## 1. Introduction (15% of Report Grade) (~1,500 words)
**Overall Rubric Requirement:** *"The introduction gives a comprehensive and precise account of the project's setting firmly based on peer-reviewed literature and derives an evaluation strategy derived from such literature."*

*   **1.1 Context & Motivation:** 
    *   Introduce the problem of power-efficient object detection and the shift towards neuromorphic computing.
    *   **Rubric Link:** Must set the scene *"firmly based on peer-reviewed literature"*.
*   **1.2 Project Aims & Objectives:** 
    *   Clearly state challenging, substantial goals: implementing and rigorously comparing SNN and CNN architectures for object detection on the high-definition ETRAM dataset.
*   **1.3 Scope & Constraints:** 
    *   Define the boundaries of the project (e.g., local execution vs. neuromorphic hardware modeling).
*   **1.4 Evaluation Strategy:** 
    *   **Rubric Link:** Must derive *"an evaluation strategy derived from such [peer-reviewed] literature."*
    *   Explicitly state how the project will be evaluated (e.g., empirical comparison of dynamic power, confidence calibration) and prove this strategy is based on established academic methods.
*   **1.5 Report Roadmap:** A brief paragraph outlining the structure of the remaining chapters.

## 2. Background & Theory (25% of Report Grade) (~3,500 words)
**Overall Rubric Requirement:** *"There is a precise and exhaustive description of the project's setting firmly based on peer-reviewed literature. An excellent understanding of the content and relevance of the included literature is demonstrated."*

*   **2.1 Artificial Neural Networks (ANNs):** Brief overview of traditional CNNs used in object detection.
*   **2.2 Spiking Neural Networks (SNNs):** 
    *   Exhaustive description of the core concepts of SNNs, spiking neurons, temporal dynamics, and event-driven computing.
    *   **Rubric Link:** Must be *"exhaustive"* and *"firmly based on peer-reviewed literature"*.
*   **2.3 Object Detection & The ETRAM Dataset:** Discuss object detection principles, Mean Intersection over Union (IoU) metrics, and the specific characteristics of the high-definition ETRAM dataset.
*   **2.4 Hardware Considerations:** Explain the differences between local hardware (GPUs/CPUs) and Neuromorphic Hardware, focusing on power consumption and inference time.
*   **2.5 Similar Systems & Related Work:** 
    *   Comprehensive review of existing literature on SNNs vs CNNs for object detection.
    *   **Rubric Link:** Must demonstrate *"excellent understanding"* of how your work fits into this landscape, highlighting the gap in rigorous empirical comparisons to justify your project's originality.

## 3. Technical Quality, Methodology & Evaluation (35% of Report Grade) (~4,500 words)
**Overall Rubric Requirement:** *"The writing demonstrates an extremely thorough understanding of the project work and the field... Explanations of the technical details, work of the project and evaluation are exceptional."* / *"The output has been evaluated to a very high level."* / *"standard accepted methods of describing designs... an attempt has been made to formalise the description."*

*   **3.1 Requirements Analysis:** 
    *   **Rubric Link:** Explicitly addresses the "Requirements analysis" key assessment point.
    *   Formal analysis of what the system needed to achieve (e.g., equivalent parameter counts, handling 1280x720 HD inputs, real-time power tracking).
*   **3.2 System Architecture Overview:** 
    *   High-level overview of the models and pipeline.
    *   **Rubric Link:** Use *"standard accepted methods of describing designs (e.g. architecture diagrams, UML...)"*.
*   **3.3 Model Design (Formalized):**
    *   *3.3.1 CNN Baseline Architecture:* Detail the layers, parameters, and design choices.
    *   *3.3.2 SNN Architecture (SNN_MAX_REPLICA_SE):* Detail the Enhanced MAX-SE architecture. Discuss the incorporation of SE blocks, SEWResBlock, and the 16x total downsampling mechanism. 
    *   **Rubric Link:** Ensure *"designs are very well considered, clear, and easy to understand"*.
*   **3.4 Data Processing (The REPLICA Pipeline):**
    *   Detail the `PRECOMPUTED_10K_HD_REPLICA_V2` pipeline (spatiotemporal noise filtering, bilinear temporal interpolation to 10 bins, spatial downsampling).
*   **3.5 Experimental Setup & Testing Methodology:** 
    *   Design of the five core experiments.
    *   **Rubric Link:** Justify key decisions to show an *"extremely thorough understanding"*.
*   **3.6 Results & Evaluation:**
    *   *3.6.1 Dynamic Power vs. Scene Activity*
    *   *3.6.2 Accuracy vs. Object Size* (Quantization error)
    *   *3.6.3 Confidence Calibration* (Reliability Diagrams)
    *   *3.6.4 Temporal Evidence Accumulation*
    *   *3.6.5 Hardware Implications*
    *   **Rubric Link:** Prove the output is *"evaluated to a very high level"* by analyzing correctness, fitness for purpose, and performance metrics across these 5 distinct experiments.

## 4. Summary and Conclusions (15% of Report Grade) (~1,500 words)
**Overall Rubric Requirement:** *"The summary and conclusions are excellent in precision and coverage. It is clear that the student has mastered the material and has given a definitive set of conclusions and a well thought-through plan for future work to reach definitive conclusions."*

*   **4.1 Summary of Outcomes:** 
    *   Precise and excellent summary of the main findings from the empirical comparison.
*   **4.2 Aims Achieved:** 
    *   Explicitly and honestly state whether the challenging objectives from Section 1.2 were met.
*   **4.3 Critical Reflection:** 
    *   **Rubric Link:** Must contain a *"critical analysis of the work in a thorough and honest way. The ability to see weaknesses is apparent and good solutions to problems are given."*
    *   What were the weaknesses in the methodology, the model, or the dataset? How could testing have been improved?
*   **4.4 Future Work:** 
    *   **Rubric Link:** Must be a *"well thought-through plan for future work to reach definitive conclusions"* which are *"ambitious, relevant and well thought out"*.
    *   Provide a mini-proposal for future work (e.g., deployment on physical Intel Loihi chips, solving the small-object quantization error). Not just "more of the same".

## 5. Presentation, Structure and Language (10% of Report Grade)
**Overall Rubric Requirement:** *"There is very little to fault. A broad vocabulary and a thorough understanding of the English language is evident. Beautifully presented."*

*(This is an assessment criteria applied to the whole document. Ensure:)*
*   **Length:** Strictly between 10,000 and 15,000 words. (Deviation outside 8,500-16,500 fails the criteria).
*   **Structure:** Logical flow with appropriate chapters, sections, and subsections.
*   **Citations:** References perfectly formatted and consistent.
*   **Visuals:** High-quality, correctly numbered figures and tables with readable text (same size as document font).
*   **Language:** Professional grammar, spelling, no contractions, academic tone. Technical terms and abbreviations always defined.

---

## Back Matter (Not included in word count)
*   **Bibliography:** Consistent citation style (e.g., IEEE/LaTeX `abbrv` or `alpha`), sorted alphabetically by author's surname.
*   **Appendices:**
    *   Full Validation Visual Audit (Failure mode images for validation samples).
    *   Full test result tables (if too large for the Results section).
    *   Additional diagrams (e.g., SEBlock and SEWResBlock internal architecture).