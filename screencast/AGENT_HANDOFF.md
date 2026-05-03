# Screencast Production — Agent Handoff

**Last updated:** 2026-05-01
**For:** A fresh Claude agent picking up screencast production while another agent works on the report in parallel.
**Read this whole file before doing anything.**

---

## 1. Project at a glance

**DetectorNX** is Varun Premakantha's BSc Computer Science dissertation at the University of Manchester (2026). It is a **strictly-controlled, variable-isolated comparison of an SNN object detector against an architecturally-equivalent CNN baseline** on the ETraM event-camera dataset (Verma et al., 2024).

The two model variants:

- **DetectorNX-G3-SNN** — spiking variant, SEWResBlock backbone
- **DetectorNX-G3-CNN** — continuous twin, ResBlock backbone
- Both at **11.7 M parameters**, identical preprocessing, identical regression head, identical training hyperparameters and data. The only difference is whether activations are continuous or spiking.

**Headline results to know** (these get cited in the screencast voiceovers):

- **94.33% per-frame energy reduction** (SNN: 2.4 mJ/frame vs CNN: 42.4 mJ/frame)
- **94.9% mIoU parity** (SNN matches the CNN baseline within ~5%)
- **91.3% mAP₅₀ parity**
- **100% recall** on objects with IoU ≥ 0.5 (both models)
- **259.80 FPS on GPU** (8.6× margin over the 30-FPS real-time threshold)
- **Reactive Scalability — R² = 0.7514** (SNN energy scales with scene activity; CNN doesn't)
- **Confidence calibration finding** — SNN's confidence drops honestly toward zero on uncertain detections; CNN exhibits high-confidence hallucinations. Implicit uncertainty sensor → safety-relevant for ADAS.

**To our knowledge, this is the first directly-trained spiking detector evaluated on ETraM** — keep this hedge phrasing when relevant.

---

## 2. Screencast goal and rubric

**Target:** 7–9 minute screencast for the BSc dissertation rubric, aiming for top marks. Reference quality bar: Tesla FSD reveal videos / Anthropic product launch videos. Cinematic, confident, professional.

**Current total runtime:** 8:35 (inside band).

**Beat structure (8 beats):**

| Beat | Range | What |
|---|---|---|
| 1 | 0:00 – 0:18 | Title intro |
| 2 | 0:18 – 1:30 | Motivation + ADAS Demo (real driving footage + auto-brake) |
| 3 | 1:30 – 2:30 | **SNN Introduction** ← we are here |
| 4 | 2:30 – 3:20 | Aims + Roadmap |
| 5 | 3:20 – 4:10 | Approach (Methodology + Artefacts) |
| 6 | 4:10 – 6:20 | Results (live SNN+CNN parallel demo) |
| 7 | 6:20 – 7:20 | Calibration finding |
| 8 | 7:20 – 8:35 | Conclusion + Future Work |

**Full script:** `/sessions/focused-eloquent-hawking/mnt/DNX_Report/screencast/scripts/full_script.md` — read this for visual timelines, voiceovers, and music direction. Treat it as the source of truth.

---

## 3. File map for the screencast folder

```
screencast/
├── AGENT_HANDOFF.md                      ← this file
├── scripts/
│   └── full_script.md                    ← source of truth for narration + visuals
└── animations/
    ├── README.md                         ← Manim install + render instructions
    ├── cnn_inference.py                  ← DONE (Sub-beat 2C, 1st half)
    ├── trajectory_graph.py               ← DONE (Sub-beat 2C, 2nd half)
    ├── lif_neuron.py                     ← TO BUILD (Sub-beat 3A, 1st half)
    └── sparsity_grid.py                  ← TO BUILD (Sub-beat 3A, 2nd half)
```

Render commands live in `animations/README.md`. Standard final command:

```bash
manim -pqh <file>.py <SceneClassName>
```

Output: `media/videos/<file>/1080p60/<SceneClass>.mp4` — drag straight into Keynote.

---

## 4. Production state — what's done and what's pending

### Beat 1 — Title intro
- ✅ Script ready
- ✅ Slide built and voiceover recorded by user (per their last status update)

### Beat 2 — Motivation + ADAS Demo
- ✅ Script ready
- ⚠️ Sub-beat 2A (ADAS demonstration, 17 s): footage to shoot — Varun's car, dashboard ADAS interface, auto-brake intervention. Dual-camera recommended.
- ⚠️ Sub-beat 2B (What ADAS does, 20 s): multi-scenario footage to shoot (pedestrians, cyclists, lane keeping, adaptive cruise) + regulatory-context graphic.
- ✅ Sub-beat 2C (technical challenge, 35 s):
  - ✅ `cnn_inference.py` — rendered, ~8.5 s, ends with FLOP counter at 9.22 G-FLOPs
  - ✅ `trajectory_graph.py` — rendered, ~13 s, ends with arrow + "?" pointing DOWN from L4 dot toward budget line
  - ✅ Voiceover updated to use real watt numbers (ECU < 50 W, L3 200–350 W, L4 ~1000 W, industry target ~200 W)

### Beat 3 — SNN Introduction ← **immediate next task**
- ✅ Script ready (Sub-beat 3A voiceover paired with two animations to build)
- ❌ `lif_neuron.py` — **TO BUILD**
- ❌ `sparsity_grid.py` — **TO BUILD**
- ⚠️ Sub-beat 3B (the catch, 15 s) — quantisation diagram. Can be a simple slide; doesn't need Manim unless you have time.

### Beats 4–8
- ✅ All scripts ready
- ❌ No production work yet
- Beat 5B uses the existing high-level architecture SVG from the report (`report/chapter_3/figures/high-level-architecture.svg`)
- Beat 6 needs the live SNN+CNN parallel demo (separate engineering task — likely outside the screencast folder)
- Beat 7 uses the two reliability diagrams from §3.8 of the report
- Beat 8 is mostly text cards + thumbnails of earlier visuals

---

## 5. **Immediate next task — build `lif_neuron.py`**

**Voiceover this animation pairs with** (Sub-beat 3A, lines 1:35 – 1:55, 20 s on screen):

> "Unlike conventional CNNs — where every neuron fires a continuous activation every cycle — a spiking neuron stays silent until its input crosses a threshold. Then it fires a single discrete spike, and resets."

**(The full Sub-beat 3A voiceover is longer; this animation only needs to cover the threshold-cross-fire-reset cycle. The sparsity grid carries the rest.)**

**Visual specification** (from `full_script.md`, Sub-beat 3A visual timeline):

> Single neuron on the left with input synapses; membrane-potential trace on the right rises step-by-step with each input spike, decays slightly between inputs, hits a horizontal dashed threshold, fires a spike, and resets. Output spike train below.

**Concrete elements to include:**

1. **Left third:** a labelled neuron — circle with 3–4 input synapse arrows feeding in. Input spikes arrive as discrete pulses on those synapses (sparse timing).
2. **Middle/right two-thirds:** a graph titled *"Membrane potential V(t)"* — y-axis = potential, x-axis = time. A horizontal dashed threshold line (label: *"threshold"*).
3. **Trace behaviour:** with each input spike, the membrane potential jumps up (integrate). Between inputs, it decays slightly (leak). When the trace crosses threshold, a spike fires (visual flash on the neuron + tick on output train) and the potential **resets to zero**. Cycle repeats 2–3 times during the animation.
4. **Bottom:** an output spike train — discrete vertical lines marking each output spike time.
5. **Closing caption** (~last 2 s): *"spike → reset → repeat"*.

**Style requirements (match the existing two animations):**

- Background: pure black `#000000`
- Title at top, font_size=30, white
- Axis labels font_size=24, GREY_B
- Threshold dashed line in YELLOW or GREY_B
- Membrane trace in BLUE (or RED if you want to match "compute" → "spike paradigm" framing)
- Spike events: brief white flash on neuron + same colour tick on output train
- Use Manim Community Edition idioms (Scene class, self.play, run_time params)
- **No emojis**

**Timing target:** ~18–22 s total. Voiceover slot is 20 s; aim for 20.

---

## 6. After `lif_neuron.py` — build `sparsity_grid.py`

**Voiceover this animation pairs with** (Sub-beat 3A, lines 1:55 – 2:15, 20 s on screen):

> "The entire network communicates through these sparse binary events. In a typical scene, ninety to ninety-five percent of neurons stay quiet at any given moment. And here's the key: no spike means no computation. The hardware skips the multiply-accumulate entirely."

**Visual specification:**

- Side-by-side grids labelled *"CNN"* (left) and *"SNN"* (right). Each grid ~12×12 cells.
- **CNN grid:** every cell is continuously coloured (a heatmap-style fill, e.g. varying intensities of one colour) — visual message: "always on."
- **SNN grid:** mostly black cells, with occasional white flashes appearing and disappearing (~5–8% active at any frame) — visual message: "mostly silent, sparse spikes."
- Below each grid: an "% active this frame" counter.
  - CNN counter: stays at *"100%"* throughout.
  - SNN counter: hovers at *"5–8%"*, fluctuating slightly.
- **Closing card** (~last 3 s): a centered text frame replacing or overlaying the grids: *"no spike → no computation → no power"*.

**Style:** same as `lif_neuron.py` (black background, same fonts, same colour palette).

**Timing target:** ~18–22 s.

---

## 7. Stylistic patterns established by the existing animations

Read `cnn_inference.py` and `trajectory_graph.py` before you start. Concrete patterns to match:

- File starts with a docstring describing what the animation does, where it sits in the screencast, and the render commands.
- `self.camera.background_color = "#000000"` first line of `construct`.
- Block comments separate the file into named sections (e.g. `# ===== TITLE =====`).
- Each `self.play(...)` has an explicit `run_time=...`.
- Animations end with a short `self.wait(0.8)` or similar to let the final frame land.
- Total animation length is in the file's docstring.

---

## 8. Lessons learned from prior iterations (don't repeat these)

- **Don't fabricate numbers.** When the trajectory graph first showed an arbitrary 12 W power budget, the user pushed back. We then asked for real data points. If you need a number you don't have, ask Varun for it before guessing.
- **Labels need empty quadrants.** On `trajectory_graph.py`, multiple iterations were needed because labels collided with the x-axis numerals and the rising curve. Plan label positions explicitly into empty regions of the chart.
- **Use UP from a dot when the dot is near the x-axis** — labels positioned DR (down-right) end up below y=0 and clash with axis numerals.
- **Explicit watt numbers > vague qualitative claims.** The script was rewritten to use "200–350 W" instead of "tight power budgets" because concrete numbers land harder.
- **Confident phrasing > hedged phrasing.** Varun has a gentle tendency toward hedge words like "attempt to reduce" or "we set out to". In voiceover phrasing, default to confident verbs ("DetectorNX turns to…", "DetectorNX answers…"). Always preserve Varun's original wording as an italicised fallback note.

---

## 9. How Varun likes to work

- **Iterative.** He'll review what you build, give specific feedback, and ask for revisions. Don't try to nail it in one shot — get a v1 in front of him.
- **Specific feedback.** When he points at a bug ("the curve doesn't connect to the L4 point"), fix exactly that bug; don't take liberties unless you flag them.
- **Confident proposals welcome.** If you see a structural improvement (like swapping the order of two beats), propose it explicitly and explain why. He'll accept or push back.
- **Author's intent matters.** When Varun gives you a voiceover line, you can suggest refinements but preserve his version as a fallback. He's the author.

---

## 10. Communication shortcuts

- The user is **Varun** (`vpremakantha@gmail.com`). Address him by name when relevant.
- Workspace folder he sees: `/sessions/focused-eloquent-hawking/mnt/DNX_Report/`. When sharing files use `computer://` links to the workspace path, not the sandbox path.
- He's also working with another agent on the report in parallel — coordinate by treating the script and animation files as the shared interface. **Don't touch report files** (anything outside the `screencast/` folder) unless he explicitly asks. The report agent is the owner of `report/`, `chapter_*/`, `evaluations/`, etc.

---

## 11. When you finish a task

1. Verify the change (read the file back; run it if it's renderable).
2. Tell Varun what you did, in 2–4 lines, and provide a `computer://` link to the deliverable.
3. Suggest the next concrete step.
4. Don't write long summaries unless asked.

---

## 12. If you're starting cold right now, do exactly this:

1. Read this entire file.
2. Read `scripts/full_script.md` — at minimum Beats 2 and 3 to understand the bridge from trajectory "?" into SNN reveal.
3. Read `animations/cnn_inference.py` and `animations/trajectory_graph.py` for style.
4. Build `animations/lif_neuron.py` to spec (§5 above).
5. Tell Varun it's ready and wait for feedback before moving on to `sparsity_grid.py`.
