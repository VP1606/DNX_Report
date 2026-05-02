# DetectorNX Screencast — Full Script

**Total runtime:** 8:35 (within 7-9 min rubric band)
**Beat order:** Title → Motivation+ADAS Demo → SNN Introduction → Aims+Roadmap → Approach → Results → Calibration → Conclusion

```
═══════════════════════════════════════════════════════════════
  TIMING SUMMARY
═══════════════════════════════════════════════════════════════
  Beat 1 — Title intro                  0:00 – 0:18  (~18 sec)
  Beat 2 — Motivation + ADAS Demo       0:18 – 1:30  (~72 sec)
  Beat 3 — SNN Introduction             1:30 – 2:30  (~60 sec)
  Beat 4 — Aims + Roadmap               2:30 – 3:20  (~50 sec)
  Beat 5 — Approach                     3:20 – 4:10  (~50 sec)
  Beat 6 — Results                      4:10 – 6:20  (~130 sec)
  Beat 7 — Calibration finding          6:20 – 7:20  (~60 sec)
  Beat 8 — Conclusion + Future Work     7:20 – 8:35  (~75 sec)
                                              Total: 8:35
═══════════════════════════════════════════════════════════════
```

---

## Beat 1: Title Intro

```
═══════════════════════════════════════════════════════════════
  BEAT 1 — TITLE INTRO (0:00 – 0:18, ~18 sec)
═══════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│ [0:00 – 0:18]  SUB-BEAT 1A: TITLE + CONTEXT  (~18 sec)      │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE:** Title card.
- Centre: "DetectorNX" in large type
- Below: "Premakantha Varun"
- Footer: "BSc Computer Science · University of Manchester · 2026"
- Bottom-right: university logo

**VOICEOVER:**

> "Hi, I'm Varun. This is my third-year project, DetectorNX — investigating the viability of spiking neural networks for advanced driver-assistance systems, through a strictly-controlled comparison against an equivalent CNN baseline on automotive vehicle detection."

(40 words / ~18 sec)

---

## Beat 2: Motivation + ADAS Demo

```
═══════════════════════════════════════════════════════════════
  BEAT 2 — MOTIVATION + ADAS DEMO (0:18 – 1:30, ~72 sec)
═══════════════════════════════════════════════════════════════

NARRATIVE: Ground the project in real-world ADAS in action
before posing the project's questions. Open with a visceral
auto-brake demonstration; explain what ADAS is and why it
matters; close with the technical challenge that drives the
project.

