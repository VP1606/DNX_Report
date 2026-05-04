# Current Video Timeline

**Current Duration: 1:19**

Note: the time markings (eg. T+0:16) indicate the time that the current section **ends** at: T+0:16 would mean that the current section ends at 0:16s from the start of the full timeline.

## 1. Intro (T+0:16)

- Visual: An intro slide, with the report title, and my name.

- Voiceover: "Hi, I'm Varun. This is my third-year project, DetectorNX — investigating the viability of spiking neural networks for advanced driver-assistance systems, through a strictly-controlled comparison against an equivalent CNN baseline on automotive vehicle detection."

## 2. ADAS + The Problem

### 2.1: AEB Example (T+0:32)

- Visual: A clip that I recorded of my car driving, showing the AEB system activating.

- Voiceover: "What you're watching is an Advanced Driver-Assistance System — ADAS — in action. The car has detected an obstacle in its path and informed me through the alert. If I didn't notiice this, or the car in front brakes hard, it would apply the brakes automatically. Faster than I could react."

### 2.2: ADAS Overall (T+0:52)

- Visual: Clips of Tesla's FSD system, and at the end the EuroNCAP logo appears when talking about the new rule changes of 2026.

- Voiceover: "ADAS systems handle pedestrians at junctions, cyclists in blind spots, lane keeping, adaptive cruise — the kinds of perception we used to leave entirely to human attention. By 2026, regulators want every new vehicle to handle these scenarios reliably, at speeds up to 130 kilometres per hour."

### 2.3: Technical Challenge

#### 2.3.1: Current CNNs (T+1:06)

- Visual: Manim CNN visualisation (screencast/animations/cnn_inference.py)

- Voiceover: "Modern ADAS handles this with Dense Convolutional Neural Networks running on GPUs. Billions of operations every seconds just to percieve the road - but cars have tight power and thermal budgets, and as ADAS becomes more capable, the compute demand keeps climbing."

#### 2.3.2: Compute Trajectory (T+1:19)

- Visual: Manim Trajectory visualisation (screencast/animations/trajectory_graph.py)

- Voiceover: "Just 8 years ago, studies showed that CPU inference had already exceeded what onboard hardware could sustain. We're now approaching the same wall with GPUs, calling for a fundamentally different approach to solve this problem."

## 3. SNNs + Sparsity

### 3.1: SNNs (T+1:38)

- Visual: Manim LIF visualization (screencast/animations/lif_neuron.py)

- Voiceover: "To attempt to reduce the power draw, this project turns to spiking neural networks. Unlike a CNN - where every neuron fires every cycle - a spiking neuron stays silent. It integrates input until that input crosses a threshold. Then, it fires a single discrete spike, and resets." 

### 3.2: Sparsity (T+1:58)

- Visual: Manim Visualization (screencast/animations/sparsity_grid.py)

- Voiceover: "One of the main reasons spiking neural networks are so efficient is due to their sparsity. The entire network communicates through these sparse binary events. At any moment, ninety to ninety-five percent of neurons are silent. And because spikes are binary, no spike means a multiply by zero, so the hardware skips the operation entirely."

%%%%%%%%%% PLAN %%%%%%%%%%

### Quantization Catch (T+2:)

- Visual: Manim Visualization (screencast/animations/quantization_diagram.py)

- Voiceover: "But there's a catch: a spike is binary --- it either fires or it doesn't --- so every single signal collapses from a 32bit float down to a single bit, losing all detail in between.

The resulting loss in precision is called quantization error, and one of this project's aims is to measure it."

## 4. Aims + Roadmap

### 4.1: Aims

- Visual: Slides, with animation of two points:

1. "Is the spiking paradigm viable for automotive-grade perception?"

2. "What does it cost?"

- Voiceover: "And that's one of two central questions this project takes on.
The first is whether the spiking paradigm is actually viable for safety-critical automotive perception.
The second is what that precision cost actually is — measured by evaluating a CNN and an SNN with the same input and output types, and one-to-one architectural parity."

### 4.2: Roadmap

- Visual: Slide containing:
Vertical numbered list, each item highlighted/lit as you say it (subtle accent-colour fade, not bouncing).
1. Method
2. Results
3. Calibration finding
4. What's next

- Voiceover: "Over the next few minutes, we'll start with our experimental approach, isolating the spiking mechanism for an objective comparison. 
Then, we'll cover the headline results in both energy and accuracy.
We'll look at a surprising, safety-critical advantage uncovered in our calibration analysis.
And, we'll close with the future directions DetectorNX opens up."

