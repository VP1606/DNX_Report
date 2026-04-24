---
Hash: 359a758
Branch: stronger_cleanup
Date: Fri Apr 24 2026
Time: 18:38:18 BST
Evaluator: Claude (claude-sonnet-4-6) via Cowork
---

# DetectorNX — Report Card

**Report Title:** DetectorNX: A Variable-Isolated Evaluation of Directly-Trained Spiking Neural Networks for High-Definition Automotive Perception
**Degree Programme:** BSc Computer Science (COMP30040)
**Supervisor:** Dr Oliver Rhodes
**Rubric Source:** `guides/project_assessment.pdf`

---

## Score Summary

| Rubric Section                          | Weight | Raw Score | Weighted Score |
|-----------------------------------------|--------|-----------|----------------|
| 3.1 Abstract & Introduction             | 15%    | 87/100    | 13.1 / 15      |
| 3.2 Background & Theory                 | 25%    | 70/100    | 17.5 / 25      |
| 3.3 Technical Quality & Methodology     | 35%    | 88/100    | 30.8 / 35      |
| 3.4 Summary & Conclusions               | 15%    | 88/100    | 13.2 / 15      |
| 3.5 Presentation, Structure & Language  | 10%    | 76/100    | 7.6 / 10       |
| **Overall**                             | 100%   | —         | **82.2 / 100** |

**Projected Classification: First Class (82%)**

---

## Section 3.1 — Abstract & Introduction
**Weight: 15% | Score: 87/100 | Weighted: 13.1/15**

### Justification

The abstract is exemplary for a BSc project. It opens with a tight problem statement (compute/power constraints in automotive DNNs), presents the project's methodological contribution (variable-isolated SNN–CNN pairing), and reports six specific quantitative outcomes in four sentences: 94.9% mIoU parity, 91.3% mAP₅₀ parity, 100% recall at IoU > 0.5, 94.33% energy savings with R²=0.7514 reactive scalability, 259.80 FPS throughput, and superior confidence calibration. It closes with the unexpected finding (scale-independent quantisation ceiling rather than scale-dependent), which demonstrates that the author has genuinely engaged with the results rather than just reporting positives. The claim "to the best of our knowledge, this is the first directly-trained SNN developed and evaluated on ETraM" is appropriately hedged.

Chapter 1 is among the strongest introductions seen in a BSc dissertation. The six success criteria are fully quantitative — "≥ 90% mIoU parity", "≥ 30 FPS", "within 1% parameter count", "100% recall at IoU > 0.5" — which is unusual and impressive at this level. Each criterion is directly traceable through the report to a specific experiment and a validation outcome in Chapter 4. The evaluation approach section explicitly frames the project as a controlled variable-isolation study, which is methodologically sophisticated. The report structure section maps each chapter clearly.

### Strengths

- Abstract contains six specific numerical results, not vague summaries.
- Novelty claim is properly hedged ("to the best of our knowledge").
- Six quantitative, testable success criteria — rare for a BSc.
- Traceability is established from the introduction: SC → Architecture (§3.2 Table 1) → Experiment → Validation (§4.1 Table).
- The evaluation approach explicitly defines what "success" looks like before results are presented, which is rigorous experimental practice.
- Unexpected finding (scale-independent quantisation ceiling) is surfaced in the abstract, showing intellectual honesty.

### Areas for Improvement

- The introduction does not explicitly position the work relative to the closest competitors (SpikeDet, SpikeYOLO, EMS-YOLO). A single sentence acknowledging the published landscape would strengthen the contribution statement.
- The report structure section (§1.5) is a standard walkthrough and does not explain *why* the structure was chosen — a brief justification of the chapter ordering would improve it.
- SC1 ("≥ 90% mIoU") is a numerical threshold, but the motivation for *why* 90% was the chosen bar is not explained in the introduction. A short justification referencing prior SNN work would add depth.

---

## Section 3.2 — Background & Theory
**Weight: 25% | Score: 70/100 | Weighted: 17.5/25**

### Justification

