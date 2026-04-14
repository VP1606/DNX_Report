# Qualitative Audit — Image Selection

## Selected Pairs

### Pair 1 — SNN Excellent
**Sample 178**
- `cnn_audit/audit_sample_178.png` — Det: 1, GT: 1, Conf: 0.93
- `snn_audit/audit_sample_178.png` — Det: 1, GT: 1, Conf: 1.0000

### Pair 2 — SNN Critical: Localization Imprecision
**Sample 003**
- `cnn_audit/audit_sample_003.png` — Det: 1, GT: 1, Conf: 0.94, tight bbox
- `snn_audit/audit_sample_003.png` — Det: 1, GT: 1, Conf: 0.96, massively oversized bbox

### Pair 3 — Ghost Detection (False Positive)
**Sample 020**
- `cnn_audit/audit_sample_020.png` — Det: 1, GT: 1, Conf: 0.78
- `snn_audit/audit_sample_020.png` — Det: 3, GT: 1, Conf: 0.94 / 0.66 / 0.57

### Pair 4 — CNN Blind Spot / SNN Sensitivity
**Sample 030**
- `cnn_audit/audit_sample_030.png` — Det: 0, GT: 1 (complete miss)
- `snn_audit/audit_sample_030.png` — Det: 2, GT: 1 (oversized, but fires in target region)

---

## Narrative

**Pair 1** directly instantiates the `Max Confidence: 1.0000` entry from Table 1.6, giving the
quantitative result a concrete visual anchor. On a large, isolated vehicle target the SNN not only
matches the CNN but surpasses it in confidence, confirming the §1.7.2 hypothesis that binary
discretization is negligible when object scale is large.

**Pair 2** is the clearest possible illustration of the SNN's primary failure mode. Both models
detect the same target with near-identical confidence (CNN 0.94, SNN 0.96), so the SNN is not
under-confident — it simply cannot resolve the boundary precisely. The predicted box overshoots the
ground truth by a wide margin. This is the direct visual explanation for why mIoU sits at 0.4658
vs 0.4861 despite the SNN recording a higher mean confidence (0.4084 vs 0.3872): the accuracy gap
is geometric, not semantic. It grounds the §1.7.2 quantization error argument in a concrete case.

**Pair 3** shows a residual ghost detection in the final ULTRA model. The SNN emits three
predictions for a single GT target; two are spurious, driven by background sensor noise rather than
a real vehicle. The paper documents ghost detections as a historical failure mode (§1.6.2) and
demonstrates that the 8×8 adaptive pooling head substantially reduced them. This sample confirms
the problem was reduced, not eliminated, and provides the critical analysis with evidence that
objectness suppression in the SNN remains imperfect.

**Pair 4** rebalances the narrative. The CNN produces zero detections on a frame that contains a
real vehicle — a complete miss — while the SNN, despite generating oversized boxes, at least fires
in the correct region. This is qualitative evidence for the §1.7.4 Temporal Evidence Accumulation
hypothesis: the SNN's sequential membrane-potential integration across T=10 timesteps provides
sensitivity in sparse event regions where the CNN's single spatial pass yields nothing. The SNN is
not strictly inferior; the two paradigms exhibit complementary failure modes.

---

## Combined Critical Analysis Paragraph (draft)

The qualitative audit reveals a consistent and interpretable pattern. On large, well-defined
targets the SNN achieves maximal confidence with competitive localization, directly evidencing the
parity predicted for high-signal scenes (Sample 178). Its dominant failure mode is not missed
detections but geometric imprecision: with comparable confidence to the CNN, the SNN's bounding
box substantially overshoots the ground truth boundary, a direct consequence of the binary
discretization floor imposed by 1-bit spike activations (Sample 003). This explains why the mIoU
gap (0.4658 vs 0.4861) is disproportionately small relative to the representational gap between
continuous floats and binary spikes. Residual ghost detections demonstrate that objectness
suppression remains imperfect in sparse event regions (Sample 020). Crucially, however, the SNN
demonstrates complementary sensitivity: on a frame where the CNN produces no output, the SNN's
temporal integration generates a response, highlighting that the two paradigms exhibit distinct
rather than uniformly ordered failure profiles (Sample 030).
