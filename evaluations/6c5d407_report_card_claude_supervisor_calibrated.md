---
Hash: 6c5d407
Branch: draft2
Date: Sun May 03 2026
Time: (third re-evaluation following supervisor-priority work + lit-anchoring + §2.6 figure)
Evaluator: Claude (claude-opus-4-7) — calibrated to supervisor feedback in `supervisor_notes.md`
---

# DetectorNX — Report Card (Supervisor-Calibrated)

**Report Title:** DetectorNX — Evaluating Spiking Neural Networks for High-Definition Automotive Perception
**Degree Programme:** BSc Computer Science (COMP30040)
**Supervisor:** Dr Oliver Rhodes
**Rubric Source:** `guides/project_assessment.pdf`
**Calibration Note:** Same calibration approach as the previous two report cards (`cc59984_…` and `291f93d_…`). The marking weights the supervisor-flagged concerns in proportion to how a real second marker reading the current draft would respond. This evaluation does not re-read every `.tex` file from scratch (that was done at `291f93d` two days ago); instead it tracks the diff against `291f93d` and re-scores accordingly.

---

## Score Summary

| Rubric Section | Weight | Raw | Weighted |
|---|---|---|---|
| 3.1 Abstract & Introduction | 15% | 79 | 11.85 / 15 |
| 3.2 Background & Theory | 25% | 76 | 19.0 / 25 |
| 3.3 Technical Quality, Methodology & Evaluation | 35% | 80 | 28.0 / 35 |
| 3.4 Summary & Conclusions | 15% | 76 | 11.4 / 15 |
| 3.5 Presentation, Structure & Language | 10% | 76 | 7.6 / 10 |
| **Overall** | 100% | — | **~78 / 100** |

**Projected band:** Comfortable First Class (lower-mid).
**Delta vs previous evaluation (`291f93d`, also 2026-05-03):** **+1 mark** (77 → 78).
**Delta vs original supervisor-feedback evaluation (`cc59984`, 2026-04-30):** **+6 marks** (72 → 78) over ~3 days of focused work.

---

## Headline (mirroring supervisor's tone)

Modest incremental progress since the prior card. The §2.6 *MAC vs AC* figure added today closes one of the two remaining background-figure gaps — §2.6 now has visual support for its central energy-economics claim. The §1.5 metrics suite has been lit-anchored to COCO (Lin et al.) + Pascal VOC (Everingham et al.) + Guo et al., closing one of the smaller §3.1 gaps. Various SVG and SPaG polish landed (SNN ONLY badge alignment, `∈` → `in` substitutions in two SVGs, table styling fixes from the prior pass holding firm).

The **single biggest remaining gap is still §1.4 Success Criteria**: 4 of 6 criteria (SC2, SC4, SC5, SC6) lack literature anchors, and the framing sentence presents the SC set as project-internal goals rather than as derived from prior work. The Outstanding-band rubric criterion for §3.1 specifically calls for an *"evaluation strategy derived from such literature"* — that work is drafted in chat but not yet applied.

Two other discussed-but-not-yet-applied items: the §1.6 Report Structure paragraph (still factually wrong about chapter organisation) and the §1.5 ECE wording (still claims ECE is computed when the project actually uses Reliability Diagrams).

If those three drafted-but-not-applied items land, the report should reach ~80 (mid-First). The remaining lift to upper-First / Outstanding requires either the §2.7 figure plus §1.4 anchoring (both within reach) or the substantive empirical extensions (ablation, T-sweep, multi-seed variance — each ~1–2 weeks).

---

## Section 3.1 — Abstract & Introduction (79/100, weighted 11.85/15)

### Justification

