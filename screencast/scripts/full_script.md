## Beat 1: Intro

═══════════════════════════════════════════════════════════════
  BEAT 1 — INTRO (0:00 – 1:10, ~67 sec)
═══════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│ [0:00 – 0:15]  SUB-BEAT 1: TITLE + CONTEXT  (~15 sec)       │
└─────────────────────────────────────────────────────────────┘

SLIDE: Title card.
  • Centre: [DetectorNX] in large type
  • Below: "Premakantha Varun"
  • Footer: "BSc Computer Science · University of Manchester · 2026"
  • Bottom-right: university logo

VOICEOVER:
""Hi, I'm Varun. This is my third-year project, DetectorNX —
 investigating the viability of spiking neural networks for
 advanced driver-assistance systems, through a strictly-
 controlled comparison against an equivalent CNN baseline
 on automotive vehicle detection."

(40 words / ~18 sec)

┌─────────────────────────────────────────────────────────────┐
│ [0:15 – 0:40]  SUB-BEAT 2: AIMS  (~25 sec)                  │
└─────────────────────────────────────────────────────────────┘

SLIDE: Two questions, fading in sequentially as spoken.
  Q1: "Is the spiking paradigm viable for automotive-grade
       perception?"
  Q2: "What does it cost?"
  (Both stay on screen at the end of the sub-beat.)

VOICEOVER:
"We set out to answer two main questions in this project. First — is the spiking
 neural network paradigm actually viable for safety-critical
 automotive perception at high definition? And second — what
 does the precision cost of switching from continuous to
 spiking actually look like, when measured under tightly
 controlled conditions?"

(50 words at ~140 wpm)


┌─────────────────────────────────────────────────────────────┐
│ [0:40 – 1:10]  SUB-BEAT 3: ROADMAP  (~30 sec)               │
└─────────────────────────────────────────────────────────────┘

SLIDE: Vertical numbered list, each item highlighted/lit as
       you say it (subtle accent-colour fade, not bouncing).
  1. Motivation
  2. Method
  3. Results
  4. Calibration finding
  5. What's next

VOICEOVER:
"In the next eight minutes, I'll walk you through five
things: the motivation behind moving away from dense neural
networks; how DetectorNX isolates the spiking mechanism
through strict architectural parity; our headline results,
including a 94 percent energy saving alongside full
precision parity; an unexpected finding about confidence
calibration that's safety-relevant for advanced driver-
assistance systems; and finally, the open question of how
this generalises beyond automotive vehicle detection."

(73 words at ~140 wpm)

## Beat 2: Motivation

═══════════════════════════════════════════════════════════════
  BEAT 2 — MOTIVATION / PROBLEM (1:10 – 2:10, ~60 sec)
═══════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│ [1:10 – 1:27]  SUB-BEAT 2A: GROWING DEMANDS  (~17 sec)      │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Urban-driving B-roll (top-down or driver POV).
  Overlay text appears as you mention each item:
    • "Pedestrians at junctions"
    • "Cyclists from blind spots"
    • "Up to 130 km/h"
  Bottom-right corner: small "Euro NCAP 2026" tag, royalty-free
  use only.

VOICEOVER:
"Autonomous driving is getting more demanding by the year.
 Regulators like Euro NCAP are pushing manufacturers toward
 systems that can spot pedestrians at busy junctions,
 cyclists emerging from blind spots, and motorcycles braking
 ahead — all at speeds up to 130 kilometres per hour."

(37 words / ~17 sec)


┌─────────────────────────────────────────────────────────────┐
│ [1:27 – 1:37]  SUB-BEAT 2B: CURRENT APPROACH  (~10 sec)     │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Animated CNN architecture diagram (input
  frame → conv blocks → output bounding boxes). At the end of
  the sub-beat, a counter appears:
    "9.22 G-FLOPs · per frame · per inference"

VOICEOVER:
"Modern vehicles meet these demands with dense convolutional
 neural networks processing high-definition video streams in
 real time — billions of operations every single second."

(22 words / ~10 sec)


┌─────────────────────────────────────────────────────────────┐
│ [1:37 – 1:55]  SUB-BEAT 2C: HITTING A WALL  (~18 sec)       │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Two-line graph.
  Y-axis: compute demand (W).
  X-axis: time (years, 2015 → 2026).
  Line 1: rising compute demand of perception models.
  Line 2: flat or shrinking automotive on-board power budget.
  CPU-saturation marker around 2018 (anchored by "Lin et al. 2018").
  GPU still flat-ish but approaching the demand line.

