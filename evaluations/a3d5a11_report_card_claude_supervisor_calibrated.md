---
Hash: a3d5a11
Branch: draft2
Date: Mon May 04 2026
Time: 10:27:39
Evaluator: Claude (claude-opus-4-7) — calibrated to supervisor feedback in `supervisor_notes.md`
---

# DetectorNX — Report Card (Supervisor-Calibrated)

**Report Title:** DetectorNX — Evaluating Spiking Neural Networks for High-Definition Automotive Perception
**Degree Programme:** BSc Computer Science (COMP30040)
**Supervisor:** Dr Oliver Rhodes
**Rubric Source:** `guides/project_assessment.pdf`
**Calibration Note:** Same calibration approach as the previous three report cards in this series (`cc59984_…`, `291f93d_…`, `6c5d407_…`). The marking weights the supervisor-flagged concerns in proportion to how a real second marker reading the current draft would respond. This evaluation is anchored on the agent's three full re-reads of the report performed earlier today (after each of three SPaG passes), with the diff vs `6c5d407` taken from the SESSION_HANDOFF entries for the day.

---

## Score Summary

| Rubric Section | Weight | Raw | Weighted |
|---|---|---|---|
| 3.1 Abstract & Introduction | 15% | 80 | 12.00 / 15 |
| 3.2 Background & Theory | 25% | 76 | 19.00 / 25 |
| 3.3 Technical Quality, Methodology & Evaluation | 35% | 80 | 28.00 / 35 |
| 3.4 Summary & Conclusions | 15% | 76 | 11.40 / 15 |
| 3.5 Presentation, Structure & Language | 10% | 81 | 8.10 / 10 |
| **Overall** | 100% | — | **~79 / 100** |

**Projected band:** Comfortable First Class (lower-mid).
**Delta vs previous evaluation (`6c5d407`, 2026-05-03 p.m.):** **+1 mark** (78 → 79).
**Delta vs original supervisor-feedback evaluation (`cc59984`, 2026-04-30):** **+7 marks** (72 → 79) over four days.

---

## Headline (mirroring supervisor's tone)

The day's work has been almost entirely **typographic, mechanical, and methodological-accuracy polish** — three full SPaG passes (35 + 22 + 35 = ~92 applied fixes plus ~7 math-notation typography improvements), ~6 user-driven micro-edits, and one focused soundness/correctness review that surfaced 12 substantive findings.

The biggest *content-affecting* changes since `6c5d407`:

1. **§1.5 ECE wording fix applied.** The methodological-inaccuracy callout from the 6c5d407 card has been resolved — §1.5 now correctly says *"reliability-diagram-based calibration analysis"* rather than *"ECE-based confidence calibration"*. This was the single biggest §3.1 callout in the prior card and is now closed.
2. **§1.6 partial alignment.** *"Neuromorphic energy economics"* → *"neuromorphic hardware and energy modelling"* (matches §2.6's actual title), plus *"confidence-calibration"* hyphen removed. The full §1.6 rewrite (factual chapter-organisation claim) is still pending.
3. **§3.3.5 (latency hypothesis) unit error.** `33\text{ ms}^{-1}` rendered as "per millisecond" — corrected to `33\,m\,s^{-1}` (metres per second). Genuine factual fix.
4. **§3.7.6 typography bug.** `($E_{chip})$` (with stray closing paren outside math + extra `$`) corrected to `($E_{chip}$)`.
5. **§3.7.1 / §3.7.6 math notation polish.** All six math-mode `FLOPs_l` / `SOPs_l` instances wrapped in `\mathrm{}` so the acronyms render upright as proper names rather than as italic-letter products `F·L·O·P·s_l`.
6. **§3.7.7 metric count fix.** *"Four complementary metrics"* → *"Five complementary metrics"* (matches the actual list).

Plus the cumulative effect of ~92 individual SPaG fixes across all chapters: Oxford commas added in lists; em-dashes corrected; American-→-British spellings (`localization`→`localisation`, `analyze`→`analyse`, `synthesizing`→`synthesising`, `artifact`→`artefact`); closing-backtick errors fixed (`` ``X`` `` → `` ``X'' ``); subject–verb agreement fixed in several places; missing articles inserted (`a \gls{ac}` → `an \gls{ac}`); broken sentences rewritten; orphan `\todo` comments deleted; unit notation standardised (`100ms`→`100\,ms`, `\mu J`→`\mu\text{J}`).

**The single biggest remaining gap is still §1.4 Success Criteria literature anchoring.** Four of six SCs (SC2, SC4, SC5, SC6) lack literature anchors. Drafted in chat across multiple sessions but never applied. This remains the binding constraint for §3.1 reaching the upper-First / Outstanding band.

**A new concern this round: today's soundness review surfaced 12 substantive findings (now visible to the agent's analysis) that pre-existed the SPaG work and are largely still unfixed.** They include factual contradictions (V_{th} history disagreement between §3.4 and §3.6), definitional mismatches (recall metric framed three different ways), promised-but-not-reported metrics (Mean Prediction Confidence in §3.7.7 doesn't appear in the §4R table), and stale references ("Phase 1 ambiguity problem" in §3.7.7 with no Phase definition anywhere). See "Soundness Review Findings" below. None of these are catastrophic, but a careful examiner doing a second read would catch them.

---

## Section 3.1 — Abstract & Introduction (80/100, weighted 12.00/15)

### Justification

Score nudged from 79 to 80 by:

- **§1.5 ECE wording fix applied** — this was the single substantive methodological-accuracy concern called out in the `6c5d407` card. §1.5 now correctly says *"reliability-diagram-based calibration analysis following the framework of Guo et al. \cite{guo2017calibration}"* matching what the actual experiments do. (One downstream side-effect: the `\newacronym{ece}` line in `abbreviations.tex:35` is now orphaned and should be deleted.)
- **§1.6 partial alignment** — the *"neuromorphic hardware and energy modelling"* phrasing now matches §2.6's title; *"confidence-calibration"* hyphen removed. The full §1.6 chapter-organisation rewrite is still pending.
- **Abstract preposition fix** — *"superior confidence calibration at low-confidence regions"* → *"in low-confidence regions"*.
- **§1.1 opener tightened** — *"…driven by both legislation and consumer demand to adopt increasingly complex autonomous driving systems, which will inevitably require…"* → *"…driven by legislation and consumer demand for increasingly complex autonomous driving systems requiring…"*.
- **§1.1 motivation glossary fix** — `\acrfull{ac}` swapped for `\gls{ac}` to avoid *"Conditional Addition (AC) additions"* redundancy.
- **§1.1 abstract typography** — *"identical-model"* → *"strict architectural"* (applied in Pass 1).

The abstract still delivers a tight problem framing, names the project, states the research question, and reports six concrete numerical outcomes (94.9% mIoU parity, 91.3% mAP\textsubscript{50} parity, 100% recall, 94.33% energy saving, 259.80 FPS, superior low-confidence calibration). The novelty claim is appropriately hedged.

The introduction (Chapter 1) retains its well-judged structure: regulatory motivation grounded in Euro NCAP 2026 protocols, CPU→GPU technical-squeeze framing via Lin, six quantitative success criteria, and the chapter-by-chapter map.

**However, two known issues persist** and prevent §3.1 from moving further toward the Outstanding band:

1. **§1.4 Success Criteria — still 4 of 6 unanchored.** SC2 (energy savings), SC4 (architectural parity), SC5 (detection completeness, IoU>0.5), and SC6 (calibration) are all stated without literature anchors. The Outstanding-band rubric explicitly wants the evaluation strategy *"derived from such literature"* — and §1.4 is where that derivation would primarily live. Recommended changes (Cordone for SC2/SC4, Lin for SC5, Guo for SC6, plus a literature-anchoring opening sentence) drafted in chat across multiple sessions but **not yet applied**.
2. **§1.6 Report Structure full rewrite still pending.** The chapter-organisation factual claim is still slightly off (drafted 134-word rewrite waiting in chat).

**Plus a new in-flight item:** the user has proposed standardising SC5's recall wording to `Both models must achieve $100\%$ recall at $\mathrm{IoU}=0.5$ on the validation set` — agent recommended applying this AND propagating the `=0.5` framing across the abstract, §4R/global_evaluator critical analysis, §4 outcomes table, and §3.7.7 metric description (5–6 locations total). This change is greenlit-pending but not yet applied.

### Strengths

- Six quantitative success criteria with traceability through the report.
- Abstract foregrounds the falsification finding (scale-stable quantisation ceiling), demonstrating engagement with results rather than pure positives.
- Introduction's CPU→GPU trajectory framing is a defensible forward-looking argument grounded in Lin's actual claims.
- §1.5 metrics suite lit-anchored to COCO + Pascal VOC + Guo.
- §1.5 calibration methodology now methodologically accurate (reliability-diagram-based, not ECE).
- §1.6 partial alignment with §2.6's actual title.
- SpikeDet, SpikeYOLO, EMS-YOLO competitor positioning visible in §1.1.

### Areas for Improvement

1. **Apply the §1.4 literature-anchoring (drafted in chat, multiple sessions).** Adds a framing sentence + 4 per-SC citations. Closes the binding constraint for §3.1.
2. **Apply the §1.6 Report Structure full rewrite (drafted in chat).** Structural-claim accuracy.
3. **Apply the SC5 reformulation across 5–6 locations (drafted in chat, awaiting greenlight).** Resolves a definitional inconsistency that affects §3.1 + §3.3 + §3.4.
4. **Delete orphan `\newacronym{ece}` from `abbreviations.tex:35`** — leftover after the §1.5 fix.
5. **Add a single visual to the introduction** if a clean teaser or regulatory-trajectory chart fits — Outstanding presentations rarely have a text-only introduction. Lower priority.

### Path to Outstanding (90+)

Once items 1–4 above are applied, §3.1 should land at ~83. To push further:

1. **Literature-derived evaluation strategy** — beyond per-SC citations, add an explicit one-sentence justification of *why* each chosen threshold (90%, 30 FPS, 1% parity, IoU>0.5) was set at that level, citing prior work for each.
2. **Tighter positioning vs competitors** in §1.1 — currently mentions SpikeDet/SpikeYOLO/EMS-YOLO. Outstanding-band introductions go further: *what does DetectorNX add that none of these do?*
3. **One visual in Chapter 1.**

---

## Section 3.2 — Background & Theory (76/100, weighted 19.00/25)

### Justification

**Unchanged from `6c5d407`.** The substantive content of Chapter 2 hasn't materially changed since two days ago; today's work was SPaG only (em-dash corrections, apposition rewrites, glossary `\gls{ac}` substitutions, a unit notation fix, an article fix). These are presentation improvements that primarily affect §3.5, not the §3.2 substantive judgement.

The chapter retains its **seven figures** across the original six text-only sections:

- §2.2 *CNN*: hierarchical features (LeCun) + standard residual block (He et al.) — 2 figures
- §2.3 *SNN*: LIF dynamics (custom) + surrogate gradient (custom) — 2 figures
- §2.4 *Event vision*: Gallego frame-vs-event — 1 figure
- §2.5 *ETraM*: Verma sample frames — 1 figure
- §2.6 *Neuromorphic hardware*: MAC vs AC operation diagram — 1 figure
- §2.7 *Related work*: still text-only — 0 figures

**Remaining gap: §2.7 Related Work is still text-only.** A landscape scatter (year × resolution, with surveyed competitors marked, DetectorNX in its own quadrant) would close this gap fully and is the single highest-impact remaining diagram for §3.2. The publication-year and input-resolution data needed is mostly already in `chapter_4R/theoretical_energy.tex`'s efficiency-landscape table.

The chapter's other persistent issues from prior reviews: SEWResBlock still introduced for the first time in §3.4 with no Background-level anchor; voxelisation still introduced for the first time in §3.3 rather than §2.4. These are minor and lower-priority than the §2.7 figure.

### Strengths

- 7 of 7 originally-flagged background sections now have figures except §2.7. Supervisor priority #1 is ~85% complete.
- §2.6 *MAC vs AC* figure makes the central energy-economics claim *visible* — exactly the kind of "concept clarification" diagram the supervisor requested.
- Loihi 2 disambiguation done cleanly throughout (both in this chapter and propagated through §3.7 and §4.4).
- Citations are appropriate and contemporary; the Lin/Everingham/Guo additions on the prior pass extended this further.
- All matplotlib-generated figures (surrogate gradient, arch progression, MAC vs AC) share a visual family.
- Today's SPaG polish has tightened several apposition issues in §2.3, §2.5, §2.6, and §2.7 that were minor irritations.

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

## Section 3.3 — Technical Quality, Methodology & Evaluation (80/100, weighted 28.00/35)

### Justification

**Unchanged headline (80) but composition shifts.** Today's work delivered four substantive technical-quality improvements:

1. **Math notation polish (`\mathrm{FLOPs}_l` / `\mathrm{SOPs}_l`)** in §3.7.1 and §3.7.6. Previously rendered as italic-letter products (`F·L·O·P·s·_l`) which looked like multiple-variable multiplication — now correctly rendered as proper names with subscript $l$ italic. Six instances across two files.
2. **Unit error fix in §3.7.5** (latency hypothesis) — `33\text{ ms}^{-1}` (which renders as "per millisecond") corrected to `33\,m\,s^{-1}` (metres per second). The unit was just wrong.
3. **Typography bug in §3.7.6** subsubsection title — `($E_{chip})$` (closing paren outside math + stray `$`) corrected to `($E_{chip}$)`.
4. **§3.7.7 metric count fix** — *"Four complementary metrics"* → *"Five"* (matching the actual list of mIoU, mAP_50, Recall, ADP, Mean Prediction Confidence).

These would individually push §3.3 up by ~1 mark.

**However, the soundness review surfaced 12 findings** that, while pre-existing, reduce confidence in some of §3.3's headline claims if a careful examiner reads through:

- **V_{th} history contradiction** between §3.4 (says earlier $V_{th}=0.3$) and §3.6 (says lowered $V_{th}=0.5\rightarrow0.2$). Cannot both be correct.
- **Training-speedup numbers don't reconcile.** §3.4 (16h → 7h, ~2.3×) vs §3.6 (1.8× combined with AMP).
- **Recall metric defined three different ways** across SC5 / §3.7.7 / §4R table caption.
- **Mean Prediction Confidence promised in §3.7.7 but not actually reported** in §4R (table reports Max/Min instead).
- **§3.7.7 references "Phase 1 ambiguity problem"** — but the project uses Generations G0/G1/G2/G3, no Phase defined.
- **§3.7.5 (latency) LIF formula not algebraically identical to §2.3 main formula.** Different placement of the $1/\tau$ factor.

These are genuine consistency/definitional issues a careful examiner would catch. They don't drag §3.3 below 80, but they do prevent the math/notation polish from lifting it further.

Net: §3.3 stays at 80. The polish is real but the soundness debt now visible is real too.

Quick recap of why §3.3 is at 80:

- Variable-isolation experimental design enforced consistently across both backbones.
- BOLT pipeline documented to production-engineering standard.
- Architectural evolution (G0 → G1 → G2 → G3) shows what failed and why, generation by generation.
- Mathematical validation of energy claims (±0.01% internal consistency).
- Reactive scalability regression analysis (R² = 0.7514) is a novel and well-grounded interpretation.
- The `chapter_4R/arch_progression.tex` section directly addresses supervisor priority #3.
- §4.4 efficiency landscape table has the Dataset (Task) column + separator row + dagger footnote on mAP/mJ + three explicit asymmetry callouts in prose.

### Strengths

- Variable-isolation principle enforced and explicitly stated.
- BOLT pipeline documented to a production-engineering standard.
- Architectural evolution shows what failed and why.
- Mathematical validation of energy claims (±0.01%).
- Reactive scalability regression analysis.
- Comparative efficiency landscape methodologically honest about its asymmetries.
- **New today**: math notation typography correct (FLOPs/SOPs upright); unit error fixed in §3.7.5; typography bug fixed in §3.7.6 title.
- **New today**: §3.7.7 metric list count corrected (4 → 5).

### Areas for Improvement

(Most carry over from `6c5d407`, plus newly-visible items from today's soundness review.)

1. **Resolve the V_{th} history contradiction** between §3.4 and §3.6 (one must be wrong).
2. **Reconcile training-speedup numbers** between §3.4 (2.3×) and §3.6 (1.8×) — different baselines or genuine inconsistency?
3. **Standardise the recall metric definition.** Currently three different framings (IoU>0.5 vs confidence>0.5 vs ambiguous). The user's proposed SC5 reformulation (`recall at $\mathrm{IoU}=0.5$`) is the right anchor; needs propagating to 5–6 locations.
4. **Either add a Mean Prediction Confidence row to §4R/global_evaluator's table OR rewrite the §3.7.7 metric bullet** to describe what's actually shown (Max/Min). Agent has drafted "Confidence Range (Max/Min)" rewrite; awaiting greenlight.
5. **Replace "Phase 1" with "Generation 1"** in §3.7.7 (leftover from earlier draft).
6. **Decide §3.7.5 LIF formula**: either rewrite to match §2.3's form, or add a "simplified for illustration" note.
7. **Verify the Horowitz CMOS reference** flagged by an existing `\todo`.
8. **`chapter_4R/quantization_error.tex` table column-spec** was fixed in Pass 1 (`|l|c|c|c|` → `|l|c|c|`). ✓ Closed.
9. **The §3.7/latency.tex citation `davies2018loihi`** is still used for the historical "10× lower latency" claim — Loihi 2 may have updated latency numbers worth substituting.
10. **Soften "with a confidence of zero"** in §4R/confidence_calibration L21 to "near zero" or "below 0.01" (Min Confidence is 0.0011, not zero).
11. **"event" → "target"** in §4R/temporal L65 ("two nested bounding boxes being drawn for the same event" — wrong noun).
12. **Apply the §3.2 Cordone-citation removal recommendation** drafted in chat (one-line deletion).

### Path to Outstanding (90+)

1. **Ablation study** for at least one major architectural decision (e.g., remove SE block, remove FRR, swap SEW for vanilla residual). ~1–2 weeks.
2. **A T-sweep experiment** for the quantisation-error analysis. Mathematically the $1/T$ ceiling is testable empirically by running T ∈ {2, 4, 8, 16, 32}.
3. **Hardware-realisation cross-check** with `nvidia-smi` measurements — bridges theoretical to actual.
4. **Multi-seed variance reporting** for the headline metrics — converts point estimates into confidence intervals.

These are the substantive empirical extensions that distinguish Outstanding (90+) from Excellent (80–89).

---

## Section 3.4 — Summary & Conclusions (76/100, weighted 11.40/15)

### Justification

**Unchanged from `6c5d407`.** Chapter 4 has had only minor SPaG fixes since the prior card:

- `outcomes.tex` L13–14: missing-space comma issues fixed.
- `reflection_future.tex` L11: sentence-initial lowercase "utilising" → "Utilising".
- `reflection_future.tex` L56: American "artifact" → "artefact".
- `reflection_future.tex` L60: incorrect adverb-adjective hyphen "manually-relabelled" → "manually relabelled".

These are pure presentation fixes; the §3.4 substantive judgement is unchanged.

The Outcomes section walks through Global Precision Parity, Decisive Efficiency Gains, Temporal Reliability and Sharpening, Real-Time Viability, and the Success Criteria Validation table. SC2 row correctly cites *"$76.21\%$ extrapolated on Intel Loihi 2"*. Critical Reflection identifies four substantive limitations with specificity; future-work directions are technically specific.

### Strengths

- SC validation table closes the loop on every criterion from Chapter 1.
- Four limitations are substantive and individually actionable.
- Future-work directions technically specific (Loihi 2, TTFS, ROC, CARLA, adaptive timestepping).
- Honest about hardware-mismatch penalties and dataset choice trade-offs.
- Mature framing of the detection-head-mismatch as a *"deliberate methodological constraint"*.

### Areas for Improvement

(Largely unchanged from `6c5d407`.)

- Acknowledge *"Hunting Behaviour"* alongside *"Bounding Box Sharpening"* in the conclusion's outcomes summary.
- Qualify *"immediate viability"* with the GPU-hardware caveat.
- Tighten the CARLA future-work item with a specific testable success metric.
- If the SC5 reformulation lands, propagate the recall wording in the SC outcomes table (`outcomes.tex:39`).

### Path to Outstanding (90+)

(Unchanged from `6c5d407`.) A definitive overall conclusion sentence; falsifiable success metrics for each future-work item; a "what could not be concluded" section; tight balance acknowledging both temporal-integration phenomena; and a forward-looking "what would convince a sceptic" closing.

---

## Section 3.5 — Presentation, Structure & Language (81/100, weighted 8.10/10)

### Justification

Score nudged from 76 to 81 — the largest single-section jump this round. Three full SPaG passes plus math-notation typography polish have substantially cleaned the presentation. The headline counts:

- **Pass 1**: 40 + 1 bonus + 1 user-rephrase = 42 fixes
- **Pass 2**: 35 of 40 approved items applied (3 user-skipped, 1 audit-misread dropped)
- **Pass 3**: 22 of 22 approved items applied (3 user-skipped)
- **Math typography**: 6 math-mode `FLOPs_l` / `SOPs_l` instances wrapped in `\mathrm{}`
- **User micro-edits**: 2 (§3.7.4 "spike", §3.6.4 "Concurrently" → "also")

**Total: ~99 individual presentation/grammar/typography improvements.** Many addressed items the `6c5d407` card explicitly flagged:

- *"Backpropgation"* typo (`abbreviations.tex` L37) ✓ Fixed
- Missing-space commas in `outcomes.tex` L13–14 ✓ Fixed
- `chapter_4R/quantization_error.tex` table column-spec mismatch ✓ Fixed

Other notable presentation improvements:

- All American-→-British spelling inconsistencies corrected (`localization`/`analyze`/`synthesizing`/`artifact`/`organize`/`synchronization`).
- Closing-backtick errors corrected systematically (`` ``Windowing`` `` → `` ``Windowing'' ``, `` ``objectness`` ``, `` ``Squeeze`` ``, `` ``Excitation`` ``, `` ``Architectural Parity`` ``).
- Em-dash typography standardised (en-dash and single-hyphen instances corrected to em-dash where appropriate).
- Math-mode unit notation standardised (`100ms` → `100\,ms`, `\mu J` → `\mu\text{J}`, `0.9pJ` → `0.9\,\text{pJ}`).
- Glossary discipline tightened (`SNN` → `\gls{snn}`, `CPU` → `\gls{cpu}`, `FPS` → `\gls{fps}` in body prose; `$IoU$` → `$\mathrm{IoU}$` in math).
- Article corrections (`a \gls{ac}` → `an \gls{ac}`; `a 11.73M` → `an 11.73M`).
- Oxford commas added in lists.
- Stray TODO comments removed.
- Subject–verb agreement fixed.
- Several broken sentences rewritten (notably the `$E_{SNN}$ replaces $E_{AC}$ for $E_{chip}$` reorder in §3.7.6).
- Math typography: `\mathrm{}` on multi-letter acronyms, exclusive `[0,∞)` interval notation, fixed closing-paren bugs.

The report now *reads* substantially more polished. After three passes the §3.5 mark sits firmly in the Excellent (80–89) band — meeting the rubric criterion of *"not many occasions when the layout and formatting causes annoyance to the reader"*.

**Remaining presentation issues** (carrying over from prior cards, plus newly-visible from today's soundness review):

- §2.7 still text-only (carry-over).
- The §1.6 Report Structure paragraph is still factually wrong about chapter organisation (drafted rewrite pending).
- The shortened title agreed in screencast-side discussions hasn't been applied — `report.tex` line 73 still uses the long subtitle.
- Orphan `\newacronym{ece}` in `abbreviations.tex:35` (now unused after §1.5 fix).
- Three discussions in flight from today: SC5 reformulation, Mean→Range confidence bullet rewrite, word-count reduction proposals (12 candidates, ~177 words available).
- A handful of small word-choice items from the soundness review (§4R/confidence_calibration "with a confidence of zero" hyperbole; §4R/temporal "event" should be "target").

### Strengths

- **~99 SPaG fixes applied this round in three coordinated passes** — every clearly-defensible mechanical issue identified in three full re-reads has been resolved.
- Math typography: `\mathrm{}` on multi-letter acronyms (FLOPs/SOPs), correct interval notation, fixed typography bugs, standardised unit spacing.
- Glossary integration thorough; `\gls{}` macros consistently used in body prose.
- Bibliography consistently formatted (numeric BibLaTeX with `sorting=nty`).
- Appendix hyperparameter tables detailed and complete.
- Figures (where present) have short titles for the list of figures.
- All `\todo` notes correctly suppressed in PDF.
- Tables consistently styled across the project (`tabularx` + raggedright + hlines).
- All matplotlib visuals share a serif-font visual family (surrogate gradient, arch progression, MAC vs AC).
- SVG rendering issues addressed in prior pass (`∈` no longer renders as tofu, SNN ONLY badges centred).

### Areas for Improvement (priority order)

1. **Apply the §1.6 Report Structure rewrite** (drafted in chat; ~134 words; reflects the new four-chapter layout). Closes the largest remaining structural-claim issue.
2. **Apply the SC5 reformulation across 5–6 locations** (drafted; awaiting greenlight). Closes a metric-definition inconsistency.
3. **Apply the "Confidence Range (Max/Min)" bullet rewrite for §3.7.7** (drafted; awaiting greenlight). Closes the metric-promised-but-not-reported inconsistency.
4. **Apply word-count cuts** — user has 12 candidates totalling ~177 words; just need to pick which subset.
5. **Add a §2.7 figure** (SNN-detector landscape scatter) to close the diagram-coverage gap completely.
6. **Decide on the title** — apply the shortened subtitle to `report.tex` line 73 or commit to the long version.
7. **Delete orphan ECE acronym** from `abbreviations.tex:35`.
8. **Apply the `[h]` → `[H]` swap to `fig:constant_target_bias`** preventively (matches what was done for the G1 super-box figure).

### Path to Outstanding (90+)

To push beyond 81 toward Outstanding:

1. **Zero remaining typographical issues** — even the small ones (orphan acronym, in-flight pending items).
2. **Diagrams everywhere they earn their place** — close §2.7 figure gap.
3. **Consistent terminology throughout** — particularly the recall metric definition (currently three framings).
4. **Complete glossary** — drop unused entries; ensure every defined acronym is actually referenced.
5. **High-standard mathematics typesetting** — math notation polish is now done for FLOPs/SOPs/IoU; would benefit from one more pass on remaining math-mode unit spacing.

---

## Soundness Review Findings (NEW this round)

A focused soundness/correctness review surfaced 12 substantive findings. These are factual, definitional, mathematical, or structural issues — not pure SPaG. Most pre-existed the SPaG passes; the review just made them visible.

**A. Factual / numerical inconsistencies (highest concern):**

1. **`V_{th}` history contradiction**: §3.4 says earlier $V_{th} = 0.3$ silenced the network; §3.6 says the threshold was lowered $V_{th} = 0.5 \rightarrow 0.2$. Cannot both be correct.
2. **Training-speedup numbers don't reconcile**: §3.4 says step_mode='m' gave 16h → 7h (~2.3×); §3.6 says step_mode + AMP combined gives ~1.8×. Different baselines or genuine inconsistency?

**B. Internal definition / metric inconsistencies:**

3. **Recall metric defined three different ways**: SC5 (IoU>0.5), §3.7.7 metric description (confidence threshold of 50%), §4R table caption ("Detections > 0.5"). User's proposed SC5 reformulation would standardise.
4. **"Mean Prediction Confidence" promised in §3.7.7 but not reported**: §4R table shows Max/Min Confidence rows instead of Mean.
5. **§3.7.7 references "Phase 1 ambiguity problem"** — but the project uses Generations G0/G1/G2/G3, no "Phase" defined.
6. **"Mean/Median IoU" promised in §3.7 parent, only Mean reported** in §4R table.

**C. Methodological / mathematical issues:**

7. **§3.7.5 (latency) LIF formula not algebraically identical to §2.3 main formula**. Different placement of the $1/\tau$ factor on the input term.
8. **Orphaned `ECE` glossary entry** (now unused after §1.5 fix; should be deleted from `abbreviations.tex:35`).

**D. Smaller soundness items:**

9. **§4R/confidence_calibration L21**: hyperbolic "with a confidence of zero" — Min Confidence is 0.0011, not zero.
10. **§4R/temporal L65**: "two nested bounding boxes being drawn for the same event" — wrong noun in object-detection context.

**Numerical sanity check (PASSED ✓)**: All 18 headline numbers verified to compute correctly (parity ratios, energy savings, ops reduction, layer-wise FLOPs/SOPs sums, Loihi 2/TrueNorth/A100 derivations, generation gain pp values, FPS thresholds, P99-above-mean ratio, mean firing rate across 9 layers, highway speed conversion, spatial cell counts, parameter delta).

**Net verdict**: Most findings are minor or fixable in <5 minutes. The two factual contradictions (V_{th}, training speedup) are the highest concern — either numbers are wrong somewhere, or the prose obscures a real distinction the reader can't follow. Worth resolving before submission.

---

## Overall Observations

**What changed since `6c5d407`, what stayed:**

| Item | Status change | Net mark impact |
|---|---|---|
| §1.5 ECE methodology fix applied (was the prior card's flagged issue) | Closes the §3.1 methodological-accuracy callout | §3.1 79 → 80 (+0.15 weighted) |
| §1.6 partial alignment (matches §2.6 title; hyphen fix) | Closes a small §3.1 / §3.5 issue | included in §3.1 lift |
| §3.7.5 unit error `33 ms⁻¹` → `33 m s⁻¹` | Substantive fix | included in §3.3 unchanged |
| §3.7.6 typography bug `($E_{chip})$` | Cosmetic but real | included in §3.5 lift |
| §3.7.7 "four metrics" → "five metrics" count fix | Definitional accuracy | included in §3.3 unchanged |
| Math notation polish (FLOPs/SOPs `\mathrm{}` ×6) | Typographic correctness | included in §3.5 lift |
| ~92 SPaG fixes across all chapters (Passes 1, 2, 3) | Substantial polish | §3.5 76 → 81 (+0.50 weighted) |
| User micro-edits (§3.7.4 "spike", §3.6.4 "also") | Tightens prose | included in §3.5 lift |
| Soundness review surfaces 12 issues | New visibility, no score impact (issues pre-existed) | offset against §3.3 polish gain |
| §1.4 SC literature anchoring (drafted, not applied) | Still pending | Would lift §3.1 80 → 84 if applied |
| §1.6 full rewrite (drafted, not applied) | Still pending | Would lift §3.1 + §3.5 |
| SC5 reformulation across 5–6 locations (drafted, not applied) | New in-flight item | Would close definitional issue |
| §3.7.7 confidence-bullet rewrite (drafted, not applied) | New in-flight item | Would close metric-mismatch issue |
| §2.7 figure (still planned) | Discussed; data partially available | Would lift §3.2 76 → 78 if built |

**Net: +1 mark (~78 → ~79).** Driven primarily by §3.5 polish (76 → 81) and §3.1 substantive fix (79 → 80). The soundness review didn't materially affect scoring because the issues pre-existed; it just makes them more visible to future review.

**The four most consequential remaining improvements before final submission, in priority order:**

1. **Apply the §1.4 SC literature-anchoring** (drafted across multiple sessions). Estimated lift: §3.1 80 → 84 = **+0.6 weighted marks**.
2. **Resolve the V_{th} and training-speedup contradictions** (Soundness #1, #2). Reduces §3.3 risk from a careful examiner; doesn't necessarily lift the score but de-risks it.
3. **Apply the §1.6 + SC5 + Confidence Range drafted edits** (~30–60 min of edit work). Combined lift: ~+0.4 weighted marks.
4. **Add the §2.7 figure** (SNN-detector landscape scatter). Estimated lift: §3.2 76 → 78 = **+0.5 weighted marks**.

If all four are addressed, the projected band moves from ~79 to **~81 (mid-First)**. The substance is already there; the structural and consistency refinements would let it land properly.

---

## Cross-Cutting Path to Outstanding (90+)

**High impact, low-to-moderate effort (the closeable items):**

1. **Apply the §1.4 SC literature-anchoring** (drafted; ~30 min of edit work). Lifts §3.1.
2. **Resolve V_{th} + training-speedup contradictions** (~15 min; needs user clarification of correct values).
3. **Add §2.7 background figure** (~1–2 hours; data mostly already to hand). Lifts §3.2.
4. **Apply the §1.6 + SC5 + Confidence Range drafted edits** (~30–60 min). Lifts §3.1 + §3.3 + §3.5.
5. **Apply word-count cuts** (~30 min; user picks subset of 12 candidates).
6. **Replace "Phase 1" → "Generation 1"; delete orphan ECE acronym** (~5 min).

Combined: **~3–4 hours of focused work** would lift the overall to ~81–82.

**High impact, high effort (the Outstanding-tier additions):**

7. **One ablation experiment** (~1–2 weeks). §3.3 80 → 85.
8. **One T-sweep experiment** (~1–2 weeks). §3.3 80 → 85.
9. **Multi-seed variance reporting** (~3–5 days of training compute + analysis). §3.3 toward 85.

**Moderate impact, low effort:**

10. **Literature-derive the success criteria** beyond per-SC citations — explicit one-sentence justification of *why* each chosen threshold was set at that level. Lifts §3.1.
11. **Articulate relevance per cited work** in Background. Each major citation tied to a specific DetectorNX choice. Lifts §3.2.
12. **A definitive overall conclusion sentence** in Chapter 4 closer. Lifts §3.4.
13. **Falsifiable success metrics for each future-work item.** Lifts §3.4.
14. **Final proofread pass** for any residual typographical issues introduced by the in-flight edits.

**Realistic target:**

For a BSc dissertation, the report has now meaningfully entered the comfortable First range (~79). With items 1–6 above (~3–4 hours), it should land at ~81–82. With items 7–9 (~1–2 weeks each), individual sections could push toward Outstanding territory. Hitting 90+ overall requires both substantively novel results (which this project arguably has — variable-isolated comparison protocol + scale-stable quantisation finding + implicit-uncertainty-sensor finding) AND publication-quality presentation. The substance is there; items 1–9 above would close most of the remaining gap.

**Effort budget:**

- Closeable items (1–6): ~3–4 hours total. Lifts to ~81–82.
- Adding any one of the empirical extensions (7–9): ~1–2 weeks each.
- Full Outstanding-tier polish: ~4–6 weeks of full-time work.

If submission is imminent, items 1–6 are the right focus.

---

## Four-Card Trajectory (cc59984 → 291f93d → 6c5d407 → a3d5a11)

| Section | cc59984 (2026-04-30) | 291f93d (2026-05-03 a.m.) | 6c5d407 (2026-05-03 p.m.) | a3d5a11 (2026-05-04) | Δ this round |
|---|---|---|---|---|---|
| 3.1 Abstract & Introduction | 78 | 78 | 79 | **80** | +1 |
| 3.2 Background & Theory | 65 | 75 | 76 | **76** | 0 |
| 3.3 Technical Quality | 75 | 80 | 80 | **80** | 0 |
| 3.4 Summary & Conclusions | 75 | 76 | 76 | **76** | 0 |
| 3.5 Presentation | 62 | 75 | 76 | **81** | +5 |
| **Overall** | **72** | **77** | **78** | **~79** | **+1** |

**Pattern:** The early-trajectory gains came from substantive changes (results restructure, G1/G2/G3 evidence section, background figures, MAC vs AC figure, lit-anchoring of §1.5 metrics). This round's gain comes almost entirely from §3.5 polish — three SPaG passes addressing every clearly-defensible mechanical issue across all chapters — plus a substantive methodological-accuracy fix in §1.5 (ECE → reliability-diagram-based) that was a prior-card callout.

**Plateau warning:** The next +1 mark won't come from further SPaG. It will require either (a) the drafted-but-not-applied items landing (§1.4 SC anchoring, §1.6 full rewrite, SC5 reformulation across 5–6 locations, Confidence Range bullet, §3.2 Cordone removal — all together ~+1.5 weighted) or (b) the §2.7 figure being built (~+0.5 weighted) or (c) substantive empirical extensions (multi-week work). Polish alone has now run out of headroom in the supervisor-calibrated marking.

---

*Card generated 2026-05-04 10:27. Three full report re-reads were performed earlier today; the agent's state at scoring reflects the report after all three SPaG passes + math-notation polish + user micro-edits + the soundness review. No new substantive content has been added since 6c5d407; today's progression is consolidation, polish, and consistency.*
