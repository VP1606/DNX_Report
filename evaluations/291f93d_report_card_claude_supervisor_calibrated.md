---
Hash: 291f93d
Branch: draft2
Date: Sun May 03 2026
Time: (re-evaluation following supervisor-priority work)
Evaluator: Claude (claude-opus-4-7) — calibrated to supervisor feedback in `supervisor_notes.md`
---

# DetectorNX — Report Card (Supervisor-Calibrated)

**Report Title:** DetectorNX — Evaluating Spiking Neural Networks for High-Definition Automotive Perception
**Degree Programme:** BSc Computer Science (COMP30040)
**Supervisor:** Dr Oliver Rhodes
**Rubric Source:** `guides/project_assessment.pdf`
**Calibration Note:** Same calibration approach as the previous report card (`cc59984_report_card_claude_supervisor_calibrated.md`). The marking weights the same supervisor-flagged concerns in proportion to how a real second marker reading the current draft would respond. **Crucially, this evaluation re-reads every `.tex` file from scratch; it does not rely on any prior summary.**

---

## Score Summary

| Rubric Section | Weight | Raw | Weighted |
|---|---|---|---|
| 3.1 Abstract & Introduction | 15% | 78 | 11.7 / 15 |
| 3.2 Background & Theory | 25% | 75 | 18.75 / 25 |
| 3.3 Technical Quality, Methodology & Evaluation | 35% | 80 | 28.0 / 35 |
| 3.4 Summary & Conclusions | 15% | 76 | 11.4 / 15 |
| 3.5 Presentation, Structure & Language | 10% | 75 | 7.5 / 10 |
| **Overall** | 100% | — | **~77 / 100** |

**Projected band:** Comfortable First Class (lower-mid band).
**Delta vs previous evaluation (`cc59984`, 30-Apr-2026):** **+5 marks** (72 → 77), driven primarily by closure of the four supervisor-flagged priorities.

---

## Headline (mirroring supervisor's tone)

The four supervisor priorities have substantially landed. Six background-chapter diagrams are now present (CNN feature hierarchy, residual block, LIF dynamics, surrogate gradient, frame-vs-event, ETraM samples) — the chapter is no longer text-only and reads as a competent treatment of the prerequisite theory. Results have been separated into their own chapter (`chapter_4R`) with the supervisor-requested G1/G2/G3 architectural-progression evidence sitting *first* in that chapter as a dedicated table-plus-chart section that explicitly justifies the G3 selection as evidence-based. Loihi has been disambiguated to Loihi 2 throughout, and the Loihi 2 per-SOP figure (16.1 pJ) propagates correctly through the energy table and the SC2 outcomes row.

What remains is mostly polish and a couple of closeable structural items. **Two background sections (§2.6 Neuromorphic Hardware and §2.7 Related Work) remain text-only**, so the diagram coverage is ~75% rather than 100%. **The §1.6 Report Structure paragraph is now factually wrong** — it still claims methods and evaluation are integrated in a single chapter, but the recent restructure has split them. A handful of small SPaG / typographic items also persist.

This is now a comfortable First. With ~1 day of additional polish (the two missing background figures, the report-structure paragraph, the SPaG list below) the report would be near the upper end of First (low 80s).

---

## Section 3.1 — Abstract & Introduction (78/100, weighted 11.7/15)

### Justification

Largely unchanged in substance from the previous evaluation; the score therefore stays at 78. The abstract still delivers a tight problem framing, names the project, states the research question, and reports six concrete numerical outcomes (94.9% mIoU parity, 91.3% mAP\textsubscript{50} parity, 100% recall, 94.33% energy saving, 259.80 FPS, superior low-confidence calibration). The novelty claim is still appropriately hedged. The four-paragraph structure remains conventional and easy to follow.

The introduction (Chapter 1) retains the well-judged structure: regulatory motivation grounded in Euro NCAP 2026 protocols (now with the *"Europe's vehicle safety rating programme"* clarifier in place), CPU→GPU technical-squeeze framing via Lin, six quantitative success criteria, and the chapter-by-chapter map. The traceability between SC1–SC6 and validating experiments is intact via Table 3.1.

The aims/objectives now correctly reference *"Intel Loihi 2"* (Objective 5), reflecting the Loihi-version disambiguation flagged in the previous review.

### Strengths

- Six quantitative success criteria with traceability through the report.
- Abstract foregrounds the falsification finding (scale-stable quantisation ceiling), demonstrating engagement with results rather than pure positives.
- Introduction's CPU→GPU trajectory framing is a defensible forward-looking argument grounded in Lin's actual claims.
- The introduction now explicitly positions DetectorNX against three published competitors (SpikeDet, SpikeYOLO, EMS-YOLO) in §1.1 — partially closing one of the previous "Areas for Improvement".

