---
Hash: cc59984
Branch: draft2
Date: Thu Apr 30 2026
Time: 14:19:11 BST
Evaluator: Claude (claude-opus-4-7) — calibrated to supervisor feedback in `supervisor_notes.md`
---

# DetectorNX — Report Card (Supervisor-Calibrated)

**Report Title:** DetectorNX — controlled SNN/CNN comparison for HD automotive vehicle detection on event-camera data
**Degree Programme:** BSc Computer Science (COMP30040)
**Supervisor:** Dr Oliver Rhodes
**Rubric Source:** `guides/project_assessment.pdf`
**Calibration Note:** This evaluation is intentionally aligned to the supervisor's feedback recorded in `supervisor_notes.md`. Where the supervisor flagged specific concerns, the marking weights those concerns in proportion to how a real second-marker reading the same draft would likely respond.

---

## Score Summary

| Rubric Section | Weight | Raw | Weighted |
|---|---|---|---|
| 3.1 Abstract & Introduction | 15% | 78 | 11.7 / 15 |
| 3.2 Background & Theory | 25% | 65 | 16.25 / 25 |
| 3.3 Technical Quality, Methodology & Evaluation | 35% | 75 | 26.25 / 35 |
| 3.4 Summary & Conclusions | 15% | 75 | 11.25 / 15 |
| 3.5 Presentation, Structure & Language | 10% | 62 | 6.2 / 10 |
| **Overall** | 100% | — | **~72 / 100** |

**Projected band:** Above Expectations / boundary of First Class.

---

## Headline (mirroring supervisor's tone)

This is a nice piece of work. The experimental setup is well-described, the presentation of findings is clear, and the critical analysis is good. **However, the most pressing issue across the report is the absence of diagrams** — particularly in the Background chapter — which represents a missed opportunity to communicate technical concepts to a second marker who may be unfamiliar with the field. A handful of structural and factual refinements would push this from a strong Above Expectations to a comfortable First.

---

## Section 3.1 — Abstract & Introduction (78/100, weighted 11.7/15)

### Justification

The abstract delivers a tight problem framing, names the project (DetectorNX) clearly, states the research question (viability + cost of the spiking paradigm), and reports six concrete numerical outcomes (94.9% mIoU parity, 91.3% mAP\textsubscript{50} parity, 100% recall, 94.33% energy saving, 259.80 FPS, superior low-confidence calibration). The novelty claim ("to the best of our knowledge, the first directly-trained SNN evaluated on ETraM") is appropriately hedged. The four-paragraph structure (problem → method → results → contribution) is conventional and easy to follow.

The introduction (Chapter 1) is well-structured: regulatory motivation, technical-squeeze problem statement, a six-criterion success specification, an evaluation-strategy summary, and a chapter-by-chapter report structure. Each criterion is quantitative and directly traceable to a validating experiment in Chapter 4.

### Strengths

- Six quantitative success criteria with traceability through the report.
- Abstract foregrounds the falsification finding (scale-stable quantisation ceiling), demonstrating engagement with results rather than pure positives.
- Introduction's CPU→GPU trajectory framing is a defensible forward-looking argument grounded in Lin's actual claims.

### Areas for Improvement

- **Add a single supporting visual** — even a small figure in the introduction or as a callout box for the regulatory framing (e.g. Euro NCAP 2026 protocol diagram) would partially address the diagram-absence concern that runs through the report.
- The introduction does not concretely position the work against published SNN object-detector competitors (SpikeDet, SpikeYOLO, EMS-YOLO, E-SpikeFormer). One sentence acknowledging these would strengthen the contribution claim where it currently stands.
- The "Why 90% mIoU?" question for SC1 is not addressed — the threshold appears chosen by convention rather than justified by reference to prior SNN work.

### Path to Outstanding (90+)

The Outstanding band for this rubric area requires: *"a precise and comprehensive overview of the project's achievements in its proper context"* (abstract) + *"a comprehensive and precise account of the project's setting firmly based on peer-reviewed literature and derives an evaluation strategy derived from such literature"* (introduction).