VOICEOVER:
"But this is hitting a wall. Cars have tight on-board power
 and thermal budgets. Lin and colleagues showed back in 2018
 that CPU-based inference had already exceeded those
 constraints, motivating the industry's shift to GPU
 accelerators."

(38 words / ~18 sec)


┌─────────────────────────────────────────────────────────────┐
│ [1:55 – 2:10]  SUB-BEAT 2D: TRAJECTORY → NEW PARADIGM       │
│                                                  (~15 sec)  │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Same graph as 2C, now extending to 2026+.
  GPU compute-demand line now crossing the budget line.
  A bold "?" or arrow points beyond the GPU saturation point.
  Sets up Beat 3 — what comes next?

VOICEOVER:
"Eight years on, dense GPU inference is heading toward the
 same saturation — calling for a fundamentally more efficient
 computational paradigm."

(22 words / ~10 sec — leaves 5-sec breathing space before Beat 3)

## Beat 3: Approach

═══════════════════════════════════════════════════════════════
  BEAT 3 — APPROACH (2:10 – 3:40, ~90 sec)
═══════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│ [2:10 – 2:35]  SUB-BEAT 3A: WHAT'S AN SNN  (~25 sec)        │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Side-by-side CNN-vs-SNN neuron output.
  Left panel: continuous waveform output (CNN neuron — always
              active, smooth curve)
  Right panel: spike train (SNN neuron — quiet most of the time,
              discrete vertical lines when membrane potential
              crosses threshold)
  Animate the membrane potential rising and crossing a dashed
  threshold line, triggering a spike.

VOICEOVER:
"Spiking neural networks offer a fundamentally different
 approach. Unlike conventional CNNs — where every neuron
 computes a continuous activation at every layer — spiking
 neurons only fire, and only consume energy, when their
 membrane potential crosses a threshold. The result is
 sparse, event-driven computation that mirrors how
 biological brains actually work."

(55 words / ~25 sec)


┌─────────────────────────────────────────────────────────────┐
│ [2:35 – 2:48]  SUB-BEAT 3B: THE CATCH  (~13 sec)            │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Quantisation diagram.
  A smooth continuous activation curve vs. a 1-bit binary
  spike train at the same timestamps. Caption underneath:
    "32-bit continuous → 1-bit spike"
  Brief on-screen text: "How much does this cost?"

VOICEOVER:
"But there's a catch. Spikes are binary — they either fire
 or they don't — so every signal gets quantised to one bit.
 The question is, how much does that actually cost?"

(29 words / ~13 sec)


┌─────────────────────────────────────────────────────────────┐
│ [2:48 – 3:13]  SUB-BEAT 3C: METHODOLOGY  (~25 sec)          │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Two backbones side-by-side, structurally
  identical (same block shapes, same connections). The only
  visual difference: the residual blocks are coloured green
  (SNN, SEWResBlock) on the left, purple (CNN, ResBlock) on
  the right. Identical preprocessing pipeline above; identical
  regression head below.
  Bottom-left tag: "11.72 M params" / "11.73 M params"

VOICEOVER:
"To answer that, we built two object detectors with strict
 architectural parity. Same backbone shape, same parameter
 count, same training hyperparameters, same data. The only
 thing that changes between them is whether the activations
 are continuous or spiking — which means any performance
 difference we measure is attributable to the spiking
 mechanism alone."

(55 words / ~25 sec)


┌─────────────────────────────────────────────────────────────┐
│ [3:13 – 3:36]  SUB-BEAT 3D: THE ARTEFACTS  (~23 sec)        │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: The full high-level architecture diagram (the
  SVG we just made — green SNN backbone, purple CNN backbone,
  preprocessing pipeline above, regression head and evaluation
  suite below). It lands on the slide all at once and stays
  for the duration of the sub-beat.
  Below the diagram, an ETraM sample frame appears with a
  caption: "ETraM event-camera dataset — Verma et al., 2024"

VOICEOVER:
"That's DetectorNX. The spiking variant — DetectorNX-G3-SNN
 — and its continuous twin — DetectorNX-G3-CNN. Both at
 11.7 million parameters. Both trained on the ETraM event-
 camera dataset, which captures real urban traffic from a
 static roadside camera. To our knowledge, this is the first
 directly-trained spiking detector evaluated on ETraM."

(50 words / ~23 sec)

## Beat 4:  Results