## 5. Approach

### 5.1: Methodology

- Visual: Manim (screencast/animations/methodology_parity.py)

- Voiceover: "So, let's start with the methods. To isolate the spiking mechanism, we built two detectors with strict architectural parity. The one thing that changes is the activations --- continuous in one, discrete spikes in the other. Same backbone, same parameters, and the same data. Any difference we measure is attributable to the spiking mechanism alone."

### 5.2: Artefacts

- Visual: screencast/animations/artefact_diagram.py

- Voiceover: "And here is DetectorNX, end-to-end. The spiking variant --- G3-SNN --- and its continuous twin --- G3-CNN. Both at 11.7 million parameters, and trained on ETRaM: an event-camera dataset capturing real urban traffic from a static roadside camera.
To our knowledge, this is the first directly-trained spiking detector evaluated on ETraM."

## 6. Results

### 6.1: Precision Parity

- Visual:

- Voiceover: "
Now, onto the results. The two detectors are running here in parallel on the same ETraM scene, with bounding boxes being overlaid in real time.

Starting with precision: the spiking variant reaches a mean IoU of 0.461 — 94.9% of the continuous baseline's 0.486. 

On the stricter mAP-at-0.5 metric, it scores 59.8% - 91.3% of the baseline. Both architectures achieve 100% recall on objects with IoU above 0.5, meaning every vehicle in the scene is found. The roughly 5-percent gap is the measured cost of one-bit quantisation, but the spiking model still matches the continuous baseline on detection completeness."

### 6.2: Efficiency

- Voiceover: "
Now efficiency. The spiking variant consumes 2.4 millijoules per frame, against 42.4 for the continuous baseline, resulting in a 94.33% reduction in per-frame energy. But, there's something more interesting going on. The SNN's energy scales with the activity in the scene: as the traffic gets denser, the spiking model's energy rises proportionally — what we call Reactive Scalability, with an R-squared of 0.7514. The CNN, in contrast, consumes the same energy whether the road is empty or packed. This is a paradigm-level efficiency property that doesn't exist on continuous architectures."

### 6.3: Real-Time FPS

- Voiceover: "
And now speed. 
The SNN sustains nearly 260 frames per second on GPU hardware,
which is 8 times the safety margin over the 30-FPS threshold that is considered the minimum for real-time automotive perception. 

Across all six pre-defined success criteria — precision parity, energy efficiency, real-time throughput, parameter parity, detection completeness, and confidence calibration — DetectorNX passes every single one. But one of those criteria produced a result we didn't expect."

## 7. Confidence Finding

"The sixth criterion was confidence calibration — how well the model's stated certainty in a detection compares to whether that detection was actually correct. Going in, we expected parity. We got something different."

"Here's the calibration plot. The CNN, on the right, shows a pronounced overconfidence bias — routinely assigning high confidence to detections that turn out to have zero overlap with any actual vehicle. The SNN, on the left, doesn't do this. When the spiking model is uncertain, its confidence correctly drops toward zero."

"As a result, the SNN naturally acts as an implicit uncertainty sensor. 
For ADAS — where over-confident hallucinations could trigger dangerous emergency braking — this finding becomes even more signficant, as it becomes a safety-critical advantage."

## 8. Conclusion + Future Work

"To conclude, let's summarise the key takeaways of this project. First — the cost. Under variable-isolated comparison, the spiking variant loses roughly 5% mIoU against its continuous twin. Measurable, but architecturally tractable."

Sub-beat 8B: The Benefit (~13 s, 29 words):

"Second — the benefit. That cost buys a 94% reduction in per-frame energy, plus reactive scalability — energy that scales with scene activity rather than running flat."

Sub-beat 8C: The Advantage (~13 s, 26 words):

"Third — the unexpected finding. The spiking model calibrates honestly at low confidence — naturally acting as an implicit uncertainty sensor, directly safety-relevant for ADAS."

Sub-beat 8D: Where This Goes Next + Close (~28 s, 58 words):

"Together, these results establish the spiking paradigm as a viable — not theoretical — route to safety-critical edge perception. The open question is whether this generalises beyond automotive vehicle detection. That's where this work points next: porting DetectorNX to multi-class benchmarks, integrating an SNN-native classification head, and ultimately deploying on real neuromorphic silicon. 

In the end, neuromorphic computing is still in its infancy, and projects such as DetectorNX  serve as baselines and proof-of-concept for what will soon be possible. This is DetectorNX: a High-Definition spiking neural network designed for automotive perception, thank you for watching.