Score nudged from 78 to 79 by the §1.5 *Evaluation Approach* lit-anchoring. The metrics suite is now correctly framed as derived from established benchmarks: *"...using the standard object-detection evaluation suite (\gls{iou}, \gls{map_50}, recall at a fixed overlap threshold) established by~\textcite{lin2014microsoft} and~\textcite{everingham2010pascal}, complemented by \gls{ece}-based confidence calibration \cite{guo2017calibration}."* This is exactly the kind of literature-derivation the rubric wants — it converts the metrics from project-internal choices to community-established conventions.

The abstract still delivers a tight problem framing, names the project, states the research question, and reports six concrete numerical outcomes (94.9% mIoU parity, 91.3% mAP\textsubscript{50} parity, 100% recall, 94.33% energy saving, 259.80 FPS, superior low-confidence calibration). The novelty claim is appropriately hedged.

The introduction (Chapter 1) retains the well-judged structure: regulatory motivation grounded in Euro NCAP 2026 protocols, CPU→GPU technical-squeeze framing via Lin, six quantitative success criteria, and the chapter-by-chapter map.

**However, three known issues persist** and prevent §3.1 from moving further toward the Outstanding band:

1. **§1.4 Success Criteria — still 4 of 6 unanchored.** SC2 (energy savings), SC4 (architectural parity), SC5 (detection completeness, IoU>0.5), and SC6 (calibration) are all stated without literature anchors. The Outstanding-band rubric explicitly wants the evaluation strategy *"derived from such literature"* — and §1.4 is where that derivation would primarily live. The recommended changes (Cordone for SC2/SC4, Lin for SC5, Guo for SC6, plus a literature-anchoring opening sentence) were drafted in chat but **not yet applied**.
2. **§1.5 ECE wording is methodologically inaccurate.** §1.5 currently says *"ECE-based confidence calibration"* but the actual experimental sections (`chapter_3/3_7_sections/confidence_calibration.tex` and `chapter_4R/confidence_calibration.tex`) use **Reliability Diagrams**, not computed ECE values. ECE is defined as an acronym in `abbreviations.tex` and named in §1.5 + the SC validation table, but no scalar ECE values appear anywhere in the report. A careful examiner who flips between §1.5 and the calibration-results section will spot the mismatch. Recommended fix (rewrite to *"reliability-diagram-based calibration analysis following the framework of Guo et al. \cite{guo2017calibration}"*) drafted in chat but **not yet applied**.
3. **§1.6 Report Structure is still factually wrong.** It claims *"By integrating the architectural design (DetectorNX-G3-SNN and DetectorNX-G3-CNN) with the experimental setup and evaluation within a single chapter, the report directly links architectural choices..."* — but the report has been restructured so methods (Chapter 3) and results (Chapter 4) are now distinct. A 4-paragraph rewrite was drafted in chat but **not yet applied**.

### Strengths

- Six quantitative success criteria with traceability through the report.
- Abstract foregrounds the falsification finding (scale-stable quantisation ceiling), demonstrating engagement with results rather than pure positives.
- Introduction's CPU→GPU trajectory framing is a defensible forward-looking argument grounded in Lin's actual claims.
- §1.5 metrics suite now lit-anchored to COCO + Pascal VOC + Guo — closes one of the smaller §3.1 gaps and reads as deliberately derived from established benchmarks.
- SpikeDet, SpikeYOLO, EMS-YOLO competitor positioning visible in §1.1.

### Areas for Improvement

1. **Apply the §1.4 literature-anchoring (drafted in chat).** Adds a framing sentence + 4 per-SC citations. Closes the binding constraint for §3.1.
2. **Apply the §1.5 ECE → Reliability Diagrams correction (drafted in chat).** Methodological accuracy.
3. **Apply the §1.6 Report Structure rewrite (drafted in chat).** Structural-claim accuracy.
4. **Add a single visual to the introduction** if a clean teaser or regulatory-trajectory chart fits — Outstanding presentations rarely have a text-only introduction. Lower priority.

### Path to Outstanding (90+)

Once items 1–3 above are applied, §3.1 should land at ~83. To push further:

1. **Literature-derived evaluation strategy** — beyond the per-SC citations, add an explicit one-sentence justification of *why* each chosen threshold (90%, 30 FPS, 1% parity, IoU>0.5) was set at that level, citing prior work for each. This converts *"following the convention"* to *"following the convention because [specific reason]"*.
2. **Tighter positioning vs competitors** in §1.1 — currently mentions SpikeDet/SpikeYOLO/EMS-YOLO. Outstanding-band introductions go further: *what does DetectorNX add that none of these do?*
3. **One visual in Chapter 1.**

---

## Section 3.2 — Background & Theory (76/100, weighted 19.0/25)

### Justification

Score nudged from 75 to 76 by the §2.6 *MAC vs AC* figure added today. The figure is a clean side-by-side schematic of the silicon-level operation cost: MAC (×, then +) costing 4.6 pJ on the left, AC (single conditional + when s=1) costing 0.9 pJ on the right, with a *"5× reduction"* tagline pinning the central claim. It uses the same matplotlib rcParams (serif font, similar palette) as the §4 arch_progression chart, so the report's matplotlib visuals now form a coherent visual family. Placement is forced inline (`[H]`) at 0.85\textwidth.

The chapter now has **seven figures** across the original six text-only sections:

- §2.2 *CNN*: hierarchical features (LeCun) + standard residual block (He et al.) — 2 figures
- §2.3 *SNN*: LIF dynamics (custom) + surrogate gradient (custom) — 2 figures
- §2.4 *Event vision*: Gallego frame-vs-event — 1 figure
- §2.5 *ETraM*: Verma sample frames — 1 figure
- **§2.6 *Neuromorphic hardware*: MAC vs AC operation diagram (new today)** — 1 figure
- §2.7 *Related work*: still text-only — 0 figures

Each figure is properly cited (*"Reproduced from \cite{...}"* / *"Adapted from \cite{...}"* / no citation for project-original) and is positioned adjacent to the prose that explains the concept. Captions are descriptive rather than purely titular.

The Loihi version disambiguation continues to land cleanly: §2.6 correctly identifies *"Intel Loihi 2"* with the per-SOP figure of 16.1 pJ alongside IBM TrueNorth at 26.0 pJ.

**Remaining gap: §2.7 Related Work is still text-only.** A landscape scatter (year × resolution, with surveyed competitors marked, DetectorNX in its own quadrant) would close this gap fully and is the single highest-impact remaining diagram for §3.2. The publication-year and input-resolution data needed is mostly already in `chapter_4R/theoretical_energy.tex`'s efficiency-landscape table.

The chapter's other persistent issues from prior reviews: SEWResBlock still introduced for the first time in §3.4 with no Background-level anchor; voxelisation still introduced for the first time in §3.3 rather than §2.4. These are minor and lower-priority than the §2.7 figure.

### Strengths

- **7 of 7 originally-flagged background sections now have figures** except §2.7. Supervisor priority #1 is ~85% complete.
- §2.6 *MAC vs AC* figure makes the central energy-economics claim *visible* — exactly the kind of "concept clarification" diagram the supervisor requested.
- Loihi 2 disambiguation done cleanly throughout (both in this chapter and propagated through §3.7 and §4.4).
- Citations are appropriate and contemporary; the Lin/Everingham/Guo additions today extended this further.
- All matplotlib-generated figures (surrogate gradient, arch progression, MAC vs AC) now share a visual family.

### Areas for Improvement

1. **Add a §2.7 figure** (SNN-detector landscape scatter) — the highest-impact single remaining addition for §3.2. Closes supervisor priority #1 fully. Lifts §3.2 from 76 to ~78.
2. **Anchor SEWResBlock at Background level** — the §3.4 implementation discusses it well, but a Background-level paragraph in §2.2 or §2.3 would mean a reader meets the concept before seeing the implementation.
3. **Voxelisation introduction in §2.4** — close the last Background-coverage gap.