To reach Outstanding, the report would need:

1. **Literature-derived evaluation strategy.** Currently the six success criteria are stated as project-internal goals. Outstanding wants them visibly *derived from* prior work — e.g. "SC1 (≥ 90% mIoU parity) follows the convention established by [SpikeDet, SpikeYOLO] for evaluating spiking detectors against continuous baselines." Each criterion should have a literature-anchored justification.
2. **Explicit positioning vs. competitors in the introduction.** One sentence in §1.1 or §1.2 acknowledging SpikeDet / SpikeYOLO / EMS-YOLO / E-SpikeFormer and stating what DetectorNX adds beyond them.
3. **Abstract tightening.** The abstract is already strong, but Outstanding-band abstracts compress every claim further — replace any remaining adjective-heavy phrasing with quantitative substance.
4. **Add a single visual** in the introduction (a high-level project-architecture teaser, or a regulatory-trajectory chart) — Outstanding presentations rarely have a text-only introduction.

---

## Section 3.2 — Background & Theory (65/100, weighted 16.25/25)

### Justification

**This is where the supervisor's most pointed critique lands, and the score reflects it.** The chapter covers the necessary ground (ANNs, CNNs and residual learning, SNNs and surrogate gradients, event-based vision, ETraM, neuromorphic hardware, related work), the citations are appropriate and contemporary, and §2.6 (neuromorphic hardware) and §2.7 (related work) are individually strong — the energy economics treatment (Horowitz constants, MAC vs AC asymmetry) and the gap-statement narrative for SNN object detection are at First-class level.

**However**: the chapter is almost entirely text. There are no diagrams to break up the prose or to communicate technical concepts to a reader who has not studied the field at third-year level. This is a serious presentation-of-background issue and a major missed opportunity.

Specifically, the following concepts would benefit immediately from accompanying diagrams:

- **CNNs** — a simple block-diagram of a residual connection (skip path, identity + residual) would clarify the foundational architecture for any reader unfamiliar with He et al. 2016.
- **Surrogate gradients** — a graph showing the Heaviside step function vs the smooth surrogate (e.g. ATan) would communicate this concept far faster than the current equation.
- **Event-based vision** — a side-by-side comparison of a frame-based output vs. an event-stream output would land in seconds where the prose currently takes paragraphs.
- **ETraM dataset extracts** — at minimum a single sample frame from the dataset would orient the reader. Currently the dataset is described entirely through prose and tables.
- **Spike trains / temporal binning** — a visualisation of how T = 10 timesteps quantise a continuous signal would anchor the rate-coding discussion.
- **SEWResBlock vs standard ResBlock** — even a simple two-panel diagram would make the §3.4 architectural choices land much more cleanly.

A second concrete factual issue: the chapter mentions Intel Loihi without specifying whether this refers to **Loihi 1** or **Loihi 2**. The energy figures and per-SOP costs differ substantially between the two generations; Loihi 2 numbers are the current reference and should be explicit. This is the kind of precision a thorough examiner notices.

A handful of structural gaps are also present: §2.3.6 (Temporal Dynamics) ends mid-thought without the TTFS / Rate-Order Coding sentences that appear later in §4.2.2 as future work; spatiotemporal voxelisation is referenced repeatedly in §3.3 without an explicit Background introduction; SEWResBlock is introduced for the first time in §3.4 with no Background anchor.

### Strengths

- Comprehensive coverage of the seven topic areas with appropriate citations.
- §2.6 (neuromorphic hardware energy economics) is precise and well-grounded.
- §2.7 (related work) correctly identifies the closest competitors and articulates the gap.
- LIF dynamics equations are properly presented with parameter labelling.

### Areas for Improvement (priority order)