Chapter 2 covers seven topic areas: ANNs (§2.1), CNNs and residual learning (§2.2), SNNs with LIF dynamics and surrogate gradients (§2.3), event cameras (§2.4), the ETraM dataset (§2.5), neuromorphic hardware and energy models (§2.6), and related spiking detectors (§2.7). The breadth is appropriate and the chapter is well-cited with a mix of foundational (Hopfield, LeCun, He et al.) and recent (fang2022resnet_sew, Verma_2024_CVPR, fan2025spikedet) references.

The strongest sections are §2.6 and §2.7. The neuromorphic hardware section (§2.6) makes the MAC vs AC energy distinction concrete, introduces the Horowitz 45nm CMOS limits, and correctly identifies the AC/FLOP energy ratio (0.9pJ vs 4.6pJ) that underpins the energy model in Chapter 3. Related Work (§2.7) identifies the key published detectors (SpikeDet, SpikeYOLO, EMS-YOLO, E-SpikeFormer), articulates their limitations, and explicitly states the gap this project addresses. These sections are at First-class standard.

However, Chapter 2 has structural gaps that pull the score down:

**Gap 1: §2.3 SNN section is incomplete.** The Temporal Dynamics subsection (§2.3.6) ends abruptly. The section transitions from a quantisation error comment to a cross-reference to §3.7.4 without the promised discussion of TTFS and Rate-Order Coding — these appear only in the future work section of Chapter 4 (§4.4.2), which is the wrong location for background material. The SEW ResBlocks architecture, central to the entire backbone, is absent from Chapter 2; it is introduced for the first time in §3.4, meaning a reader encounters the concept with no grounding. The supervisor guidance that "background = general theory" and "methodology = specific implementation" is respected, but there is space in §2.3 to introduce the *problem* that SEW ResBlocks solve (non-binary residual sums in spiking networks) without describing the specific implementation.

**Gap 2: §2.4 is significantly thinned.** The Spatiotemporal Voxelization subsection was removed from §2.4. This is the dominant event representation technique used in the project, and a reader encountering §3.3 (which uses voxelization throughout) has no background introduction to the concept. The event representation tuple e=(x,y,t,p) definition was also removed, meaning §3.3 re-introduces it on line 4 without a Ch2 anchor.

**Gap 3: Multi-box detection and regression head design are not covered.** Chapter 3 introduces the GIoU loss, SmoothL1, BCEWithLogitsLoss, and greedy assignment matching, all of which are presented without any background foundation. A short §2.2.x on modern detection head design (YOLO-style regression, IoU-based losses) would significantly improve the readability of Chapter 3.

**Gap 4: Pipeline naming consistency.** Within the files I read, the pipeline is consistently called BOLT, which is good. However, any remaining REPLICA references elsewhere would constitute an inconsistency that a marker would note.

The bibliography has several entries that likely carry incorrect metadata (he2015deep→2016, fang2022resnet_sew→NeurIPS 2021, cordone→IJCNN 2022 not ACM), which would be noted by a thorough examiner.

### Strengths

- §2.6 and §2.7 are First-class quality: precise energy constants, clear competitive landscape, explicit gap statement.
- Good use of equations for LIF dynamics (membrane potential and Heaviside spike function) with parameter labelling.
- The neuromorphic hardware section correctly distinguishes theoretical minimum energy (Horowitz) from real silicon overhead, showing depth of understanding.
- Related Work covers both the SNN detection progression and the event-camera detection landscape as separate threads, then synthesises the gap.
- Well-cited: breadth from foundational (1980s–2010s) to current (2023–2025) literature.
- §2.5 (ETraM) is concise and factually accurate, noting the HD resolution, static mounting, and manual annotation quality.

### Areas for Improvement