### Areas for Improvement

- **§1.6 Report Structure is factually out of date.** It still says *"By integrating the architectural design (DetectorNX-G3-SNN and DetectorNX-G3-CNN) with the experimental setup and evaluation within a single chapter, the report directly links architectural choices…"* — but the report has since been restructured so methods (Chapter 3) and results (Chapter 4) are now distinct. The whole *Methodology and Evaluation* paragraph needs splitting into a *Methodology* paragraph (Ch3) and an *Evaluation/Results* paragraph (Ch4) plus a *Conclusions* paragraph (Ch5). This is a real factual inconsistency that a careful examiner will spot.
- The "Why 90% mIoU?" question for SC1 is still not addressed — the threshold appears chosen by convention rather than justified by reference to prior SNN work. The prose mentions Iaboni et al. 2024 generally, but doesn't tie the 90% figure to a specific cited convention.
- Aim 4 ("Benchmark inference latency on GPU hardware") is met, but the introduction does not yet acknowledge that GPU latency is a *known-unfair* benchmark for SNNs (the conclusion does flag this, but the introduction sets expectations from the start). One half-sentence in §1.2 acknowledging this would honest-frame the latency result.

### Path to Outstanding (90+)

The Outstanding band for this rubric area requires: *"a precise and comprehensive overview of the project's achievements in its proper context"* (abstract) + *"a comprehensive and precise account of the project's setting firmly based on peer-reviewed literature and derives an evaluation strategy derived from such literature"* (introduction).

To reach Outstanding, the report would need:

1. **Literature-derived evaluation strategy.** Currently the six success criteria are stated as project-internal goals. Outstanding wants them visibly *derived from* prior work — e.g. *"SC1 (≥ 90% mIoU parity) follows the convention established by [SpikeDet, SpikeYOLO] for evaluating spiking detectors against continuous baselines."* Each criterion should have a literature-anchored justification.
2. **Tighter positioning vs competitors.** §1.1 now mentions SpikeDet/SpikeYOLO/EMS-YOLO. Outstanding-band introductions go further: *what does DetectorNX add that none of these do?* Currently the answer is buried in the abstract; surface it in §1.1 explicitly.
3. **Fix the §1.6 inconsistency** as a precondition (this is a must-fix for the current band, not just for Outstanding).
4. **Add a single visual** in the introduction (a high-level project-architecture teaser, or a regulatory-trajectory chart). Outstanding presentations rarely have a text-only introduction.

---

## Section 3.2 — Background & Theory (75/100, weighted 18.75/25)

### Justification

**This section has improved substantially since the previous evaluation (was 65, now 75) — the supervisor's diagram critique has been largely addressed.** Six new figures are now present in the background chapter:

- §2.2 *Convolutional Networks*: hierarchical feature visualisation (LeCun) + standard residual block (He et al.)
- §2.3 *Spiking Neural Networks*: LIF dynamics diagram + surrogate gradient (forward Heaviside vs backward atan family)
- §2.4 *Event-Based Vision*: frame-vs-event same-scene comparison (Gallego)
- §2.5 *ETraM Dataset*: Verma et al. sample frames

Each figure is properly cited (*"Reproduced from \cite{...}"*, *"Adapted from \cite{...}"*) and is positioned adjacent to the prose that explains the concept. Captions are descriptive rather than purely titular. The choice of figures matches the supervisor's explicit suggestions almost one-for-one (CNNs ✓, residual connections ✓, surrogate gradients ✓, event-based vision ✓, ETraM extracts ✓).

The Loihi version disambiguation has also been completed: §2.6 now correctly identifies *"Intel Loihi 2"* with the per-SOP figure of 16.1 pJ (citing Gralewicz et al. 2024) alongside IBM TrueNorth at 26.0 pJ. The per-SOP cost propagates correctly through the energy modelling chain.

**However, two sections still lack figures and represent the remaining ~25% of the diagram-coverage gap:**

- **§2.6 Neuromorphic Hardware** — no figure. A simple side-by-side schematic (synchronous GPU computation vs asynchronous neuromorphic) or a Loihi 2 die/architecture diagram would land here.
- **§2.7 Related Work** — no figure. A 2D landscape scatter (year × resolution, with surveyed competitors as points and DetectorNX marked distinctly) would do double-duty as both a literature-positioning visual and a §3.1 framing aid.

These two missing diagrams are the binding constraint preventing this section from reaching the upper-First band (~80+).

The chapter's other persistent issues from the previous review have been **partially** addressed: the SEW vs standard ResBlock contrast is now explained in the body text (though still not anchored at the Background level — first encounter is still in §3.4); the temporal-dynamics treatment in §2.3.6 reads more completely. Voxelisation is still introduced for the first time in §3.3 rather than §2.4.