┌─────────────────────────────────────────────────────────────┐
│ [0:18 – 0:35]  SUB-BEAT 2A: ADAS DEMONSTRATION  (~17 sec)   │
└─────────────────────────────────────────────────────────────┘
```

**VISUAL TIMELINE:**

| Time | What's on screen |
|---|---|
| 0:18 – 0:21 | Quick transition from title to driving footage (1 sec wipe / dissolve). |
| 0:21 – 0:30 | **ADAS demo footage.** Your car driving forward. Dashboard ADAS interface visible (or in inset). An obstacle/vehicle appears in path. Auto-braking activates — visible as ADAS warning indicator lighting up + slight deceleration. |
| 0:30 – 0:35 | Hold on the moment of intervention. Slow-mo on the brake-warning light or the indicator on the dash. |

**VOICEOVER:**

> "What you're watching is an Advanced Driver-Assistance System — ADAS — in action. The car has detected an obstacle in its path and informed me through the alert. If I didn't notiice this, or the car in front brakes hard, it would apply the brakes automatically. Faster than I could react."

(28 words / ~14 sec)

**Voice direction:**
- Open with "What you're watching is..." — invites the marker to lean in. Standard documentary opening device.
- Slight pause after "in action."
- Emphasis on "automatically" and "faster than I could react".

**Music character:** Continues from intro (calm pad). Holds.

```
┌─────────────────────────────────────────────────────────────┐
│ [0:35 – 0:55]  SUB-BEAT 2B: WHAT ADAS DOES  (~20 sec)       │
└─────────────────────────────────────────────────────────────┘
```

**VISUAL TIMELINE:**

| Time | What's on screen |
|---|---|
| 0:35 – 0:42 | **Cutaway to driving footage** showing different ADAS scenarios — pedestrian crossing, cyclist passing, vehicle merging. Brief overlay text appearing as you list them: *"Pedestrians · Cyclists · Lane keeping · Adaptive cruise"* |
| 0:42 – 0:50 | Cut to **regulatory-context graphic** — could be a stylised Euro NCAP-style chart, or text appearing: *"By 2026 — mandatory in every new vehicle"* with brief footage backdrop. |
| 0:50 – 0:55 | Hold on a wide driving shot. |

**VOICEOVER:**

> "ADAS systems handle pedestrians at junctions, cyclists in blind spots, lane keeping, adaptive cruise — the kinds of perception we used to leave entirely to human attention. By 2026, regulators want every new vehicle to handle these scenarios reliably, at speeds up to 130 kilometres per hour."

(46 words / ~21 sec)

**Voice direction:**
- "ADAS systems handle..." — list rhythm, slight pause between items.
- Emphasis on "By 2026", "every new vehicle", "130 kilometres per hour".

**Music character:** Music begins to add texture — a subtle rhythmic element. Tension building toward the technical challenge.

```
┌─────────────────────────────────────────────────────────────┐
│ [0:55 – 1:30]  SUB-BEAT 2C: THE TECHNICAL CHALLENGE (~35s)  │
└─────────────────────────────────────────────────────────────┘
```

**VISUAL TIMELINE:**

| Time | What's on screen |
|---|---|
| 0:55 – 1:05 | **Animated CNN inference graphic** (Manim — `cnn_inference.py`). Event-camera frame in, five conv blocks fade in across the middle, activation pulse cascades left → right, output frame on the right gets bounding boxes (`car 0.94`, `ped 0.81`), FLOP counter at the bottom ticks up to *"9.22 G-FLOPs · per frame"*. |
| 1:05 – 1:18 | **Trajectory graph** (Manim — `trajectory_graph.py`). Compute demand vs. industry power target, 2015 → 2030. Three markers: Conventional ECU (< 50 W), L3 self-driving (200–350 W), L4 autonomy (~1000 W). Green budget line at 200 W. Red exponential compute-demand curve overshoots the budget around the L3 marker. |
| 1:18 – 1:30 | Graph holds. Final visual cue: an arrow drops DOWN from the L4 dot toward the budget line, with a large "?" beneath it — gesturing "how do we bring this back into budget?" — anticipation handed straight to Beat 3 (SNN Introduction). |

**VOICEOVER:**

> "Modern ADAS runs on dense convolutional neural networks — about 9 G-FLOPs per frame, billions of multiply-accumulates, just to perceive the road. The problem is the budget. A conventional engine-control unit draws under 50 watts. The industry's target for an onboard perception ECU sits around 200 watts. But Level-3 self-driving systems already need 200 to 350 — and Level-4 projections push past 1000. The compute demand isn't just rising — it's overshooting the budget."

(80 words / ~36 sec)

**Voice direction:**
- Build tension through this beat.
- Slight pause at "The problem is the budget." — the pivot moment.
- List rhythm on the watt numbers: "under 50… around 200… 200 to 350… past 1000."
- Emphasis on "overshooting the budget" — this is the line that the trajectory "?" answers.

**Music character:** Music builds. Tension peaks at "overshooting the budget". Holds at the visual "?" — anticipation handed off to Beat 3 (SNN Introduction).

---

## Beat 3: SNN Introduction

```
═══════════════════════════════════════════════════════════════
  BEAT 3 — SNN INTRODUCTION (1:30 – 2:30, ~60 sec)
═══════════════════════════════════════════════════════════════

NARRATIVE: Answer the "how do we bring this down?" question
posed by Beat 2's trajectory graph. Introduce the spiking
paradigm as the project's response — first the single-neuron
mechanic, then network-level sparsity — then immediately
flag the catch (one-bit quantisation) that frames why this
project exists at all.