- **Restore or add a brief Spatiotemporal Voxelization subsection in §2.4.** Even 200 words defining the 4D tensor shape `[T, C, H, W]` would anchor the reader before §3.3.
- **Add a note on the SEW problem in §2.3** (non-binary residual addition destroys sparsity) without going into implementation details — this is background theory, not implementation.
- **Complete §2.3.6 Temporal Dynamics** with the TTFS and ROC encoding sentences that are currently missing.
- **Add a short subsection on modern object detection loss design** (regression losses, IoU variants) under §2.2, so GIoU and BCEWithLogitsLoss in §3.9 are not encountered cold.
- Verify and correct bibliography metadata (publication years, venues) for the flagged entries.

---

## Section 3.3 — Technical Quality & Methodology
**Weight: 35% | Score: 88/100 | Weighted: 30.8/35**

### Justification

Chapter 3 is the strongest chapter and the primary reason this project merits a First classification. The methodology is documented to a level of rigour and detail that exceeds typical BSc output and approaches taught MSc quality. The chapter spans requirements (§3.1), system architecture (§3.2), data preprocessing (§3.3), SNN architecture (§3.4), CNN baseline (§3.5), architectural evolution (§3.6), experimental setup (§3.7), and results with analysis (§3.8), followed by a complete training specification (§3.9).

**Experimental design** is where the project excels. The variable-isolation principle (fixed BOLT pipeline, fixed regression head, interchangeable backbone) is consistently enforced and explicitly stated in §3.2. The traceability table (Table 3.2.1) maps each of the six success criteria to an architectural mechanism and a validating experiment — a level of methodological rigour rarely seen at BSc level. The six experiments (global evaluator, dynamic power, real-time latency, temporal evidence, quantisation error, confidence calibration) constitute a genuinely multidimensional evaluation: spatial accuracy, energy consumption, reactive scalability, inference latency, object-size-dependent error, and predictive reliability. Each experiment includes a hypothesis section, a setup section, results, and critical analysis.

**BOLT Pipeline (§3.3)** is thoroughly documented: box-central sampling strategy with justification (guarantees 100% label coverage), 100ms window choice anchored in human visual persistence (~100ms), density filter (min_events=500) with dual justification (SNN gradient flow + background activity noise), signal conditioning steps lifted and adapted from Verma et al. 2024, spatiotemporal voxelisation producing `[10, 2, 720, 1280]` tensors, Max-Pooling downsampling with justification (feature preservation vs Average-Pooling), max-normalisation with explicit tie to Vth=0.2 threshold, multi-object label alignment with fixed-capacity padding and binary masking, and the LRU-cached chunking strategy that reduces 150-epoch training time to ~6 hours. This is an exceptionally complete pipeline description.

**SNN Architecture (§3.4)** correctly motivates every design decision. The SEW residual paradigm is explained with the core proof (`1+1=2` breaks sparsity), justified by citing Fang et al. 2022, and tied to the specific failure mode it prevents. The SE block is introduced at the correct bottleneck location (Stage 3, 22×40) with a two-part justification (spatial constraint + semantic shift). The FRR penalty is given both the biological motivation (metabolic sparsity) and the implementation justification (prevents silencing and over-saturation). The hyperparameter choices (Vth=0.2, τ=4.0, T=10) are individually justified with reference to empirical tuning during architectural evolution. The LIF threshold tuning narrative ("V_th=0.3 silenced the network; decreasing further submitted background noise") is a good example of showing rather than just claiming.

**Energy results** are particularly strong: the mathematical validation of the mean energy figures (§3.8, dynamic power) demonstrates internal consistency to within 0.01%, and the reactive scalability analysis (linear regression of event count vs energy, R²=0.7514, y-intercept as resting metabolic cost, slope as per-event cost) is a genuinely insightful framing. The platform extrapolation table (Table 3.8.2) is honest about its assumptions.

**The efficiency landscape comparison (Table 3.8.4)** is methodologically careful — the two confounds (COCO vs ETraM, 80-class vs binary) are explicitly stated with the correct conclusion that the finding "hints at" rather than proves superior efficiency.

**Architectural evolution (§3.6)** shows intellectual development across four generations (Phase 0 → G1 → G2 → G3), documenting what failed and why at each stage, which is exactly what an examiner wants to see.