### Strengths

- Six new diagrams covering the supervisor's named topics, each with appropriate citation.
- Loihi 2 disambiguation done cleanly — both Loihi 1 (23.6 pJ) and Loihi 2 (16.1 pJ) appear in the energy-constants table with proper citations, and the prose consistently uses *"Loihi 2"* as the current reference.
- §2.6 (neuromorphic hardware energy economics) and §2.7 (related work) remain individually strong textually — the energy economics treatment (Horowitz constants, MAC vs AC asymmetry) and the gap-statement narrative for SNN object detection are at First-class level.
- All major citations are appropriate and contemporary; no obvious metadata errors spotted.

### Areas for Improvement

1. **Add a §2.6 figure** (synchronous GPU vs asynchronous neuromorphic, or Loihi 2 architecture). This is the highest-impact single addition for this section.
2. **Add a §2.7 figure** (SNN-detector landscape scatter — year × resolution with comparators + DetectorNX marked). This also doubles as evidence for the gap-claim.
3. **Anchor SEWResBlock at Background level** — the §3.4 implementation discusses it well, but a Background-level paragraph in §2.2 or §2.3 would mean a reader meets the concept before seeing the implementation.
4. **Voxelisation introduction in §2.4** — currently the reader meets *"4D `[T, C, H, W]` tensor"* for the first time in §3.3. A short subsection in §2.4 anchoring spatiotemporal voxelisation conceptually would close the last Background-coverage gap.
5. **Bibliography alphabetical sort** (per supervisor sub-item) — verify this has been applied; the *"sorting=nty"* in the biblatex preamble suggests yes, but worth a visual check on the rendered references list.

### Path to Outstanding (90+)

To reach Outstanding (in addition to closing the items above):

1. **A diagram per major concept** rather than just six. Aim for ~8–12 across the chapter: the existing six plus a §2.6 GPU-vs-neuromorphic schematic, §2.7 landscape scatter, possibly a voxel-grid construction visualisation in §2.4, an FRR penalty curve in §2.3, and a Loihi 2 chip-topology diagram.
2. **Explicit relevance-articulation per cited work.** Currently most citations are factual ("X did Y"). Outstanding requires *"excellent understanding of the content and relevance of the included literature"* — each major cited work should have a sentence or clause linking it to a specific DetectorNX choice. E.g. *"Fang et al.'s SEW residuals (2022) directly motivate the §3.4 backbone choice — without it, the binary-spike chain at Stage 3 would saturate."*
3. **Bibliography metadata audit.** Verify publication years, venues, and citation keys across every entry. Outstanding examiners notice metadata errors. (One specific item: `davies2018loihi` is still cited in §3.7/latency.tex for a latency-benchmark claim — Loihi 2 may have updated latency figures worth substituting.)
4. **Background-section coverage gaps closed entirely** — no reader should encounter a core concept (voxelisation, SEW, multi-box detection head, GIoU loss) for the first time outside Chapter 2.
5. **A "Background Synthesis" closing subsection** that explicitly states what the reader should now believe before reading Chapter 3, summarising the literature-grounded position of the project.

---

## Section 3.3 — Technical Quality, Methodology & Evaluation (80/100, weighted 28.0/35)

### Justification

This section has lifted from 75 to 80, driven primarily by the closure of supervisor priority #3: G1/G2/G3 architectural progression is now visible *as evidence-based decision* in the Results chapter. Specifically, `chapter_4R/arch_progression.tex` is now positioned as the very first Results section (placed before the global evaluator), and contains:

- A four-row comparative table (G0/G1/G2/G3) with Params and Validation mIoU columns. mIoU is now consistently presented across all four generations (1.37%‡, 20.4%, 41.1%, 46.1%) — the only metric instrumented across the full progression. The G0 row carries a `‡` footnote explaining the protocol asymmetry (separately-created test set vs the stratified validation subset used elsewhere).
- A bar chart visualising the mIoU trajectory, with single-box (G0/G1) vs multi-box (G2/G3) family colour-coding and explicit family-bracket annotations.
- Cross-references both ways with §3.6 (Methods → Results and Results → Methods), explicitly inverting the flow so a reader who skips to Results sees the evidence base *first*, then can drill into Methods for the engineering rationale.
- An honest framing: *"Validation mIoU serves as the primary cross-generation metric, since it is the only quantitative measure collected across all four generations."* Additional generation-specific evidence (firing rates, ADP, qualitative failure modes) is acknowledged with cross-references.
- The closing sentence explicitly justifies G3 as *"the canonical \texttt{DetectorNX-G3-SNN} architecture"* — this is the evidence-based justification the supervisor was asking for.