┌─────────────────────────────────────────────────────────────┐
│ [1:30 – 2:15]  SUB-BEAT 3A: SPIKING NEURON + SPARSITY       │
│                                                  (~45 sec)  │
└─────────────────────────────────────────────────────────────┘
```

**VISUAL TIMELINE:**

| Time | What's on screen |
|---|---|
| 1:30 – 1:35 | Bridge transition — the trajectory "?" dissolves; brief title-card flash *"Spiking Neural Networks"* (or direct cut into the LIF animation if you'd rather skip the card). |
| 1:35 – 1:55 | **LIF-neuron animation** (Manim — `lif_neuron.py`, 19.8 s). Soma + four input synapses on the left; membrane-potential trace on the right rises step-by-step with each input spike, leaks between inputs, crosses a dashed yellow threshold, the soma flashes yellow, an output tick lands on the train below, and the trace resets to zero. Cycle plays out twice. Closing caption: *"spike → reset → repeat"*. |
| 1:55 – 2:15 | **Sparsity visualisation** (Manim — `sparsity_grid.py`). Side-by-side grids: CNN-style with continuously-coloured cells (counter: *100% active each frame*) versus SNN-style with mostly-black cells and occasional white spike flashes (counter: *~5–8% active each frame*). Closing card: *"no spike → no computation → no power"*. |

**VOICEOVER (1:30 – 1:35, bridge, ~5 sec):**

> "To answer that question, DetectorNX turns to spiking neural networks."

(11 words / ~5 sec)

**VOICEOVER (1:35 – 1:55, LIF animation slot, ~18 sec spoken in a 20-sec slot):**

> "Unlike a CNN — where every neuron fires every cycle — a spiking neuron stays silent. It integrates input until that input crosses a threshold. Then it fires a single discrete spike, and resets."

(32 words / ~16 sec spoken; the remaining ~4 sec accommodates emphasis pauses on the key words below)

**Word-to-visual alignment** (animation runs 19.8 s, fires at ~10.2 s and ~15.5 s of animation time):

- "stays silent" — opens the first integration phase on screen (trace climbing under the threshold).
- *"threshold"* — lands on the first fire (the trace pierces the yellow line at ~10.2 s and the soma flashes yellow). Pause briefly after.
- *"spike"* — lands on the second fire at ~15.5 s. Punctuated, sharp.
- *"and resets"* — lands as the trace drops vertically back to zero immediately after the second fire, bridging into the closing caption *"spike → reset → repeat"* that fades up at ~17.2 s.

**VOICEOVER (1:55 – 2:15, sparsity-grid slot, ~22 sec):**

> "The entire network communicates through these sparse binary events. In a typical scene, ninety to ninety-five percent of neurons stay quiet at any given moment. And here's the key: no spike means no computation. The hardware skips the multiply-accumulate entirely."

(47 words / ~22 sec — may be tightened once `sparsity_grid.py` is built and its precise event timing is known)

**Voice direction:**
- Bridge "To answer that question" — direct callback to the on-screen "?" at the end of Beat 2. The phrasing is deliberate.
- "DetectorNX turns to spiking neural networks" — first re-anchor of the project name since the title slide. Land it.
- LIF voiceover: emphasise "threshold", "spike", and "resets" so they land on the visual fire/reset events (alignment notes above).
- Drive to the punchline: "no spike means no computation."

*Author's alternative wording (kept as a fallback): "To attempt to reduce the power draw, this project turns to spiking neural networks: [introduction]." Slightly more hedged but preserves the same structural beat.*

*Author's original LIF wording (kept as a fallback if the tightened version above feels too sparse): "Unlike conventional CNNs — where every neuron fires a continuous activation every cycle — a spiking neuron stays silent until its input crosses a threshold. Then it fires a single discrete spike, and resets."*

**Music character:** Resolves into something quieter and more mechanical — the "answer arriving" feel. Not triumphant yet — just clean.

```
┌─────────────────────────────────────────────────────────────┐
│ [2:15 – 2:30]  SUB-BEAT 3B: THE CATCH  (~15 sec)            │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** Quantisation diagram.
- A smooth continuous activation curve vs. a 1-bit binary spike train at the same timestamps.
- Caption underneath: *"32-bit continuous → 1-bit spike"*
- Brief on-screen text: *"How much does this cost?"*

**VOICEOVER:**

> "But there's a catch. A spike is binary — it either fires or it doesn't — so every signal gets quantised to one bit. The question is, how much does that actually cost?"

(32 words / ~14 sec)

**Voice direction:**
- Tonal shift on "But there's a catch." — slight slow, eyebrow-raise.
- "How much does that actually cost?" — the question that hands off to Beat 4 (Aims).

---

## Beat 4: Aims + Roadmap