**Minor issues:**

1. §3.7 text says "five distinct experimental protocols" but the section lists 7 experiments (Global Evaluator, Dynamic Power, Theoretical Energy, Real-Time Latency, Temporal Evidence, Quantisation Error, Confidence Calibration). This is a minor internal inconsistency.

2. §3.8/temporal.tex has a remaining todo: "Fix Inconsistencies and rewrite prose." The temporal evidence section also has a figure reference inconsistency: both the "Hunting Behaviour" paragraph and the "High-confidence early detection" paragraph cite `\ref{fig:temp_seq_2}` — but both cannot be sequence 2. Based on the captions (`sequence_0.png`, `sequence_2.png`, `sequence_4.png`), Hunting Behaviour should reference `fig:temp_seq_0` or `fig:temp_seq_1`. This will appear as two paragraphs both pointing to the same figure in the compiled PDF.

3. §3.8/confidence_calibration.tex contains a prose error: "more honest regarding ambiguous features., and" — a comma followed by a period.

4. §3.8/theoretical_energy.tex has a remaining todo: "Edit CMOS reference — might not be correct." The Horowitz 2014 reference underpins the theoretical minimum energy claim; if this is wrong, the 94.33% optimality claim in §3.8 loses its grounding.

5. A typo exists in the energy consumption section: "as supposed to" should read "as opposed to."

6. The quantisation error analysis (§3.8.2) deserves brief acknowledgement that the result invalidating the original hypothesis is a genuine contribution — the current analysis makes this point but undersells it. Finding that your hypothesis was wrong and explaining why is scientifically more valuable than confirming it.

### Strengths

- Variable-isolation experimental design enforced consistently throughout; SC traceability table in §3.2 is exceptional.
- BOLT pipeline is documented to production-code quality (box-central sampling, LRU cache, chunked I/O, density filter).
- Mathematical validation of energy calculations to ±0.01% proves internal consistency.
- Four-generation architectural evolution with failure-mode documentation shows genuine engineering rigour.
- Reactive scalability framing (y-intercept = resting metabolic cost, slope = per-event cost) is a novel and well-articulated insight.
- Efficiency landscape comparison is methodologically honest about its confounds.
- Full hyperparameter tables in both the body (§3.9) and appendix (App. A) — completeness is excellent.
- Training structure is justified end-to-end: each hyperparameter choice is tied to a failure mode it addresses.
- Multi-box detection head dual-pool design (Avg+Max summation) is properly motivated by the specific "ghost detection" failure mode observed in G2.

### Areas for Improvement

- Fix the figure reference inconsistency in §3.8/temporal.tex (both "Hunting Behaviour" and "High-confidence early detection" cite `fig:temp_seq_2`).
- Rewrite the temporal evidence prose (noted by the todo) — in particular the "Hunting Behaviour" paragraph mixes discussion of two different sequences.
- Fix "as supposed to" → "as opposed to" in the energy section.
- Fix the comma/period error in confidence calibration ("ambiguous features., and").
- Resolve the "five distinct experimental protocols" vs. seven experiments inconsistency in §3.7.
- Verify the CMOS/Horowitz reference before submission.
- Consider adding a brief discussion in the quantisation error section explicitly framing the hypothesis invalidation as a positive scientific finding.

---

## Section 3.4 — Summary & Conclusions
**Weight: 15% | Score: 88/100 | Weighted: 13.2/15**

### Justification

Chapter 4 is a well-structured and honest conclusion. The outcomes section (§4.1) consolidates results against all six success criteria in a validation table (Table 4.1.2), with the achieved result stated precisely against the quantitative target. This direct SC-to-result pairing, consistent with the traceability table established in §3.2, gives the chapter a rigorous closure that ties the entire report together. The "Reactive Scalability" and "Bounding Box Sharpening" findings are surfaced as emergent behaviours beyond the original criteria, which shows the author has genuinely reflected on what the results mean, not just whether targets were hit.