═══════════════════════════════════════════════════════════════
  BEAT 4 — RESULTS (3:40 – 5:50, ~130 sec)
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
│ [3:40 – 4:17]  SUB-BEAT 4A: PRECISION PARITY  (~37 sec)     │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Demo running. Highlight the mIoU readouts at
  the bottom of each pane. Briefly overlay text: "94.9% mIoU
  parity · 91.3% mAP₅₀ parity · 100% recall (both)".

VOICEOVER:
"Let's start with precision. Both models are running here in
 parallel on the same ETraM scene — bounding boxes overlaid in
 real time. The spiking variant reaches 94.9% mIoU parity
 against the continuous baseline, and 91.3% on the stricter
 mAP-at-0.5 IoU metric. And both architectures achieve 100%
 recall on objects with IoU above 0.5 — every vehicle in the
 scene is found. The roughly 5-percent precision gap is the
 measured cost of one-bit quantisation, but the spiking model
 matches the continuous baseline on detection completeness."

(80 words / ~37 sec)


┌─────────────────────────────────────────────────────────────┐
│ [4:17 – 5:05]  SUB-BEAT 4B: EFFICIENCY  (~48 sec)           │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Demo continues. Power readouts now highlighted.
  Toward the end of the sub-beat, a small inset graph appears
  in the corner showing energy-vs-event-count with the linear
  fit (R² = 0.7514) — the "Reactive Scalability" plot.

VOICEOVER:
"Now efficiency. Watch the power readout under each model.
 The SNN consumes around 2.4 millijoules per frame, against
 42.4 for the CNN — a 94.33% reduction in per-frame energy.
 But there's something more interesting going on. The SNN's
 energy scales with the activity in the scene. As the traffic
 gets denser, the spiking model's energy rises proportionally
 — what we call Reactive Scalability, with an R-squared of
 0.7514. The CNN, in contrast, consumes the same energy whether
 the road is empty or packed. This is a paradigm-level efficiency
 property that doesn't exist on continuous architectures."

(105 words / ~48 sec)


┌─────────────────────────────────────────────────────────────┐
│ [5:05 – 5:38]  SUB-BEAT 4C: REAL-TIME + BRIDGE  (~33 sec)   │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Demo continues. FPS readouts now highlighted.
  Toward the end, the SC validation table appears briefly
  (small, summarised — six items with green ticks), then
  fades to a transitional black or simple text:
    "...one of those criteria produced a result we didn't expect."

VOICEOVER:
"And speed. The SNN sustains 259.80 frames per second on GPU
 hardware — an 8.6× safety margin over the 30-FPS threshold
 considered the minimum for real-time automotive perception.
 Across all six pre-defined success criteria — precision
 parity, energy efficiency, real-time throughput, parameter
 parity, detection completeness, and confidence calibration —
 DetectorNX passes every single one. But one of those
 criteria produced a result we didn't expect."

(75 words / ~35 sec)

## Beat 5: Calibration

═══════════════════════════════════════════════════════════════
  BEAT 5 — THE UNEXPECTED FINDING (5:50 – 6:50, ~60 sec)
═══════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────┐
│ [5:50 – 6:08]  SUB-BEAT 5A: THE REVEAL  (~18 sec)           │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Pick up from Beat 4's transition card. A
  single full-screen text card appears:
    "The 6th criterion: Confidence Calibration"
  Background colour distinct from prior beats — slight visual
  break to mark the shift to "the unexpected result".

VOICEOVER:
"That sixth criterion was confidence calibration — basically,
 how well the model's stated certainty about a detection
 actually tracks how often that detection turns out to be
 correct. Going in, we expected parity. We got something
 different."

(40 words / ~18 sec)


┌─────────────────────────────────────────────────────────────┐
│ [6:08 – 6:31]  SUB-BEAT 5B: THE EMPIRICAL FINDING  (~23 sec)│
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: The two reliability diagrams from §3.8,
  side-by-side:
    Left panel  — SNN reliability diagram
    Right panel — CNN reliability diagram
  Both axes labelled (x: confidence, y: IoU). Identity line
  (perfect calibration) shown as dashed.
  Highlight cues:
    • CNN panel: red circle/glow on the cluster of points
      at HIGH confidence + ZERO IoU (the overconfident
      hallucinations). Brief callout: "high confidence,
      zero overlap"
    • SNN panel: green circle/glow on the cluster of points
      at LOW confidence + LOW IoU (correctly suppressed).
      Brief callout: "wrong, and knows it"

VOICEOVER:
"Here's the calibration plot. The CNN, on the right, shows a
 pronounced overconfidence bias — it routinely assigns high
 confidence to detections that turn out to have zero overlap
 with any actual vehicle. The SNN, on the left, doesn't do
 this. When the spiking model is uncertain, its confidence
 honestly drops toward zero."