```
═══════════════════════════════════════════════════════════════
  BEAT 4 — AIMS + ROADMAP (2:30 – 3:20, ~50 sec)
═══════════════════════════════════════════════════════════════

NARRATIVE: With the SNN paradigm just introduced and its
one-bit trade-off acknowledged, state the project's two
core questions and lay out the roadmap for what's to come.

┌─────────────────────────────────────────────────────────────┐
│ [2:30 – 2:50]  SUB-BEAT 4A: AIMS  (~20 sec)                 │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE:** Two questions, fading in sequentially as spoken.
- Q1: "Is the spiking paradigm viable for automotive-grade perception?"
- Q2: "What does it cost?"
- (Both stay on screen at the end of the sub-beat.)

**VOICEOVER:**

> "Two questions, then. First — is the spiking paradigm actually viable for safety-critical automotive perception? And second — under conditions tight enough to attribute every percentage point of difference to the spiking mechanism alone, what does it cost?"

(40 words / ~18 sec)

```
┌─────────────────────────────────────────────────────────────┐
│ [2:50 – 3:20]  SUB-BEAT 4B: ROADMAP  (~30 sec)              │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE:** Vertical numbered list, each item highlighted/lit as you say it (subtle accent-colour fade, not bouncing).
1. Method
2. Results
3. Calibration finding
4. What's next

**VOICEOVER:**

> "From here, four things: how DetectorNX isolates the spiking mechanism through strict architectural parity; our headline results, including a 94 percent energy saving alongside full precision parity; an unexpected finding about confidence calibration that's safety-relevant for advanced driver-assistance systems; and finally, the open question of how this generalises beyond automotive vehicle detection."

(55 words / ~26 sec)

---

## Beat 5: Approach

```
═══════════════════════════════════════════════════════════════
  BEAT 5 — APPROACH (3:20 – 4:10, ~50 sec)
═══════════════════════════════════════════════════════════════

NARRATIVE: With the spiking paradigm now introduced (Beat 3)
and the project's two questions on the table (Beat 4), this
beat shows HOW DetectorNX answers them — through strict
architectural parity between the SNN and CNN variants.

┌─────────────────────────────────────────────────────────────┐
│ [3:20 – 3:45]  SUB-BEAT 5A: METHODOLOGY  (~25 sec)          │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** Two backbones side-by-side, structurally identical (same block shapes, same connections). The only visual difference: the residual blocks are coloured green (SNN, SEWResBlock) on the left, purple (CNN, ResBlock) on the right. Identical preprocessing pipeline above; identical regression head below.
- Bottom-left tag: "11.72 M params" / "11.73 M params"

**VOICEOVER:**

> "To answer that, we built two object detectors with strict architectural parity. Same backbone shape, same parameter count, same training hyperparameters, same data. The only thing that changes between them is whether the activations are continuous or spiking — which means any performance difference we measure is attributable to the spiking mechanism alone."

(55 words / ~25 sec)

```
┌─────────────────────────────────────────────────────────────┐
│ [3:45 – 4:10]  SUB-BEAT 5B: THE ARTEFACTS  (~25 sec)        │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** The full high-level architecture diagram (the SVG — green SNN backbone, purple CNN backbone, preprocessing pipeline above, regression head and evaluation suite below). It lands on the slide all at once and stays for the duration of the sub-beat.
- Below the diagram, an ETraM sample frame appears with a caption: *"ETraM event-camera dataset — Verma et al., 2024"*

**VOICEOVER:**

> "That's DetectorNX. The spiking variant — DetectorNX-G3-SNN — and its continuous twin — DetectorNX-G3-CNN. Both at 11.7 million parameters. Both trained on the ETraM event-camera dataset, which captures real urban traffic from a static roadside camera. To our knowledge, this is the first directly-trained spiking detector evaluated on ETraM."

(50 words / ~23 sec)

---

## Beat 6: Results