The §3.6 Architectural Evolution section in the methods chapter has also been comprehensively restructured into a standardised four-step format (Architectural Intent → Empirical Result → Diagnostic Analysis → Actionable Insight and Iteration) for each of G0–G3. The G0 generation now has its own subsection (previously *"Phase 0"*) with the existing Constant Target Bias figure; G1 has a new Super-Box failure figure; G2's Information Congestion and G3's metabolic-recovery analyses are clearly framed. The closing summary table includes the mIoU column and the dagger-footnote on G0.

The §3.7 introduction now correctly states *"seven distinct experimental protocols"* matching the actual count (the prior *"five protocols"* inconsistency is fixed). The energy-constants table in §3.7/energy_consumption.tex now correctly contains both Loihi 1 and Loihi 2 rows; the Loihi 2 figure (16.1 pJ) propagates through the §4.4 theoretical-energy table to give the 76.21% saving on Loihi 2 (vs 65.12% on Loihi 1 in the previous draft) — Loihi 2 is now the *current reference figure* the supervisor requested.

The pre-existing strengths remain intact: variable-isolation principle enforced; BOLT pipeline documented to production-engineering standard; mathematical validation of energy claims to ±0.01% internal consistency; reactive scalability regression analysis (R² = 0.7514); and the four-generation parameter trajectory (5.43M → 7.00M → 11.72M).

### Strengths

- **Supervisor priority #3 fully closed.** Architectural progression now visible as evidence-based decision in the Results chapter, with bidirectional cross-references to the methodology narrative.
- **Loihi 2 properly integrated into the energy-evaluation chain** (table, prose, SC2 outcomes row, future-work future-deployment item).
- Variable-isolation principle is enforced and explicitly stated.
- BOLT pipeline is documented to a production-engineering standard.
- Architectural evolution shows what failed and why, generation by generation, in a standardised structure that's consistent across G0–G3.
- Mathematical validation of energy claims (±0.01% internal consistency) demonstrates rigour.
- Reactive scalability regression analysis is a novel and well-grounded interpretation.
- Comparative efficiency landscape (Table in §4.4) is now methodologically honest about its three asymmetries (task complexity, input resolution, domain statistics) — the table itself has a "Dataset (Task)" column making the COCO/ETraM divide unmissable, plus a `\multicolumn` separator row before the DetectorNX entry, plus a `†` footnote on the mAP/mJ ratio.
- §3.5 (CNN baseline) tables now use the consistent project style (`tabularx` with raggedright p-columns, hlines between rows) — the previously-shrunk Table 3.3 reads at native size.

### Areas for Improvement

1. **Verify the Horowitz CMOS reference** flagged by an existing `\todo` (no longer rendering due to `[disable]` flag, but still exists in source).
2. **The §3.7/latency.tex citation `davies2018loihi`** (Loihi 1 paper) is still used for the *"10× lower latency over embedded GPUs"* historical claim. This is acceptable as historical context but worth flagging — Loihi 2 may have updated latency numbers worth substituting if available.
3. **chapter_4R/quantization_error.tex** has a column-spec mismatch: the table is declared with `|l|c|c|c|` (4 columns) but only contains 3 columns of data per row. Will produce an empty fourth column on render.
4. **`appendix1.tex`** is dead code — it duplicates the chapter title *"Implementation Specifications"* of `appendix_sections/main.tex` but is no longer included in `report.tex`. Should be deleted to avoid future maintenance confusion.
5. **A handful of minor typographical issues** in `outcomes.tex` (lines 13–14): missing spaces after commas — *"scalability'',consuming"* and *"activity,yielding"*. Quick proofreading fix.
6. **`abbreviations.tex` line 37** has *"Backpropgation"* (missing the second "a") — typo in the BPTT acronym definition.

### Path to Outstanding (90+)

The Outstanding band requires (cumulative across previous bands): *"the designs are very well considered, clear, and easy to understand"* + *"the output has been evaluated to a very high level (testing, questionnaires, comparison with similar work)"* + *"the student demonstrates a very thorough understanding of the technical details"* + *"there is very little to fault"* + *"the writing demonstrates an extremely thorough understanding of the project work and the field in which it sits"* + *"explanations of the technical details, work of the project and evaluation are exceptional"*.

To reach Outstanding (in addition to the supervisor priorities now closed):