### Path to Outstanding (90+)

To reach Outstanding (in addition to closing the §2.7 figure gap):

1. **A diagram per major concept** rather than just seven. Outstanding rarely has a text-only paragraph for a concept the reader needs to grasp visually.
2. **Explicit relevance-articulation per cited work.** Currently most citations are factual. Outstanding requires *"excellent understanding of the content and relevance of the included literature"* — each major cited work tied to a specific DetectorNX choice.
3. **Bibliography metadata audit.** Verify publication years, venues, and citation keys across every entry. (One specific item: `davies2018loihi` is still cited in §3.7/latency.tex for a latency-benchmark claim — Loihi 2 may have updated latency figures worth substituting.)
4. **Background-section coverage gaps closed entirely** — no reader should encounter a core concept (voxelisation, SEW, multi-box detection head, GIoU loss) for the first time outside Chapter 2.
5. **A "Background Synthesis" closing subsection** that summarises the literature-grounded position of the project before Chapter 3.

---

## Section 3.3 — Technical Quality, Methodology & Evaluation (80/100, weighted 28.0/35)

### Justification

Unchanged from the `291f93d` evaluation. The substantive content of Chapter 3 + Chapter 4R hasn't materially changed since two days ago; the polish work this round was mostly cosmetic (SVG alignment, table styling fixes that landed in the prior pass).

Quick recap of why §3.3 is at 80:

- Variable-isolation experimental design enforced consistently across both backbones.
- BOLT pipeline documented to production-engineering standard.
- Architectural evolution (G0 → G1 → G2 → G3) shows what failed and why, generation by generation, in a standardised four-step structure.
- Mathematical validation of energy claims (±0.01% internal consistency).
- Reactive scalability regression analysis (R² = 0.7514) is a novel and well-grounded interpretation.
- The new `chapter_4R/arch_progression.tex` section (added in the prior session) directly addresses supervisor priority #3 — G1/G2/G3 evidence visible in the Results chapter.
- §4.4 efficiency landscape table now has the Dataset (Task) column + separator row + dagger footnote on mAP/mJ + three explicit asymmetry callouts in prose (added in prior session).

### Strengths

(Unchanged from `291f93d`.)

- Variable-isolation principle enforced and explicitly stated.
- BOLT pipeline documented to a production-engineering standard.
- Architectural evolution shows what failed and why.
- Mathematical validation of energy claims (±0.01%).
- Reactive scalability regression analysis.
- Comparative efficiency landscape methodologically honest about its asymmetries.

### Areas for Improvement

(Unchanged from `291f93d`.)

1. Verify the Horowitz CMOS reference flagged by an existing `\todo`.
2. The §3.7/latency.tex citation `davies2018loihi` is still used for the historical "10× lower latency" claim — Loihi 2 may have updated latency numbers worth substituting.
3. **`chapter_4R/quantization_error.tex`** still has a column-spec mismatch: declared with `|l|c|c|c|` (4 columns) but only contains 3 columns of data per row.
4. A handful of minor SPaG items: `outcomes.tex` lines 13–14 missing-space comma issues; `abbreviations.tex` line 37 *"Backpropgation"* typo.
5. **Apply the §3.2 Cordone-citation removal recommendation** drafted in chat (one-line deletion in `chapter_3/3_2_system_architecture.tex`). The citation was doing weak work in that location and breaks parallelism.

### Path to Outstanding (90+)

(Unchanged from `291f93d`.)

1. **Ablation study** for at least one major architectural decision.
2. **A T-sweep experiment** for the quantisation-error analysis.
3. **Hardware-realisation cross-check** with `nvidia-smi` measurements.
4. **Multi-seed variance reporting** for the headline metrics.

These are the substantive empirical extensions that distinguish Outstanding (90+) from Excellent (80–89).

---

## Section 3.4 — Summary & Conclusions (76/100, weighted 11.4/15)

### Justification