1. **Add diagrams.** This is the single most impactful change. The supervisor explicitly lists candidates: CNNs, residual connections, surrogate gradients, event-based vision, ETraM extracts. Even a small subset (e.g. four diagrams) would shift this section from Expected to comfortably Above Expectations.
2. **Disambiguate "Loihi"** — specify Loihi 1 or Loihi 2, with the latter being the current reference for any quoted numbers.
3. **Restore voxelisation background** in §2.4 with a brief subsection introducing the 4D `[T, C, H, W]` tensor before the reader meets it in §3.3.
4. **Anchor SEWResBlock at the Background level** — even one paragraph explaining the problem SEW solves (non-binary residual sums in spiking networks) before the §3.4 implementation.
5. **Complete §2.3.6** (Temporal Dynamics) with the missing TTFS / ROC sentences.

### Path to Outstanding (90+)

The Outstanding band requires: *"a precise and exhaustive description of the project's setting firmly based on peer-reviewed literature"* and *"an excellent understanding of the content and relevance of the included literature"*.

To reach Outstanding, the chapter would need (in addition to the supervisor priorities above):

1. **A diagram per major concept** rather than just four to six. Outstanding rarely has a text-only paragraph for a concept the reader needs to grasp visually. Aim for ~8–12 diagrams across the chapter: CNN block, residual connection, surrogate gradient, event-stream vs. frame-based, ETraM sample with annotations, voxel-grid construction, SEWResBlock vs. standard ResBlock, LIF dynamics over time, FRR penalty curve, MAC vs. AC operation diagram, neuromorphic chip topology (Loihi 2), and the field landscape (where DetectorNX sits among published SNN detectors).
2. **Explicit relevance-articulation per cited work.** Currently most citations are factual ("X did Y"). Outstanding requires *"excellent understanding of the content and relevance of the included literature"* — each major cited work should have a sentence or clause linking it to a specific design or evaluation choice in DetectorNX. E.g. *"Fang et al.'s SEW residuals (2022) directly motivate the §3.4 backbone choice — without it, the binary-spike chain at Stage 3 would saturate."*
3. **Bibliography metadata audit.** Verify publication years, venues, and citation keys across every entry. Outstanding examiners notice metadata errors.
4. **Background-section coverage gaps closed entirely** — no reader should encounter a core concept (voxelisation, SEW, multi-box detection head, GIoU loss) for the first time outside Chapter 2.
5. **Possibly a "Background Synthesis" closing subsection** that explicitly states what the reader should now believe before reading Chapter 3, summarising the literature-grounded position of the project.

---

## Section 3.3 — Technical Quality, Methodology & Evaluation (75/100, weighted 26.25/35)

### Justification

This is the strongest chapter in the report and the supervisor's positive comments target it directly: "good description of experimental setup and presentation of findings, together with critical analysis." That assessment is correct. The variable-isolation experimental design (fixed BOLT preprocessing, fixed regression head, interchangeable backbone) is enforced consistently. The traceability table mapping each success criterion to an architectural mechanism and a validating experiment (§3.2 Table 1) is methodologically sophisticated and rare at BSc level. The BOLT pipeline is documented to production-quality detail (box-central sampling, density filter, voxelisation, normalisation, multi-object label alignment, LRU-cached chunked I/O). Each architectural decision in §3.4 is motivated by a specific failure mode encountered during development. The four-generation evolution narrative (Phase 0 → G1 → G2 → G3) shows genuine engineering rigour with explicit failure-mode documentation.

The evaluation suite is genuinely multidimensional: spatial accuracy (global evaluator), energy consumption (dynamic power, theoretical energy, comparative landscape), real-time viability (latency), object-size dependence (quantisation error), confidence reliability (calibration), and temporal evidence accumulation. Each experiment is structured as hypothesis → setup → results → critical analysis. The mathematical validation of the energy figures to ±0.01% demonstrates internal consistency. The reactive scalability framing (R² = 0.7514, with the y-intercept interpreted as resting metabolic cost and the slope as per-event marginal cost) is a genuine and well-articulated insight.

**However**, the supervisor flagged a specific gap that I agree with: the **G1 / G2 / G3 architectural progression is described in the methods chapter (§3.6) but is not validated with comparative results in the results chapter**. The current report tells the reader that G1 had ghost detections, G2 had a mIoU plateau at 41%, and G3 broke through to 46% — but the reader is asked to take this on the author's word. A small comparative table or chart in the results section showing G1 / G2 / G3 mIoU, parameter count, and selected metrics would make the architectural progression an evidence-based decision rather than an asserted narrative. This is the kind of evidence the supervisor explicitly expected to see and didn't.