1. **Ablation study** for at least one major architectural decision. Currently each design choice is justified by reference to a failure mode. An ablation (e.g. "with vs. without SE block at Stage 3", "with vs. without FRR", "T = 4 vs. T = 10 vs. T = 20") would convert design *justifications* into *empirical demonstrations*. Even one ablation experiment elevates the technical-quality assessment substantially.
2. **A T-sweep experiment** for the quantisation-error analysis. The current claim that 1-bit quantisation imposes a global ceiling is consistent with theory but not isolated empirically. Running the same architecture at T ∈ {4, 10, 20} and showing how mIoU degrades would directly validate the 1/T theoretical prediction and convert "consistent with" into "demonstrated by".
3. **Hardware-realisation cross-check.** Real GPU power-meter measurements (e.g. via `nvidia-smi`) alongside the theoretical Horowitz-derived figures would close the loop on SC2's "realised on GPU hardware" requirement and make the energy claim hardware-validated rather than purely theoretical.
4. **Statistical significance.** Variance across multiple training runs (e.g. 3–5 seeds) for the headline metrics would replace point estimates with means + standard deviations. Outstanding evaluations report distributions, not single numbers.
5. **All currently flagged technical-quality nits resolved** — the small items in "Areas for Improvement" above.

These additions are substantial undertakings — items 1–4 are essentially small additional experiments — but they are exactly what distinguishes Outstanding (90+) from Excellent (80–89) at this rubric level.

---

## Section 3.4 — Summary & Conclusions (76/100, weighted 11.4/15)

### Justification

Marginally improved (was 75, now 76) — the SC2 outcome row in `tab:sc_outcomes` now correctly cites *"$76.21\%$ extrapolated on Intel Loihi 2"* (previously *"on Intel Loihi"*), reflecting the Loihi-version disambiguation. The chapter is otherwise structurally unchanged.

The Outcomes section walks through Global Precision Parity, Decisive Efficiency Gains (now with the comparative landscape callback), Temporal Reliability and Sharpening, Real-Time Viability, and a Success Criteria Validation table that closes the loop on every criterion stated in the introduction. The Critical Reflection section identifies four substantive limitations (LIF simulation penalty, temporal quantisation ceiling, detection head mismatch, dataset domain gap) with specificity rather than vagueness, and each limitation is paired with concrete future-work directions (Loihi 2 deployment, adaptive timestepping/TTFS/ROC, SNN-native head, GEN1 + CARLA closed-loop).

The closing summary establishes the spiking paradigm as having *"successfully bridged the precision gap relative to an equivalent continuous baseline"* and *"transitioned SNNs from a theoretical curiosity into a rigorously quantified architectural alternative"*.

The previously-flagged residual issues persist:

- The Bounding Box Sharpening finding in §4.1.3 is partly undermined by the *"Hunting Behaviour"* observed in dense scenes. The temporal results section in `chapter_4R/temporal.tex` does now name both phenomena (Hunting Behaviour, Bounding Box Sharpening, High-confidence early detection) — but the conclusion chapter's outcomes summary still leans toward only the sharpening framing.
- The Real-Time Viability section claims *"validates immediate viability for live deployment"* but the latency was measured on a cloud-class A100 GPU. The wording could be tightened to *"on GPU hardware"*.
- The CARLA future-work item is well-motivated but lacks a falsifiable success criterion (e.g. specific reduction in emergency braking distance).

### Strengths

- SC validation table closes the loop on every criterion from Chapter 1, with the SC2 row now correctly identifying Loihi 2 as the extrapolation target.
- Four limitations are substantive and individually actionable.
- Future-work directions are technically specific (Loihi 2, TTFS, ROC, CARLA, adaptive timestepping) rather than vague.
- Honest about hardware-mismatch penalties and dataset choice trade-offs.
- The detection-head-mismatch framing as *"deliberate methodological constraint"* is mature.

### Areas for Improvement

- Acknowledge *"Hunting Behaviour"* alongside *"Bounding Box Sharpening"* in the conclusion's outcomes summary (currently only the latter is foregrounded; the temporal-results section in Ch4 is more balanced).
- Qualify *"immediate viability"* with the GPU-hardware caveat.
- Tighten the CARLA future-work item with a specific testable success metric (e.g. *"reduce emergency braking distance by X% under conditions Y"*).
- Clean the missing-spaces typos in lines 13–14 of `outcomes.tex` (*"scalability'',consuming"*, *"activity,yielding"*).

### Path to Outstanding (90+)

The Outstanding band requires: *"the summary and conclusions are excellent in precision and coverage. It is clear that the student has mastered the material and has given a definitive set of conclusions and a well thought-through plan for future work to reach definitive conclusions."*

To reach Outstanding:

1. **A definitive overall conclusion sentence.** Currently the closing summary is good but slightly incremental. Outstanding wants *one* crystallised conclusion. E.g. *"The variable-isolated comparison demonstrates that the spiking paradigm imposes a measurable but architecturally tractable precision cost (~5% mIoU) in exchange for an order-of-magnitude reduction in energy demand on automotive-grade event detection — establishing it as a viable, not merely theoretical, route to safety-critical edge perception."*
2. **Each future-work item with a falsifiable success metric.** The four current limitations have future-work directions, but Outstanding wants those directions framed so a future researcher could *know whether they succeeded*.
3. **A "what could not be concluded" section.** Outstanding conclusions acknowledge the limits of what the present evidence supports.
4. **Tight balance on each contribution.** Acknowledge *"Bounding Box Sharpening"* AND *"Hunting Behaviour"* as twin temporal-integration phenomena (one helpful, one problematic) in the conclusion, not just the methods/results chapters.
5. **A forward-looking "what would convince a sceptic" closing.** What experiment, if it succeeded, would establish the spiking paradigm as the dominant approach for automotive perception? Naming that experiment shows mastery beyond the present work.