(50 words / ~23 sec)


┌─────────────────────────────────────────────────────────────┐
│ [6:31 – 6:46]  SUB-BEAT 5C: WHY IT MATTERS  (~15 sec)       │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Concept icon — a steering wheel plus an
  emergency-brake symbol, with a thought-bubble showing the
  SNN's "honest uncertainty" output rather than a confident
  hallucination. Or simpler: text card with three lines:
    "Implicit uncertainty sensor"
    "Safety-critical for ADAS"
    "No spurious emergency interventions"

VOICEOVER:
"In other words, the SNN naturally acts as an implicit
 uncertainty sensor. For ADAS, where over-confident
 hallucinations could trigger spurious emergency braking,
 this isn't just a curiosity — it's a safety-critical
 advantage."

(33 words / ~15 sec)

## Beat 6: Conclusions, Closing & Future Work

═══════════════════════════════════════════════════════════════
  BEAT 6 — TAKEAWAY + FUTURE WORK (6:50 – 8:05, ~75 sec)
═══════════════════════════════════════════════════════════════

NARRATIVE FRAME: "So the takeaways are threefold..." Each
takeaway lands as its own sub-beat with a single big number
on screen, then the future-work close brings everything home.

┌─────────────────────────────────────────────────────────────┐
│ [6:50 – 7:04]  SUB-BEAT 6A: TAKEAWAY 1 — THE LOSS  (~14 s)  │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Three-item takeaway list appears, with
  item #1 highlighted/lit:
    1. The cost                           ◄ active
    2. The benefit
    3. The unexpected advantage
  Big number anchored beside item #1: "~5% mIoU"
  Small subtitle below: "precision cost · variable-isolated"

VOICEOVER:
"So the takeaways are threefold. First — the cost. Under
 variable-isolated comparison, the spiking variant loses
 roughly 5% mIoU against its continuous twin. Measurable,
 but architecturally tractable."

(30 words / ~14 sec)


┌─────────────────────────────────────────────────────────────┐
│ [7:04 – 7:18]  SUB-BEAT 6B: TAKEAWAY 2 — THE BENEFIT (~14s) │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Item #2 now lit on the same takeaway list.
  Big number anchored beside item #2: "94% energy reduction"
  Small subtitle: "+ reactive scalability"
  Optional: a small thumbnail of the Reactive Scalability
  inset graph from Beat 4B.

VOICEOVER:
"Second — the benefit. That precision cost buys you a 94%
 reduction in per-frame energy, plus reactive scalability —
 energy that scales with scene activity rather than running
 flat."

(29 words / ~13 sec)


┌─────────────────────────────────────────────────────────────┐
│ [7:18 – 7:33]  SUB-BEAT 6C: TAKEAWAY 3 — THE ADVANTAGE      │
│                                                  (~15 sec)  │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Item #3 now lit on the takeaway list.
  Big text anchored: "Implicit uncertainty sensor"
  Small subtitle: "safety-critical for ADAS"
  Optional: thumbnail of the SNN reliability diagram from
  Beat 5B.

VOICEOVER:
"Third — the unexpected finding. The spiking model exhibits
 superior confidence calibration at low-confidence regions,
 naturally acting as an implicit uncertainty sensor —
 directly safety-relevant for ADAS deployment."

(29 words / ~13 sec)


┌─────────────────────────────────────────────────────────────┐
│ [7:33 – 8:01]  SUB-BEAT 6D: WHERE THIS GOES NEXT  (~28 sec) │
└─────────────────────────────────────────────────────────────┘

SLIDE / VISUAL: Forward-looking visual.
  Top of slide: bold statement card —
    "Spiking is viable. Not theoretical. Viable."
  Below: three future-work directions appearing as bullets:
    → Multi-class generalisation (single-class COCO subset)
    → SNN-native classification head
    → Neuromorphic hardware deployment (Loihi 2)
  Final transition (~ last 4 sec): card fades to closing
  card with project name, your name, university, "Thanks
  for watching."

VOICEOVER:
"Together, these results establish the spiking paradigm as
 a viable — not theoretical — route to safety-critical edge
 perception. The open question is whether this generalises
 beyond automotive vehicle detection. That's where this
 work points next: porting DetectorNX to broader multi-class
 benchmarks, integrating an SNN-native classification head,
 and ultimately deploying on real neuromorphic silicon.
 Thanks for watching."

(60 words / ~28 sec)