A secondary structural issue: the **results currently sit inside Chapter 3 (§3.8) rather than being separated into their own chapter**. The supervisor recommended a "4.0 Results and Evaluation" chapter structure to make the project outputs distinct from the methods. This would not affect the rubric score directly but would improve the structural clarity of the report.

A few lower-priority issues persist from the methodology pass: the "Loihi" version disambiguation flagged in §3.2 also affects the §3.8 hardware extrapolation table (which currently quotes a per-SOP energy figure of 23.6 pJ — confirm whether this is the Loihi 1 or Loihi 2 number); the §3.7 introduction states "five distinct experimental protocols" but seven experiments are listed; the §3.8/temporal.tex todo "Fix Inconsistencies and rewrite prose" remains unaddressed and the figure reference duplication in that file (both "Hunting Behaviour" and "High-confidence early detection" cite the same `fig:temp_seq_2`) is a real error that will appear in the compiled PDF.

### Strengths

- Variable-isolation principle is enforced and explicitly stated.
- BOLT pipeline is documented to a production-engineering standard.
- Architectural evolution shows what failed and why, generation by generation.
- Mathematical validation of energy claims (±0.01% internal consistency) demonstrates rigour.
- Reactive scalability regression analysis is a novel and well-grounded interpretation.
- Comparative efficiency landscape (Table in §3.8) is methodologically honest about its dataset and task confounds.
- Four-generation parameter trajectory (5.43M → 7.00M → 11.72M) shows iterative development.

### Areas for Improvement

1. **Add G1/G2/G3 comparative results to the results chapter.** A small table showing mIoU, parameter count, and one or two selected metrics across the three generations would convert the architectural decision narrative from "asserted" to "evidence-based." Supervisor explicitly requested this.
2. **Move §3.8 into its own chapter (Chapter 4 or 5: Results and Evaluation).** Restructures the report so methods and results are visually distinct, helping a reader (and a marker) navigate. Supervisor explicitly recommended this.
3. **Disambiguate Loihi version** in the energy extrapolation section, and quote Loihi 2 numbers for currency.
4. **Resolve the §3.7 "five protocols" / seven-experiments inconsistency.**
5. **Fix the temporal.tex figure reference duplication** and rewrite the prose flagged by the existing todo.
6. **Verify the Horowitz CMOS reference** flagged by the existing todo in §3.8/theoretical_energy.tex.

### Path to Outstanding (90+)

The Outstanding band requires (cumulative across previous bands): *"the designs are very well considered, clear, and easy to understand"* + *"the output has been evaluated to a very high level (testing, questionnaires, comparison with similar work)"* + *"the student demonstrates a very thorough understanding of the technical details"* + *"there is very little to fault"* + *"the writing demonstrates an extremely thorough understanding of the project work and the field in which it sits"* + *"explanations of the technical details, work of the project and evaluation are exceptional"*.

To reach Outstanding (in addition to the supervisor priorities above):

1. **Ablation study** for at least one major architectural decision. Currently each design choice is justified by reference to a failure mode. An ablation (e.g. "with vs. without SE block at Stage 3", "with vs. without FRR", "T = 4 vs. T = 10 vs. T = 20") would convert design *justifications* into *empirical demonstrations*. Even one ablation experiment elevates the technical-quality assessment substantially.
2. **A T-sweep experiment** for the quantisation-error analysis. The current claim that 1-bit quantisation imposes a global ceiling is consistent with theory but not isolated empirically. Running the same architecture at T ∈ {4, 10, 20} and showing how mIoU degrades would directly validate the 1/T theoretical prediction and convert "consistent with" into "demonstrated by".
3. **Hardware-realisation cross-check.** Real GPU power-meter measurements (e.g. via `nvidia-smi`) alongside the theoretical Horowitz-derived figures would close the loop on SC2's "realised on GPU hardware" requirement and make the energy claim hardware-validated rather than purely theoretical.
4. **Statistical significance.** Variance across multiple training runs (e.g. 3–5 seeds) for the headline metrics would replace point estimates with means + standard deviations. Outstanding evaluations report distributions, not single numbers.
5. **All currently flagged technical-quality nits resolved** — including the Horowitz reference, the figure-reference duplication, the protocol-count inconsistency, and any existing todos.