---

## Section 3.5 — Presentation, Structure & Language (75/100, weighted 7.5/10)

### Justification

**This is the section that has lifted most (was 62, now 75)** — both supervisor structural priorities have been addressed:

**Diagram presence in Background.** Six new figures across §2.2–§2.5 means the chapter is no longer text-only. The Expected band's *"writing is supplemented by an appropriate amount of figures and tables"* criterion is now properly met for those four sections; only §2.6 and §2.7 remain text-only.

**Results-as-own-chapter.** The structural concern about *"results merged with methods"* has been fully resolved by the creation of `chapter_4R/main.tex` as a distinct *"Results and Evaluation"* chapter, with sub-sections for arch_progression, global_evaluator, dynamic_power, theoretical_energy, quantization_error, confidence_calibration, temporal, and latency. A reader (and a marker) navigating the report now sees a clean structural arc: Introduction → Background → Methodology → Results & Evaluation → Conclusions.

**Tables are now consistently styled.** The §3.5 CNN-baseline tables (Tables 3.3 and 3.4) have been migrated from the `\resizebox` pattern that was shrinking text to ~73% of normal size, into proper `tabularx` with `raggedright p{...}` columns. Hlines between rows are now consistent across the project — generational evolution table, arch_progression table, SNN-CNN mapping table, and resblock comparison all share the same horizontal-rule rhythm.

**Other fixes since the previous review:**

- The *"five protocols"* / seven-experiments inconsistency in §3.7 is fixed.
- The temporal evidence section now has three distinct figure labels (`fig:temp_seq_1`, `fig:temp_seq_2`, `fig:temp_seq_3`) — the previously-flagged duplication is resolved.
- The §3.6 *"exponentially increased"* technical-language imprecision has been replaced with *"substantially increased"*.
- The §3.7/quantization_error.tex math-overflow issue has been fixed by splitting the discrete-states list into separate inline math chunks.
- The §3.6 super-box figure placement has been fixed with `[H]` to keep it adjacent to its prose.
- `chapter_4R/global_evaluator.tex` qualitative-inference figure now spans pages cleanly via `\ContinuedFloat` rather than wasting half a page of whitespace.
- The title page now uses `\textbf{DetectorNX} \\[0.4em] <subtitle>` for visual emphasis on the project name.

**Remaining presentation issues** (none structural; all small):

- Two background sections (§2.6, §2.7) remain text-only.
- Several small SPaG items: *"Backpropgation"* typo in `abbreviations.tex` line 37; missing-space comma issues in `outcomes.tex` lines 13–14; `chapter_4R/quantization_error.tex` table column-spec mismatch.
- `appendix1.tex` is dead code (not included in `report.tex`) and should be deleted to avoid future maintenance confusion.
- The §1.6 Report Structure paragraph is now factually wrong about chapter organisation (flagged under §3.1 too).
- `\listoftodos` in `report.tex` is commented out — good — but verify list-of-figures / list-of-tables for any compilation warnings.
- The shortened title agreed in the screencast-side discussions hasn't been applied — `report.tex` line 73 still uses the long *"Evaluating Spiking Neural Networks for High-Definition Automotive Perception"* subtitle.

### Strengths

- Glossary integration is thorough; all `\gls{}` macros consistently used.
- Bibliography is consistently formatted (numeric BibLaTeX style with `sorting=nty`).
- Appendix hyperparameter tables are detailed and complete.
- Tables and figures (where present) have short titles for the list of figures.
- All `\todo` notes are correctly suppressed via the `[disable]` flag (note: `todonotes` is fully commented out now).
- The reorganisation of the appendix and the conversion of the hyperparameter table to `longtable` handle multi-page tables cleanly.
- Appendix audit-samples section is well-categorised with seven narrative groupings.
- The §3.6 generational evolution table uses consistent `\hline` between every row — matching the standard project style established by the §3.2 SC traceability table and the §4.1 arch_progression table.

### Areas for Improvement (priority order)