```
═══════════════════════════════════════════════════════════════
  BEAT 6 — RESULTS (4:10 – 6:20, ~130 sec)
═══════════════════════════════════════════════════════════════

DEMO-DRIVEN STRUCTURE: The live SNN+CNN parallel demo runs as
the visual backbone for the entire beat. Voiceover narrates and
interprets while the demo plays. Numerical overlays focus
attention on different metrics in each sub-beat.

Demo layout suggested:
  ┌──────────────────────────────────────────────────────┐
  │  [SNN inference @ ETraM scene]   │  [CNN inference]   │
  │   bounding boxes overlaid        │   bounding boxes   │
  │                                  │                    │
  │   Power: 2.4 mJ/frame            │   Power: 42.4 mJ   │
  │   FPS:   259.80                  │   FPS:   1402.60   │
  │   mIoU:  0.461                   │   mIoU:  0.486     │
  └──────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ [4:10 – 4:47]  SUB-BEAT 6A: PRECISION PARITY  (~37 sec)     │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** Demo running. Highlight the mIoU readouts at the bottom of each pane. Briefly overlay text: *"94.9% mIoU parity · 91.3% mAP₅₀ parity · 100% recall (both)"*.

**VOICEOVER:**

> "Let's start with precision. Both models are running here in parallel on the same ETraM scene — bounding boxes overlaid in real time. The spiking variant reaches 94.9% mIoU parity against the continuous baseline, and 91.3% on the stricter mAP-at-0.5 IoU metric. And both architectures achieve 100% recall on objects with IoU above 0.5 — every vehicle in the scene is found. The roughly 5-percent precision gap is the measured cost of one-bit quantisation, but the spiking model matches the continuous baseline on detection completeness."

(80 words / ~37 sec)

```
┌─────────────────────────────────────────────────────────────┐
│ [4:47 – 5:35]  SUB-BEAT 6B: EFFICIENCY  (~48 sec)           │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** Demo continues. Power readouts now highlighted. Toward the end of the sub-beat, a small inset graph appears in the corner showing energy-vs-event-count with the linear fit (R² = 0.7514) — the "Reactive Scalability" plot.

**VOICEOVER:**

> "Now efficiency. Watch the power readout under each model. The SNN consumes around 2.4 millijoules per frame, against 42.4 for the CNN — a 94.33% reduction in per-frame energy. But there's something more interesting going on. The SNN's energy scales with the activity in the scene. As the traffic gets denser, the spiking model's energy rises proportionally — what we call Reactive Scalability, with an R-squared of 0.7514. The CNN, in contrast, consumes the same energy whether the road is empty or packed. This is a paradigm-level efficiency property that doesn't exist on continuous architectures."

(105 words / ~48 sec)

```
┌─────────────────────────────────────────────────────────────┐
│ [5:35 – 6:20]  SUB-BEAT 6C: REAL-TIME + BRIDGE  (~45 sec)   │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** Demo continues. FPS readouts now highlighted. Toward the end, the SC validation table appears briefly (small, summarised — six items with green ticks), then fades to a transitional black or simple text:
*"...one of those criteria produced a result we didn't expect."*

**VOICEOVER:**

> "And speed. The SNN sustains 259.80 frames per second on GPU hardware — an 8.6× safety margin over the 30-FPS threshold considered the minimum for real-time automotive perception. Across all six pre-defined success criteria — precision parity, energy efficiency, real-time throughput, parameter parity, detection completeness, and confidence calibration — DetectorNX passes every single one. But one of those criteria produced a result we didn't expect."

(75 words / ~35 sec)

---

## Beat 7: Calibration Finding

```
═══════════════════════════════════════════════════════════════
  BEAT 7 — THE UNEXPECTED FINDING (6:20 – 7:20, ~60 sec)
═══════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│ [6:20 – 6:38]  SUB-BEAT 7A: THE REVEAL  (~18 sec)           │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** Pick up from Beat 5's transition card. A single full-screen text card appears: *"The 6th criterion: Confidence Calibration"*. Background colour distinct from prior beats — slight visual break to mark the shift to "the unexpected result".

**VOICEOVER:**

> "That sixth criterion was confidence calibration — basically, how well the model's stated certainty about a detection actually tracks how often that detection turns out to be correct. Going in, we expected parity. We got something different."

(40 words / ~18 sec)

```
┌─────────────────────────────────────────────────────────────┐
│ [6:38 – 7:01]  SUB-BEAT 7B: THE EMPIRICAL FINDING  (~23 sec)│
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** The two reliability diagrams from §3.8, side-by-side:
- Left panel — SNN reliability diagram
- Right panel — CNN reliability diagram
- Both axes labelled (x: confidence, y: IoU). Identity line (perfect calibration) shown as dashed.
- Highlight cues:
  - CNN panel: red circle/glow on the cluster of points at HIGH confidence + ZERO IoU (the overconfident hallucinations). Brief callout: *"high confidence, zero overlap"*
  - SNN panel: green circle/glow on the cluster of points at LOW confidence + LOW IoU (correctly suppressed). Brief callout: *"wrong, and knows it"*

**VOICEOVER:**

> "Here's the calibration plot. The CNN, on the right, shows a pronounced overconfidence bias — it routinely assigns high confidence to detections that turn out to have zero overlap with any actual vehicle. The SNN, on the left, doesn't do this. When the spiking model is uncertain, its confidence honestly drops toward zero."

(50 words / ~23 sec)

```
┌─────────────────────────────────────────────────────────────┐
│ [7:01 – 7:20]  SUB-BEAT 7C: WHY IT MATTERS  (~19 sec)       │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** Concept icon — a steering wheel plus an emergency-brake symbol, with a thought-bubble showing the SNN's "honest uncertainty" output rather than a confident hallucination. Or simpler: text card with three lines:
- "Implicit uncertainty sensor"
- "Safety-critical for ADAS"
- "No spurious emergency interventions"