These additions are substantial undertakings — items 1–4 are essentially small additional experiments — but they are exactly what distinguishes Outstanding (90+) from Excellent (80–89) at this rubric level.

---

## Section 3.4 — Summary & Conclusions (75/100, weighted 11.25/15)

### Justification

Chapter 4 is well-structured. The Outcomes section walks through Global Precision Parity, Decisive Efficiency Gains (now with the comparative landscape callback), Temporal Reliability and Sharpening, Real-Time Viability, and a Success Criteria Validation table that closes the loop on every criterion stated in the introduction. The Critical Reflection section identifies four substantive limitations (LIF simulation penalty, temporal quantisation ceiling, detection head mismatch, dataset domain gap) with specificity rather than vagueness, and each limitation is paired with concrete future-work directions (Loihi deployment, adaptive timestepping/TTFS/ROC, SNN-native head, GEN1 + CARLA closed-loop). The honesty about the GPU-mismatch penalty (5.4× throughput gap explicitly named) and the methodological-constraint framing of the shared detection head ("deliberate, not an oversight") are both intellectually mature.

The closing summary establishes the spiking paradigm as "a robust, first-class solution for high-definition, power-constrained automotive perception," supported by the SC validation table directly above it.

A handful of refinements remain:

- The Bounding Box Sharpening finding in §4.1.3 is partly undermined by the "Hunting Behaviour" observed in dense scenes (visible in §3.8/temporal.tex). A more balanced treatment that acknowledges both modes would be more scientifically honest.
- The Real-Time Viability section claims "validates immediate viability for live deployment in V2X and ADAS systems" but the latency was measured on a cloud-class A100 GPU, not on automotive edge silicon. Qualifying "on GPU hardware" would be more precise.
- The CARLA future-work item is well-motivated but lacks a falsifiable success criterion (e.g. specific reduction in emergency braking distance) that would make the future experiment more testable.

### Strengths

- SC validation table closes the loop on every criterion from Chapter 1.
- Four limitations are substantive and individually actionable.
- Future-work directions are technically specific (Loihi, TTFS, ROC, CARLA) rather than vague.
- Honest about hardware-mismatch penalties and dataset choice trade-offs.
- The detection-head-mismatch framing as "deliberate methodological constraint" is mature.

### Areas for Improvement

- Acknowledge "Hunting Behaviour" alongside "Bounding Box Sharpening" for balanced treatment.
- Qualify "immediate viability" with the GPU-hardware caveat.
- Tighten the CARLA future-work item with a specific testable success metric (e.g. "reduce emergency braking distance by X% under conditions Y").

### Path to Outstanding (90+)

The Outstanding band requires: *"the summary and conclusions are excellent in precision and coverage. It is clear that the student has mastered the material and has given a definitive set of conclusions and a well thought-through plan for future work to reach definitive conclusions."*

To reach Outstanding:

1. **A definitive overall conclusion sentence.** Currently the closing summary is good but slightly incremental ("first-class solution for high-definition, power-constrained automotive perception"). Outstanding wants *one* crystallised conclusion of the project that crystallises everything. E.g. *"The variable-isolated comparison demonstrates that the spiking paradigm imposes a measurable but architecturally tractable precision cost (~5% mIoU) in exchange for an order-of-magnitude reduction in energy demand on automotive-grade event detection — establishing it as a viable, not merely theoretical, route to safety-critical edge perception."*
2. **Each future-work item with a falsifiable success metric.** The four current limitations have future-work directions, but Outstanding wants those directions framed so a future researcher could *know whether they succeeded*. E.g. for CARLA: *"reduce simulated emergency braking distance by ≥ 5% at the 95% confidence level vs the dense-CNN baseline under the standard CARLA Town01 stress scenarios"*.
3. **A "what could not be concluded" section.** Outstanding conclusions acknowledge the limits of what the present evidence supports. E.g. *"The variable-isolated cost measurement of ~5% mIoU is specific to ETraM single-class detection at T=10; it cannot be assumed to generalise to multi-class detection or to lower temporal resolutions, both of which require dedicated experiments."*
4. **Tight balance on each contribution.** Acknowledge "Bounding Box Sharpening" *and* "Hunting Behaviour" as twin temporal-integration phenomena (one helpful, one problematic). Outstanding-band conclusions own the trade-offs.
5. **A forward-looking "what would convince a sceptic" closing.** What experiment, if it succeeded, would establish the spiking paradigm as the dominant approach for automotive perception? Naming that experiment shows mastery beyond the present work.

---

## Section 3.5 — Presentation, Structure & Language (62/100, weighted 6.2/10)

### Justification

**This is the section most affected by the supervisor's critique.** The score reflects two structural concerns plus several language-level issues.

**Structural concern 1 — diagram absence.** The Background chapter is text-only; this is the single most consequential presentation issue in the report. The Expected band (60–69) of the rubric specifies "the writing is supplemented by an appropriate amount of figures and tables, and they are easily interpreted, with reasonable captions" — without diagrams in the chapter that most needs them, this criterion is met partially at best. The methodology and results chapters do contain figures (constant-target-bias examples, dynamic power plots, calibration reliability diagrams, the high-level architecture diagram), so the report is not entirely figure-less, but the imbalance between dense Background prose and figure-supported later chapters is striking.

**Structural concern 2 — results merged with methods.** The supervisor recommended separating results into their own chapter (e.g. "4.0 Results and Evaluation") to make project outputs visually distinct from the methodology. Currently §3.8 (Results & Evaluation) sits inside Chapter 3, which structurally blurs methods and findings. This affects how the reader navigates and how cleanly the achievements are presented. It is also unusual for a BSc dissertation of this scope to fold results inside the methodology chapter rather than separating them.

**Language and minor issues:**

- Lingering minor typographical issues (whilst many have been addressed in recent passes, a final proofread would catch any remaining ones).
- Some over-reliance on intensifying adverbs ("drastically", "definitively", "conclusive") — academic tone is better served by letting the numbers speak.
- §3.7 says "five distinct experimental protocols" but seven are listed.
- The temporal evidence section has a figure-reference duplication that will appear in the compiled PDF.
- The `\listoftodos` command in `report.tex` is harmless given the `disable` flag on `todonotes`, but produces an empty list that should be commented out for final submission.

**Positive presentation aspects:**

- Glossary and List of Abbreviations consistently used (`\gls{}` macros throughout).
- Bibliography is consistently formatted (numeric BibLaTeX style).
- Appendix hyperparameter tables are detailed and complete.
- Tables and figures (where present) have short titles for the list of figures.
- All `\todo` notes are correctly suppressed via the `[disable]` flag.
- The recent reorganisation of the appendix and the conversion of the hyperparameter table to `longtable` (where applied) handle multi-page tables cleanly.
- Word count after the recent compression pass is in a sensible range relative to the rubric's 10,000–15,000 target band.

### Strengths

- Consistent use of named model variants throughout (`DetectorNX-G3-SNN`, `SEWResBlock`, etc.).
- Glossary integration is thorough.
- Figures that are present are well-captioned.
- Overall narrative arc (Introduction → Background → Methodology → Results → Conclusions) is logical.

### Areas for Improvement (priority order)

1. **Add diagrams to the Background chapter** (the single highest-impact presentation fix).
2. **Restructure results into their own chapter** (e.g. Chapter 4: Results and Evaluation, with the existing Chapter 4 becoming Chapter 5).
3. **Final proofreading pass** for any remaining minor punctuation or typographical issues.
4. **Resolve the §3.7 "five protocols" wording** to match the actual count of seven experiments.
5. **Reduce intensifying adverbs** ("drastically", "definitively", "conclusive") in favour of qualified quantitative statements.