The critical reflection section (§4.2) is notably strong. Four distinct limitations are identified with specificity:
1. Hardware-paradigm inequity — the GPU simulation penalty (5.4× throughput gap documented, not just asserted).
2. Temporal quantisation ceiling — the 1/T = 10% rate-coding resolution limit, cited to Thorpe et al. 2001.
3. Detection head mismatch — the shared float-based head's inability to interpret SNN temporal oscillation, introduced as a deliberate methodological constraint rather than an oversight.
4. Dataset domain gap — ETraM's static roadside perspective vs. vehicle-mounted ego-motion artefacts, with honest justification for why ETraM was chosen anyway.

The future work section is specific and actionable: adaptive timestepping, TTFS encoding, Rate-Order Coding, SNN-native membrane-regression head, ETraM→GEN1 domain adaptation, and CARLA integration. Each future direction is directly tied to a limitation identified in the same section, which shows systematic thinking.

The chapter is appropriately honest: it does not overstate the 94.33% energy savings (correctly noting these are theoretical, on GPU hardware, measured against a stronger baseline than neuromorphic silicon), and the efficiency landscape comparison is explicitly caveated.

### Strengths

- SC validation table closes the loop on every criterion stated in the introduction.
- Four limitations are each substantive and specific, not vague ("further work is needed").
- The detection head mismatch section shows mature awareness: the shared head was a deliberate constraint to protect variable isolation, not an error.
- Future work is actionable and technically grounded (CARLA, TTFS, domain adaptation strategy).
- The "Reactive Scalability" framing of the energy result is a genuine insight surfaced in the conclusions.
- Dataset selection justification (manual label fidelity over GEN1 automated labels) is intellectually honest.

### Areas for Improvement

- The outcomes section briefly mentions "Bounding Box Sharpening" (§4.1.3) as a finding from the temporal evidence experiment, but this result is partially undermined by the "hunting behaviour" observed in dense scenes. A more balanced treatment — acknowledging both the sharpening cases and the hunting failures — would make the conclusion more scientifically rigorous.
- The real-time viability section (§4.1.4) claims "validates immediate viability for live deployment in V2X and ADAS systems" but the hardware is a cloud A100 GPU, not edge hardware. This slightly overstates the implication; qualifying "on GPU hardware" would be more precise.
- The CARLA future work item is ambitious and interesting — a sentence estimating what improvement in emergency braking distance would constitute success would make it more testable.

---

## Section 3.5 — Presentation, Structure & Language
**Weight: 10% | Score: 76/100 | Weighted: 7.6/10**

### Justification

The report is professionally structured and the technical writing is generally clear and precise. The use of named architectural labels (`DetectorNX-G3-SNN`, `SEWResBlock`, `VoxelDiskDataset`) is consistent. Equations are properly numbered and labelled. All tables and figures have captions with short titles for the list of figures. The appendix hyperparameter tables are detailed and complete. The glossary and list of abbreviations are included. The bibliography uses a consistent numeric citation style throughout.

However, several specific issues reduce the presentation score:

**Language errors:**
- "as supposed to" should be "as opposed to" (energy consumption section).
- "more honest regarding ambiguous features., and" — comma and period together (confidence calibration section).
- §4.1.1: "utilising the SpikingJelly library's multi-step execution paradigm" — starts a sentence with lowercase "utilising" following a paragraph break (§4.2.1, line 11).
- Some over-reliance on intensifying adverbs ("drastically reduce", "massive, static", "definitively validates", "conclusive proof") — academic tone is better served by letting the numbers speak.
- §3.4 introduction: "The core focus, effort and innovation of this project is the development..." — this phrasing is slightly informal for an academic methodology section.

**Structural issues:**
- §3.7 states "five distinct experimental protocols" but the section contains seven sub-experiments. A reader counting along will notice the mismatch.
- The temporal evidence results section (§3.8/temporal.tex) references `fig:temp_seq_2` for both the Hunting Behaviour paragraph and the High-confidence early detection paragraph — both cannot reference the same sequence. In the compiled PDF this will appear as two different analyses of the same figure.
- §2.3.6 appears to end mid-thought (the temporal dynamics section closes without the TTFS/ROC sentences that are later surfaced in §4.2.2 as future work — the background section needs to at least introduce the concepts).