Unchanged from `291f93d`. Chapter 4 hasn't been edited in this session beyond the polish work that's already factored in.

The Outcomes section walks through Global Precision Parity, Decisive Efficiency Gains, Temporal Reliability and Sharpening, Real-Time Viability, and the Success Criteria Validation table. SC2 row correctly cites *"$76.21\%$ extrapolated on Intel Loihi 2"*. Critical Reflection identifies four substantive limitations with specificity; future-work directions are technically specific.

(Same minor refinements still pending as in the `291f93d` evaluation.)

### Strengths

- SC validation table closes the loop on every criterion from Chapter 1.
- Four limitations are substantive and individually actionable.
- Future-work directions technically specific (Loihi 2, TTFS, ROC, CARLA, adaptive timestepping).
- Honest about hardware-mismatch penalties and dataset choice trade-offs.
- Mature framing of the detection-head-mismatch as a *"deliberate methodological constraint"*.

### Areas for Improvement

(Unchanged from `291f93d`.)

- Acknowledge *"Hunting Behaviour"* alongside *"Bounding Box Sharpening"* in the conclusion's outcomes summary.
- Qualify *"immediate viability"* with the GPU-hardware caveat.
- Tighten the CARLA future-work item with a specific testable success metric.
- Clean the missing-spaces typos in `outcomes.tex` lines 13–14.

### Path to Outstanding (90+)

(Unchanged from `291f93d`.) A definitive overall conclusion sentence; falsifiable success metrics for each future-work item; a "what could not be concluded" section; tight balance acknowledging both temporal-integration phenomena; and a forward-looking "what would convince a sceptic" closing.

---

## Section 3.5 — Presentation, Structure & Language (76/100, weighted 7.6/10)

### Justification

Score nudged from 75 to 76 by the SVG and SPaG polish landed today:

- **`high-level-architecture.svg`**: SNN ONLY badge text shifted x=515→518 on lines 100 and 122, fixing the visible left-leaning offset.
- **`sewresblock_diagram.svg` and `se_block_snn_diagram.svg`**: `∈` (U+2208) replaced with `in` across 3 occurrences. The math-symbol glyph was rendering as tofu boxes in the SVG → PDF pipeline due to the fallback font lacking it.
- **`chapter_2/2_6_neuromorphic.tex`**: small SPaG fix — single hyphen `-` replaced with em-dash `---`.

Plus the §2.6 figure addition earns a small presentation bonus — the chapter now reads as visually supported.

**Remaining presentation issues (carry-over from prior cards):**

- §2.6 figure newly added; §2.7 still text-only.
- Several small SPaG items still pending: *"Backpropgation"* typo (`abbreviations.tex` L37); missing-space comma issues (`outcomes.tex` L13–14); `chapter_4R/quantization_error.tex` table column-spec mismatch.
- The §1.6 Report Structure paragraph is still factually wrong about chapter organisation.
- The shortened title agreed in the screencast-side discussions hasn't been applied — `report.tex` line 73 still uses the long subtitle.
- §1.5 ECE wording mismatch (raised under §3.1) is also a presentation/structural issue: a metric named in the introduction but never computed in the results.

### Strengths