### Path to Outstanding (90+)

The Outstanding band requires: *"there is very little to fault. A broad vocabulary and a thorough understanding of the English language is evident. Beautifully presented."*

To reach Outstanding:

1. **Beautifully presented** is a high typographic bar. Concretely:
   - Word count comfortably inside the 10,000–15,000 target band (currently right at the upper edge after compression).
   - Every figure has a short title for the list of figures, a `\centering`, sensible placement, and a caption that interprets the figure rather than just describing it.
   - Tables use consistent spacing, proper booktabs-style rules where applicable, and right-aligned numerics.
   - All cross-references resolve (no `??`).
   - No widow/orphan lines, no awkward column breaks, no overlapping floats.
2. **Diagrams everywhere they earn their place.** Outstanding presentations don't have a text-only chapter. Every chapter should have at least one figure that genuinely helps the reader.
3. **A clean structural arc.** Five chapters: Introduction, Background, Methodology, Results, Conclusions. Currently methodology + results are merged in Chapter 3 — separating them is the supervisor's recommendation and a presentational requirement at this band.
4. **Zero remaining typographical issues.** Outstanding examiners notice every "as supposed to" / "more honest regarding ambiguous features., and" / paragraph starting with lowercase letter. A final proofread (ideally by a peer) is a non-negotiable.
5. **Consistent terminology.** Every named concept (DetectorNX-G3-SNN, BOLT, SEWResBlock, FRR, etc.) used identically every time it appears. No instances of switching between "SNN", "spiking neural network", or "spiking model" in the same paragraph without a deliberate stylistic reason.
6. **Glossary and abbreviations completeness.** Every acronym defined on first use and reusable via `\gls{}`. Glossary list rendered without page numbers (already done via `nonumberlist`). All abbreviations consistently spelled.
7. **Mathematics typesetting at a high standard.** Equations centred and numbered, variables consistently italicised, units in upright Roman, vectors bold, etc.

The bar is very high. Outstanding (90+) at this rubric level effectively means a published-quality manuscript. Realistically, hitting low-to-mid 80s here is the sensible target for a BSc dissertation.

---

## Overall Observations

**What the supervisor saw and what this evaluation mirrors:**

This is a project with strong methodological substance and good experimental presentation, but with a specific and addressable presentation gap (diagram absence in Background) and a structural recommendation (results as their own chapter). The technical work is genuinely good — the variable-isolation framing, the four-generation evolution, the multidimensional evaluation, the energy mathematical validation, and the SC traceability are all First-class elements. The critical reflection chapter is mature.

**The four most consequential improvements before final submission, in priority order:**