**Positive formatting notes:**
- All todo notes are suppressed in the compiled PDF via the `[disable]` flag on the `todonotes` package — this is handled correctly and markers will not see them.
- The chapter structure is logical and the progressive disclosure (requirements → design → experiments → results → conclusions) follows a clean narrative arc.
- Figures are well-placed and captioned; the multi-panel energy comparison figure (SNN vs CNN vs merged) is particularly effective.
- The `\listoftodos` command remains in `report.tex` — with `[disable]` active this produces an empty list, which is harmless but slightly untidy.

### Strengths

- Consistent use of named model variants throughout the report.
- Tables and figures are well-captioned and list-of-figures short titles are provided.
- Complete appendix hyperparameter tables reduce the main-body word count while preserving reproducibility.
- Bibliography is consistently formatted (numeric BibLaTeX style).
- The overall narrative arc from Introduction → Background → Methodology → Results → Conclusions is clear and well-paced.
- Glossary is used consistently (GLS macros throughout).

### Areas for Improvement

- Fix "as supposed to" → "as opposed to".
- Fix the double punctuation ("features., and") in the confidence calibration section.
- Fix the figure reference duplication in the temporal evidence section.
- Remove `\listoftodos` from `report.tex` or confirm it produces no output in the compiled version (it is currently harmless but should be cleaned up).
- Reduce reliance on intensifiers ("massive", "definitively", "conclusive") in favour of qualified quantitative statements.
- Correct §3.7 to say "seven experimental protocols" or restructure the subsection numbering.
- Check and correct bibliography metadata for the flagged entries (he2015deep, fang2022resnet_sew, cordone, hu2019_se_block).

---

## Overall Observations

**What is done exceptionally well:**

This is a project that demonstrates genuine intellectual ownership of the problem. The variable-isolation framing is not just stated — it is enforced architecturally (shared BOLT pipeline, shared regression head, parameter-matched backbone) and evidenced empirically (0.09% parameter delta). The multidimensional evaluation going beyond accuracy to include energy, latency, calibration, size-dependent error, and temporal dynamics is well above average for a BSc project. The architectural evolution narrative is the kind of honest "here is what failed and why" documentation that examiners value but rarely see. The energy analysis is rigorous: mathematical validation to ±0.01%, reactive scalability regression, platform extrapolation, and a comparative landscape — all with appropriate caveats about their limitations. Chapter 4's limitations section is intellectually mature: it does not hide the 5.4× latency penalty or the hunting behaviour, and it explains *why* these occur rather than apologising for them.

**What needs the most attention before final submission:**

1. **Chapter 2 gaps** — The missing voxelization background (§2.4) and the abrupt end of §2.3.6 are the most significant remaining structural issues. A reader should not encounter the core event representation technique for the first time in §3.3. Restoring a concise voxelization subsection to §2.4 and completing §2.3.6 would push the background score from Upper Second territory into First.

2. **Temporal section rewrite** — The todo "Fix Inconsistencies and rewrite prose" in §3.8/temporal.tex is valid. The figure reference duplication is an error that will appear in the compiled PDF. The prose currently conflates two different sequence analyses under the same figure reference. This section needs a targeted rewrite.

3. **Minor language errors** — "as supposed to", the double punctuation mark, and the "five protocols / seven experiments" inconsistency are the kind of issues that do not affect the science but do affect the presentation mark.

4. **CMOS reference verification** — The Horowitz 2014 paper ("1.1 computing's energy problem") is the anchor for the theoretical minimum energy savings claim. If it does not support the specific 45nm CMOS figures used, the energy extrapolation section loses credibility. This should be verified before submission.

---

*Evaluation performed by Claude (claude-sonnet-4-6) via Anthropic Cowork on the commit at the above hash. All observations are based on a full read of every .tex source file in the report. No files were edited during this evaluation.*