(Largely unchanged from `291f93d`, plus today's polish:)

- Glossary integration thorough; `\gls{}` macros consistently used.
- Bibliography consistently formatted (numeric BibLaTeX with `sorting=nty`).
- Appendix hyperparameter tables detailed and complete.
- Figures (where present) have short titles for the list of figures.
- All `\todo` notes correctly suppressed.
- Tables now styled consistently across the project (the `tabularx` + raggedright + hlines pattern established in the prior pass).
- The new MAC vs AC figure visually consistent with prior matplotlib charts (arch progression).
- SVG rendering issues addressed — `∈` no longer renders as tofu, SNN ONLY badges centred.

### Areas for Improvement (priority order)

1. **Apply the §1.6 Report Structure rewrite** (drafted in chat; ~134 words; reflects the new four-chapter layout).
2. **Apply the §1.5 ECE → Reliability Diagrams correction** (drafted in chat; methodological accuracy).
3. **Add a §2.7 figure** (SNN-detector landscape scatter) to close the diagram-coverage gap completely.
4. **Final SPaG sweep**: *"Backpropgation"* (abbreviations.tex L37); missing-space comma issues (outcomes.tex L13–14); chapter_4R/quantization_error.tex table column count.
5. **Decide on the title** — apply the shortened subtitle to `report.tex` line 73 or commit to the long version.
6. **Apply the `[h]` → `[H]` swap to `fig:constant_target_bias`** preventively (matches what was done for the G1 super-box figure; current `[h]` placement may exhibit similar drift).

### Path to Outstanding (90+)

Same as `291f93d`. *"Beautifully presented"* is a high typographic bar requiring zero remaining typographical issues, diagrams everywhere they earn their place, consistent terminology, complete glossary, and high-standard mathematics typesetting.

---

## Overall Observations

**What changed since the previous evaluation (291f93d), what stayed:**

| Item | Status change | Net mark impact |
|---|---|---|
| §2.6 *MAC vs AC* figure added | Background figure 6→7 of 8 | §3.2 75 → 76 (+0.25 weighted) |
| §1.5 metrics suite lit-anchored (Lin + Everingham + Guo) | Closes one §3.1 gap | §3.1 78 → 79 (+0.15 weighted) |
| SVG fixes (SNN ONLY badges, `∈` → `in` in 2 SVGs) | Visible polish | §3.5 75 → 76 (+0.1 weighted) |
| SPaG: em-dash in §2.6 | Cosmetic | included in §3.5 lift |
| §1.4 SC literature anchoring (drafted) | Discussed but **not yet applied** | Would lift §3.1 79 → 83 if applied |
| §1.6 Report Structure (drafted) | Discussed but **not yet applied** | Would lift §3.1 + §3.5 |
| §1.5 ECE wording fix (drafted) | Discussed but **not yet applied** | Would close a methodological-accuracy issue |
| §3.2 Cordone citation removal (drafted) | Discussed but **not yet applied** | Cosmetic |
| §2.7 figure (planned) | Discussed; data partially available | Would lift §3.2 76 → 78 if built |

**Net: +1 mark (~77 → ~78).** The primary driver is the §2.6 figure, with smaller contributions from §1.5 lit-anchoring and SVG polish.

**The four most consequential remaining improvements before final submission, in priority order:**

1. **Apply the §1.4 SC literature-anchoring** (drafted in chat). Converts the evaluation strategy from project-internal targets to literature-derived framework. Estimated lift: §3.1 79 → 83 = **+0.6 weighted marks**.
2. **Add the §2.7 figure** (SNN-detector landscape scatter). Closes supervisor priority #1 fully. Estimated lift: §3.2 76 → 78 = **+0.5 weighted marks**.
3. **Apply the §1.6 Report Structure rewrite + §1.5 ECE wording fix** (both drafted). Methodological / structural accuracy. Combined lift: ~+0.3 weighted marks.
4. **Final SPaG sweep + table column-spec fix + Cordone citation removal**. Combined lift: ~+0.2 weighted marks.

If items 1–4 are addressed, the projected band moves from ~78 to **~80** (mid-First). The substance is already there; the presentation refinements would let it land properly.

---

## Cross-Cutting Path to Outstanding (90+)

The supervisor priorities have moved the report from ~72 to ~78 over three days of focused work. Pushing further into Outstanding (90+) is a different and higher bar that involves substantive additions, not just refinements.

**High impact, low-to-moderate effort (the closeable items):**

1. **Apply the §1.4 SC literature-anchoring** (drafted; ~30 min of edit work). Lifts §3.1.
2. **Add §2.7 background figure** (~1–2 hours; data mostly already to hand). Lifts §3.2.
3. **Apply the §1.6 + §1.5 + §3.2-Cordone drafted edits** (~30 min of edit work). Lifts §3.1 + §3.5.
4. **SPaG sweep** (~30 min). Lifts §3.5.

Combined: **~3–4 hours of focused work** would lift the overall to ~80.

**High impact, high effort (the Outstanding-tier additions):**

5. **One ablation experiment** (~1–2 weeks). §3.3 80 → 85.
6. **One T-sweep experiment** (~1–2 weeks). §3.3 80 → 85.
7. **Multi-seed variance reporting** (~3–5 days of training compute + analysis). §3.3 toward 85.

**Moderate impact, low effort:**

8. **Literature-derive the success criteria** beyond per-SC citations — explicit one-sentence justification of *why* each chosen threshold was set at that level. Lifts §3.1.
9. **Articulate relevance per cited work** in Background. Each major citation tied to a specific DetectorNX choice. Lifts §3.2.
10. **A definitive overall conclusion sentence** in Chapter 4 closer. Lifts §3.4.
11. **Falsifiable success metrics for each future-work item.** Lifts §3.4.
12. **Final proofread pass** for residual typographical issues. Lifts §3.5.

**Realistic target:**

For a BSc dissertation, the report has now meaningfully entered the comfortable First range (~78). With items 1–4 above (~3–4 hours), it should land at ~80. With items 5–7 (~1–2 weeks each), individual sections could push toward Outstanding territory. Hitting 90+ overall requires both substantively novel results (which this project arguably has — the variable-isolated comparison protocol + scale-stable quantisation finding + implicit-uncertainty-sensor finding) AND publication-quality presentation. The substance is there; items 1–7 above would close most of the remaining gap.

**Effort budget:**

- Closeable items (1–4): ~3–4 hours total. Lifts to ~80.
- Adding any one of the empirical extensions (5–7): ~1–2 weeks each.
- Full Outstanding-tier polish: ~4–6 weeks of full-time work.

If submission is imminent, items 1–4 are the right focus.

---

## Three-Card Trajectory (cc59984 → 291f93d → 6c5d407)

| Section | cc59984 (2026-04-30) | 291f93d (2026-05-03 a.m.) | 6c5d407 (2026-05-03 p.m.) | Δ |
|---|---|---|---|---|
| 3.1 Abstract & Introduction | 78 | 78 | **79** | +1 |
| 3.2 Background & Theory | 65 | 75 | **76** | +11 |
| 3.3 Technical Quality | 75 | 80 | **80** | +5 |
| 3.4 Summary & Conclusions | 75 | 76 | **76** | +1 |
| 3.5 Presentation | 62 | 75 | **76** | +14 |
| **Overall** | **72** | **77** | **78** | **+6** |

The biggest section-level lifts have been §3.5 (+14, presentation work) and §3.2 (+11, background diagrams). §3.3 also lifted +5 from the new arch_progression Results section. §3.1 and §3.4 remain mostly stable — they have less low-hanging fruit, and their Outstanding-tier improvements require substantive content additions rather than polish.

---

*Evaluation performed by Claude (claude-opus-4-7) on 2026-05-03, intentionally calibrated to the supervisor's feedback recorded in `supervisor_notes.md`. The marking emphasises the same concerns the supervisor raised so that the projected band and concrete improvement priorities better reflect what a real second marker who has access to the supervisor's input would conclude. The "Path to Outstanding" subsections per rubric area, plus the cross-cutting roadmap, identify what would be needed to push each section toward 90+ — separately from what the supervisor's feedback prioritises in the immediate term. No `.tex` files were edited during this evaluation. Calibration consistency: this is the third successive supervisor-calibrated card by the same evaluator using the same rubric weighting; the +1 delta from `291f93d` reflects the §2.6 figure addition + §1.5 lit-anchoring + SVG polish landed today.*