**VOICEOVER:**

> "In other words, the SNN naturally acts as an implicit uncertainty sensor. For ADAS, where over-confident hallucinations could trigger spurious emergency braking, this isn't just a curiosity — it's a safety-critical advantage."

(33 words / ~15 sec)

---

## Beat 8: Conclusion + Future Work

```
═══════════════════════════════════════════════════════════════
  BEAT 8 — TAKEAWAY + FUTURE WORK (7:20 – 8:35, ~75 sec)
═══════════════════════════════════════════════════════════════

NARRATIVE FRAME: "So the takeaways are threefold..." Each
takeaway lands as its own sub-beat with a single big number
on screen, then the future-work close brings everything home.

┌─────────────────────────────────────────────────────────────┐
│ [7:20 – 7:34]  SUB-BEAT 8A: TAKEAWAY 1 — THE LOSS  (~14 s)  │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** Three-item takeaway list appears, with item #1 highlighted/lit:
1. The cost                           ◄ active
2. The benefit
3. The unexpected advantage

Big number anchored beside item #1: *"~5% mIoU"*
Small subtitle below: *"precision cost · variable-isolated"*

**VOICEOVER:**

> "So the takeaways are threefold. First — the cost. Under variable-isolated comparison, the spiking variant loses roughly 5% mIoU against its continuous twin. Measurable, but architecturally tractable."

(30 words / ~14 sec)

```
┌─────────────────────────────────────────────────────────────┐
│ [7:34 – 7:48]  SUB-BEAT 8B: TAKEAWAY 2 — THE BENEFIT (~14s) │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** Item #2 now lit on the same takeaway list.
- Big number anchored beside item #2: *"94% energy reduction"*
- Small subtitle: *"+ reactive scalability"*
- Optional: a small thumbnail of the Reactive Scalability inset graph from Beat 5B.

**VOICEOVER:**

> "Second — the benefit. That precision cost buys you a 94% reduction in per-frame energy, plus reactive scalability — energy that scales with scene activity rather than running flat."

(29 words / ~13 sec)