1. **Diagrams in Background** (supervisor's top critique). Even four to six well-chosen diagrams (CNN/residual block; surrogate gradient curve; event-stream vs frame; ETraM sample frame; SEWResBlock; spike train timing) would shift §3.2 and §3.5 substantially upward.
2. **G1/G2/G3 comparative results** in the (newly separated) Results chapter, demonstrating the architectural progression as evidence-based.
3. **Results as a distinct chapter**, separating findings from methodology.
4. **Loihi version specificity** — confirm Loihi 2 and update any quoted per-SOP figures.

**Lower-priority cleanup items:**

5. Resolve §3.7 "five protocols / seven experiments" inconsistency.
6. Fix the temporal.tex figure-reference duplication.
7. Verify the Horowitz CMOS reference per the existing todo.
8. Final language proofread.

If items 1–4 are addressed, the projected band moves from upper Above Expectations / boundary First into a comfortable First. The substance is already there; the presentation refinements would let it land properly.

---

## Cross-Cutting Path to Outstanding (90+)

The supervisor priorities push the report from current ~72 to a comfortable First (~78–82). Pushing further into Outstanding (90+) is a different and higher bar that involves substantive additions, not just refinements. A realistic Outstanding-tier roadmap, prioritised by impact-per-effort:

**High impact, moderate effort:**

1. **Add diagrams to the Background chapter** (also addresses supervisor priority). 8–12 diagrams across §2.2–§2.7 covering: CNN block / residual connection / surrogate gradient / event-stream vs frame / ETraM sample / voxel construction / SEWResBlock / LIF dynamics / FRR penalty curve / MAC vs AC / Loihi 2 topology / SNN-detector landscape. Lifts §3.2 and §3.5 simultaneously.
2. **Separate results into their own chapter** (also addresses supervisor priority). Restructures the report from 4 chapters to 5. Lifts §3.5.
3. **Add G1/G2/G3 comparative results table** in the new results chapter (also addresses supervisor priority). One table converts asserted architectural progression into evidence-based decision. Lifts §3.3.
4. **Loihi version disambiguation** (also addresses supervisor priority). Quick factual fix; Loihi 2 numbers throughout. Lifts §3.2 and §3.3.

**High impact, high effort:**

5. **One ablation experiment** (e.g. with vs. without SE block at Stage 3, or with vs. without FRR penalty). Converts a design justification into an empirical demonstration. Pushes §3.3 into Outstanding territory.
6. **One T-sweep experiment** for the quantisation-error analysis (T = 4, 10, 20). Validates the 1/T theoretical prediction empirically and converts the falsification finding from "consistent with" into "demonstrated by". Pushes §3.3 into Outstanding territory.
7. **Multi-seed variance reporting** for the headline metrics. 3–5 training seeds, report mean ± std deviation. Replaces point estimates with distributions. Pushes §3.3 from "Excellent" to "Outstanding".

**Moderate impact, low effort:**

8. **Literature-derive the success criteria** in Chapter 1. Each SC needs a sentence linking it to prior work. Lifts §3.1.
9. **Articulate relevance per cited work** in Background. Each major citation tied to a specific DetectorNX choice. Lifts §3.2.
10. **A definitive overall conclusion sentence** in Chapter 4 closer. One crystallised takeaway. Lifts §3.4.
11. **Falsifiable success metrics for each future-work item.** What would success look like quantitatively? Lifts §3.4.
12. **Final proofread pass** for typography, intensifiers, and remaining minor errors. Lifts §3.5.

**Realistic target:**

For a BSc dissertation, hitting low-to-mid 80s overall is genuinely strong and reflects a publishable-quality contribution. Hitting 90+ requires either a substantively novel result (which this project arguably has — the variable-isolated comparison protocol + scale-stable quantisation finding + implicit-uncertainty-sensor finding) AND publication-quality presentation. The substance is there; items 1–7 above would close most of the gap.

**Effort budget for "comfortable First" (78–82) vs. "Outstanding" (90+):**

- The four supervisor-priority items (diagrams, results restructure, G1/G2/G3 table, Loihi version) ≈ 2–4 days of focused work. Lifts to comfortable First.
- Adding any one of the empirical extensions (ablation, T-sweep, multi-seed) ≈ 1–2 weeks each. Each one moves a section closer to Outstanding.
- Full Outstanding-tier polish (all literature derivations, full bibliography audit, comprehensive diagram set, multi-seed variance, ablations, T-sweep, beautiful typesetting, final proofread) ≈ 4–6 weeks of full-time work.

If submission is imminent, items 1–4 are the right focus. If you have several more weeks available and want to push for Outstanding, items 5–7 are where the marginal effort buys the most.

---

*Evaluation performed by Claude (claude-opus-4-7) and intentionally calibrated to the supervisor's feedback recorded in `supervisor_notes.md`. The marking emphasises the same concerns the supervisor raised (diagram absence, results-vs-methods structural distinction, G1/G2/G3 progression evidence, Loihi version specificity) so that the projected band and concrete improvement priorities better reflect what a real second marker who has access to the supervisor's input would conclude. The "Path to Outstanding" subsections per rubric area, plus the cross-cutting roadmap, identify what would be needed to push each section toward 90+ — separately from what the supervisor's feedback prioritises in the immediate term. No `.tex` files were edited during this evaluation.*