1. **Fix the §1.6 Report Structure paragraph** to reflect the new four-chapter structure (Background / Methodology / Results / Conclusions). Currently still claims *"integrating the architectural design with the experimental setup and evaluation within a single chapter"* — factually incorrect.
2. **Add a §2.6 figure and a §2.7 figure** to close the diagram-coverage gap completely.
3. **Final SPaG sweep**: *"Backpropgation"* (abbreviations.tex L37); missing-space comma issues (outcomes.tex L13–14); chapter_4R/quantization_error.tex table column count.
4. **Decide on the title** — apply the shortened *"DetectorNX: A Spiking Neural Network for Event-Based Automotive Vehicle Detection"* (or whatever variant has been chosen) to `report.tex` line 73, or commit to keeping the long version.
5. **Delete `appendix1.tex`** (dead code; duplicates `appendix_sections/main.tex` which is the active path).
6. **Apply the `[h]` → `[H]` swap to `fig:constant_target_bias`** preventively (matches what was done for the G1 super-box figure; current `[h]` placement may exhibit similar drift).
7. **Reduce intensifying adverbs** ("drastically", "definitively", "conclusive") in favour of qualified quantitative statements — still a residual issue, e.g. theoretical_energy.tex uses *"definitively validates"*, *"conclusive proof"*, etc.

### Path to Outstanding (90+)

The Outstanding band requires: *"there is very little to fault. A broad vocabulary and a thorough understanding of the English language is evident. Beautifully presented."*

To reach Outstanding:

1. **Beautifully presented** is a high typographic bar. Concretely:
   - Word count comfortably inside the 10,000–15,000 target band (verify with `texcount` after the recent additions, especially the new arch_progression section).
   - Every figure has a short title for the list of figures, a `\centering`, sensible placement, and a caption that interprets the figure rather than just describing it. (Most do; spot-check the new ones.)
   - Tables use consistent spacing, proper booktabs-style rules where applicable, and right-aligned numerics. (You're now using `tabularx` consistently — possibly worth standardising on `\hline` everywhere or `\midrule`/`\toprule` everywhere.)
   - All cross-references resolve (no `??`).
   - No widow/orphan lines, no awkward column breaks, no overlapping floats.
2. **Diagrams in §2.6 and §2.7** to round out the chapter coverage — closes the last presentation gap.
3. **Zero remaining typographical issues.** A final proofread (ideally by a peer) is non-negotiable for Outstanding-tier marks.
4. **Consistent terminology.** Every named concept (DetectorNX-G3-SNN, BOLT, SEWResBlock, FRR, etc.) used identically every time it appears.
5. **Glossary and abbreviations completeness.** All abbreviations correctly spelled (the *"Backpropgation"* typo is exactly the kind of thing Outstanding examiners notice).
6. **Mathematics typesetting at a high standard.** Equations centred and numbered, variables consistently italicised, units in upright Roman, vectors bold, etc.

The bar is very high. Outstanding (90+) at this rubric level effectively means a published-quality manuscript. Realistically, hitting low-to-mid 80s here is the sensible target for a BSc dissertation.

---

## Overall Observations

**What changed since the previous evaluation, what stayed:**

The four supervisor-flagged priorities have all been substantially addressed:

| Priority | Status (was → now) | Where the work landed |
|---|---|---|
| #1 Background diagrams | 0 figures → 6 figures | §2.2 (×2), §2.3 (×2), §2.4, §2.5; §2.6 and §2.7 still pending |
| #2 Results as own chapter | merged → separated | `chapter_4R/main.tex` with 8 sections including the new arch_progression |
| #3 G1/G2/G3 evidence | narrative-only → table + chart in Results | `chapter_4R/arch_progression.tex` placed first in chapter; bidirectional cross-references with §3.6 |
| #4 Loihi 2 disambiguation | ambiguous → explicit | §2.6 energy figures; §3.7 energy-constants table (both Loihi 1 and Loihi 2 listed); §4.4 theoretical-energy table; SC2 outcomes row |

These four closures together account for the +5-mark lift (72 → 77).

**Other supervisor sub-items also addressed since the previous evaluation:**

- COCO/ETraM comparison made more obvious in §4.4 (Dataset column + separator row + `†` footnote on mAP/mJ + three explicit asymmetries listed in prose).
- 200 audit samples accessible (20 paired in `appendix_sections/audit_samples.tex` organised into 7 narrative categories + Drive link to the full 200).
- Reduced title length: structural change applied (DetectorNX bolded + line break). Subtitle still uses the long version; full shortening pending.
- Citations alphabetical-by-name-then-year sorting (`sorting=nty`).
- Several smaller fixes: §3.7 protocol count, temporal figure-reference duplication, §3.6 *"exponentially"* imprecision, table styling consistency.

**The four most consequential improvements before final submission, in priority order:**

1. **Fix §1.6 Report Structure paragraph** — currently factually wrong about chapter organisation. This is the single highest-priority remaining issue because it's a *factual error* the marker will spot immediately when navigating the report.
2. **Add §2.6 and §2.7 figures** to complete the background-diagram set. ~75% of supervisor priority #1 is done; closing the last 25% is straightforward (one diagram each).
3. **Final SPaG sweep** for the small typographic items (*"Backpropgation"*, missing-space commas, etc.).
4. **Delete `appendix1.tex`** dead-code file.

If those four are addressed, the projected band moves from 77 to ~80 (mid-First). Pushing further into the 80s requires the Outstanding-tier additions (literature-derived SCs, ablation studies, T-sweep, multi-seed variance) listed in the per-section Path to Outstanding subsections.

---

## Cross-Cutting Path to Outstanding (90+)

The supervisor priorities have moved the report from ~72 to ~77 (comfortable First). Pushing further into Outstanding (90+) is a different and higher bar that involves substantive additions, not just refinements. A realistic Outstanding-tier roadmap, prioritised by impact-per-effort:

**High impact, low-to-moderate effort (the closeable items):**

1. **Fix §1.6 Report Structure paragraph** — must-do; cheap.
2. **Add §2.6 and §2.7 background figures** — completes supervisor priority #1. Lifts §3.2 from 75 to ~78.
3. **SPaG sweep + delete dead `appendix1.tex`** — minor lift across §3.5.

These three together would move the report to ~80 (mid-First).

**High impact, high effort (the Outstanding-tier additions):**

4. **One ablation experiment** (e.g. with vs. without SE block at Stage 3, or with vs. without FRR penalty). Converts a design justification into an empirical demonstration. Pushes §3.3 into Outstanding territory.
5. **One T-sweep experiment** for the quantisation-error analysis (T = 4, 10, 20). Validates the 1/T theoretical prediction empirically. Pushes §3.3 into Outstanding territory.
6. **Multi-seed variance reporting** for the headline metrics. 3–5 training seeds, report mean ± std deviation. Replaces point estimates with distributions. Pushes §3.3 from "Excellent" to "Outstanding".

**Moderate impact, low effort:**

7. **Literature-derive the success criteria** in Chapter 1. Each SC needs a sentence linking it to prior work. Lifts §3.1.
8. **Articulate relevance per cited work** in Background. Each major citation tied to a specific DetectorNX choice. Lifts §3.2.
9. **A definitive overall conclusion sentence** in Chapter 4 closer. One crystallised takeaway. Lifts §3.4.
10. **Falsifiable success metrics for each future-work item.** What would success look like quantitatively? Lifts §3.4.
11. **Final proofread pass** for typography, intensifiers, and remaining minor errors. Lifts §3.5.

**Realistic target:**

For a BSc dissertation, the report has now meaningfully entered the comfortable First range (~77). With items 1–3 above (~1 day of focused work), it should land at ~80. With items 4–6 (~1–2 weeks of additional experimental work, each), individual sections could push toward Outstanding territory. Hitting 90+ overall requires both substantively novel results (which this project arguably has — the variable-isolated comparison protocol + scale-stable quantisation finding + implicit-uncertainty-sensor finding) AND publication-quality presentation. The substance is there; items 1–6 above would close most of the remaining gap.

**Effort budget:**

- The four immediate closeable items (§1.6 fix, §2.6+§2.7 figures, SPaG, appendix1 deletion) ≈ 1 day. Lifts to ~80.
- Adding any one of the empirical extensions (ablation, T-sweep, multi-seed) ≈ 1–2 weeks each. Each one moves a section closer to Outstanding.
- Full Outstanding-tier polish (all literature derivations, full bibliography audit, comprehensive diagram set, multi-seed variance, ablations, T-sweep, beautiful typesetting, final proofread) ≈ 4–6 weeks of full-time work.

If submission is imminent, items 1–3 are the right focus. If you have several more weeks available and want to push for Outstanding, items 4–6 are where the marginal effort buys the most.

---

*Evaluation performed by Claude (claude-opus-4-7) on 2026-05-03, intentionally calibrated to the supervisor's feedback recorded in `supervisor_notes.md`. Every `.tex` file in `report/` was read from scratch for this evaluation; no cached summaries or prior context was used to assess the current state. The marking emphasises the same concerns the supervisor raised (diagram absence, results-vs-methods structural distinction, G1/G2/G3 progression evidence, Loihi version specificity) so that the projected band and concrete improvement priorities better reflect what a real second marker who has access to the supervisor's input would conclude. The "Path to Outstanding" subsections per rubric area, plus the cross-cutting roadmap, identify what would be needed to push each section toward 90+ — separately from what the supervisor's feedback prioritises in the immediate term. No `.tex` files were edited during this evaluation. The `+5-mark` delta vs the previous report card (72 → 77) is attributable primarily to the closure of three of the four supervisor priorities; the fourth (Loihi disambiguation) was a smaller-impact-but-equally-clean closure.*