```
┌─────────────────────────────────────────────────────────────┐
│ [7:48 – 8:03]  SUB-BEAT 8C: TAKEAWAY 3 — THE ADVANTAGE      │
│                                                  (~15 sec)  │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** Item #3 now lit on the takeaway list.
- Big text anchored: *"Implicit uncertainty sensor"*
- Small subtitle: *"safety-critical for ADAS"*
- Optional: thumbnail of the SNN reliability diagram from Beat 6B.

**VOICEOVER:**

> "Third — the unexpected finding. The spiking model exhibits superior confidence calibration at low-confidence regions, naturally acting as an implicit uncertainty sensor — directly safety-relevant for ADAS deployment."

(29 words / ~13 sec)

```
┌─────────────────────────────────────────────────────────────┐
│ [8:03 – 8:35]  SUB-BEAT 8D: WHERE THIS GOES NEXT  (~32 sec) │
└─────────────────────────────────────────────────────────────┘
```

**SLIDE / VISUAL:** Forward-looking visual.
- Top of slide: bold statement card — *"Spiking is viable. Not theoretical. Viable."*
- Below: three future-work directions appearing as bullets:
  - → Multi-class generalisation (single-class COCO subset)
  - → SNN-native classification head
  - → Neuromorphic hardware deployment (Loihi 2)
- Final transition (~ last 4 sec): card fades to closing card with project name, your name, university, "Thanks for watching."

**VOICEOVER:**

> "Together, these results establish the spiking paradigm as a viable — not theoretical — route to safety-critical edge perception. The open question is whether this generalises beyond automotive vehicle detection. That's where this work points next: porting DetectorNX to broader multi-class benchmarks, integrating an SNN-native classification head, and ultimately deploying on real neuromorphic silicon. Thanks for watching."

(60 words / ~28 sec)

---

## Refactor Notes

**v3 changes (current revision):**

- **New Beat 3: SNN Introduction** inserted between Motivation (Beat 2) and Aims (now Beat 4). The SNN reveal sits directly off the trajectory graph's "?", answering it immediately rather than waiting until after Aims+Roadmap.
- **Sub-beat 2C voiceover updated** to use concrete watt numbers (Conventional ECU < 50 W; L3 self-driving 200–350 W; L4 autonomy ~1000 W; industry target ~200 W) — matching the data points rendered in `trajectory_graph.py`.
- **Sub-beat 2C visual timeline updated** to reference the rendered Manim animations (`cnn_inference.py`, `trajectory_graph.py`) and to describe the final arrow as pointing DOWN from the L4 dot toward the budget line.
- **Old Sub-beat 4A "What's an SNN" removed** — its content is now folded into and expanded across new Sub-beat 3A.
- **Old Sub-beat 4B "The catch" moved** verbatim to new Sub-beat 3B — keeps the quantisation hedge tight to the SNN reveal.
- **Old Beat 4 (Approach)** now contains only Methodology and Artefacts (renumbered as 5A and 5B).
- **Beats 5, 6, 7 renumbered to 6, 7, 8** with all time markers shifted by +0:15 to accommodate the longer SNN intro.
- **Sub-beat 4A (Aims) compressed** from 50 → 40 words to keep total runtime inside the rubric band.
- **Sub-beat 4B (Roadmap) compressed** from 73 → 55 words; the "motivation" item was dropped from the list (motivation has already been delivered by the time the roadmap is read).
- **Total runtime: 8:20 → 8:35.** Still inside 7-9 min rubric band.

**v2 changes (previous revision):**

- **New Beat 2** inserted between Title and Aims, replacing the original abstract motivation section. Now opens with a real ADAS auto-braking demonstration to give the marker concrete context before any abstract discussion.
- **Aims and Roadmap** moved from Beat 1 (sub-beats 1B and 1C in the previous version) into a new Beat 3 that comes *after* the motivation.
- **Subsequent beats renumbered**: Approach (was Beat 3 → now Beat 4), Results (was Beat 4 → now Beat 5), Calibration (was Beat 5 → now Beat 6), Conclusion (was Beat 6 → now Beat 7).
- **Total runtime increased slightly** from ~8:05 to ~8:20 to accommodate the ADAS demonstration (Beat 2 grew from 60 sec to 72 sec).

**Asset additions for Beat 2 (shoot day):**

- ADAS auto-brake demonstration (parking lot or controlled environment, dual-camera if possible — dashboard + external)
- Multi-scenario ADAS context footage (pedestrians, cyclists, lane keeping, adaptive cruise — can be drawn from the same shoot day)
- Animated CNN inference graphic — `screencast/animations/cnn_inference.py` (Manim, rendered)
- Trajectory graph — `screencast/animations/trajectory_graph.py` (Manim, rendered)

**Asset additions for Beat 3 (Manim, to build):**

- LIF-neuron animation — `screencast/animations/lif_neuron.py` (single neuron with input synapses, membrane-potential trace, threshold cross, spike, reset; ~20 sec)
- Sparsity-grid animation — `screencast/animations/sparsity_grid.py` (side-by-side CNN-dense vs SNN-sparse activation grids with active-cell counters; ~20 sec)
- Quantisation diagram for Sub-beat 3B (slide or simple Manim — continuous activation vs. 1-bit spike train at the same timestamps)

**Music character across the beat order:**

| Beat | Music character |
|---|---|
| 1 (Title) | Quiet, contemplative, building |
| 2 (Motivation + ADAS) | Tension, slightly anxious; builds at "overshooting the budget" |
| 3 (SNN Introduction) | Quieter, mechanical — "the answer arriving"; not triumphant yet |
| 4 (Aims + Roadmap) | Methodical, mid-energy |
| 5 (Approach) | Clean, clinical |
| 6 (Results) | Triumphant, energetic, building |
| 7 (Calibration) | Brief drop into surprise; resolves |
| 8 (Conclusion) | Aspirational, uplifting, builds and resolves |
