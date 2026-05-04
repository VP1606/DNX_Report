"""
Calibration Finding — Beat 7
DetectorNX Screencast — Beat 7 (the unexpected result)

Three-act animation that picks up from Beat 6C's cliffhanger and
delivers the calibration finding.

Act 1 — The Reveal (~17 s)
  Title card: "The 6th criterion / Confidence Calibration" with a
  short italic explainer and the closing line "Going in, we expected
  parity. We got something different." (with "something different"
  in yellow to thread the cliffhanger into Act 2).

Act 2 — The Empirical Finding (~21 s)
  Drops the existing report figure (exp3_confidence_calibration.png)
  as a static background. Adds Manim highlight overlays:
    - red ellipse around the CNN's overconfident-zero-IoU stripe
      with callout "high confidence · zero overlap"
    - green ellipse around the SNN's low-confidence + low-IoU cluster
      with callout "wrong — and knows it"

Act 3 — Why It Matters (~16 s)
  Centred title "IMPLICIT UNCERTAINTY SENSOR" with three bullets
  revealed sequentially:
    →  honest confidence drops on uncertain cases
    →  safety-critical for ADAS
    →  no spurious emergency interventions

Total: ~54 s. Pairs with the Beat 7 voiceover trio (7A + 7B + 7C).

Render commands:
  Preview (fast):
      manim -pql calibration_finding.py CalibrationFinding
  Final 1080p:
      manim -pqh calibration_finding.py CalibrationFinding
"""

from manim import *
import numpy as np


CALIBRATION_PNG = (
    "../../report/chapter_3/dnx_results/exp3_confidence_calibration.png"
)


class CalibrationFinding(Scene):
    def construct(self):
        self.camera.background_color = "#000000"

        # =====================================================
        # COLOUR PALETTE
        # =====================================================
        ACCENT_YELLOW = "#F2C94C"
        HIGHLIGHT_GREEN = "#5CC788"
        HIGHLIGHT_RED = "#E15F5F"

        # =====================================================
        # ACT 1 — THE REVEAL
        # =====================================================
        small_label = Text(
            "The 6th criterion",
            font_size=24, color=GREY_B,
        ).move_to([0, 2.40, 0])

        title_word_1 = Text(
            "Confidence", font_size=72, color=WHITE, weight=BOLD,
        )
        title_word_2 = Text(
            "Calibration", font_size=72, color=WHITE, weight=BOLD,
        )
        title_block = (
            VGroup(title_word_1, title_word_2)
            .arrange(DOWN, buff=0.18)
            .move_to([0, 0.60, 0])
        )

        subtitle = Text(
            "how stated certainty tracks actual correctness",
            font_size=22, color=GREY_B, slant=ITALIC,
        ).move_to([0, -1.30, 0])

        # "Going in, we expected parity. We got something different."
        # with "something different" in yellow italic for emphasis
        going_in = Text(
            "Going in, we expected parity.",
            font_size=22, color=GREY_B,
        )
        we_got_pre = Text("We got ", font_size=22, color=GREY_B)
        we_got_emph = Text(
            "something different",
            font_size=22, color=ACCENT_YELLOW, weight=BOLD, slant=ITALIC,
        )
        we_got_period = Text(".", font_size=22, color=GREY_B)
        we_got_line = VGroup(
            we_got_pre, we_got_emph, we_got_period
        ).arrange(RIGHT, buff=0.05)

        bottom_lines = (
            VGroup(going_in, we_got_line)
            .arrange(DOWN, buff=0.18)
            .move_to([0, -2.55, 0])
        )

        # =====================================================
        # ACT 2 — CALIBRATION PLOT
        # =====================================================
        cal_image = ImageMobject(CALIBRATION_PNG)
        cal_image.scale_to_fit_width(11.5)
        cal_image.move_to([0, 0.30, 0])

        # Highlight overlays — positions tuned to the rendered image
        # (image width 11.5, height auto, centred at y=0.30).
        # If the highlight ellipses miss their targets in the v1 render,
        # adjust these coordinates and re-render.

        # CNN zero-IoU stripe — bottom of right panel
        cnn_highlight = Ellipse(
            width=4.4, height=0.55,
            color=HIGHLIGHT_RED,
            stroke_width=3.5,
            fill_opacity=0,
        ).move_to([2.60, -1.62, 0])
        cnn_callout = Text(
            "high confidence  ·  zero overlap",
            font_size=18, color=HIGHLIGHT_RED, slant=ITALIC, weight=BOLD,
        ).next_to(cnn_highlight, UP, buff=0.25)

        # SNN low-confidence + low-IoU cluster — bottom-left of left panel
        snn_highlight = Ellipse(
            width=1.6, height=1.1,
            color=HIGHLIGHT_GREEN,
            stroke_width=3.5,
            fill_opacity=0,
        ).move_to([-3.95, -1.10, 0])
        snn_callout = Text(
            "wrong — and knows it",
            font_size=18, color=HIGHLIGHT_GREEN, slant=ITALIC, weight=BOLD,
        ).next_to(snn_highlight, DOWN, buff=0.25)

        # =====================================================
        # ACT 3 — WHY IT MATTERS
        # =====================================================
        why_title = Text(
            "IMPLICIT UNCERTAINTY SENSOR",
            font_size=36, color=ACCENT_YELLOW, weight=BOLD,
        ).move_to([0, 1.80, 0])

        why_divider = Line(
            np.array([-3.50, 1.00, 0]),
            np.array([3.50, 1.00, 0]),
            color=GREY_C,
            stroke_width=1.0,
        )

        bullets_text = [
            "honest confidence drops on uncertain cases",
            "safety-critical for ADAS",
            "no spurious emergency interventions",
        ]
        bullets = []
        for text in bullets_text:
            arrow_marker = Text(
                "→", font_size=24, color=ACCENT_YELLOW, weight=BOLD,
            )
            label = Text(text, font_size=22, color=WHITE)
            row = VGroup(arrow_marker, label).arrange(RIGHT, buff=0.30)
            bullets.append(row)
        bullets_group = (
            VGroup(*bullets)
            .arrange(DOWN, buff=0.45, aligned_edge=LEFT)
            .move_to([0, -0.70, 0])
        )

        # =====================================================
        # ANIMATION SEQUENCE  (~54 s)
        # =====================================================

        # ---------- Act 1: The Reveal (~17 s) ----------
        self.play(Write(small_label), run_time=0.5)
        self.play(
            FadeIn(title_word_1, scale=1.10),
            FadeIn(title_word_2, scale=1.10),
            run_time=1.5,
        )
        self.play(FadeIn(subtitle, shift=UP * 0.20), run_time=0.7)
        self.wait(2.5)
        self.play(FadeIn(bottom_lines, shift=UP * 0.20), run_time=1.0)
        self.wait(8.0)

        # Transition Act 1 → Act 2
        act1_group = VGroup(
            small_label, title_block, subtitle, bottom_lines,
        )
        self.play(FadeOut(act1_group), run_time=0.8)

        # ---------- Act 2: Calibration Plot (~21 s) ----------
        self.play(FadeIn(cal_image), run_time=1.2)
        self.wait(1.0)

        # CNN highlight first (voiceover names CNN before SNN)
        self.play(Create(cnn_highlight), run_time=0.8)
        self.play(FadeIn(cnn_callout, shift=DOWN * 0.20), run_time=0.7)
        self.wait(4.5)

        # SNN highlight
        self.play(Create(snn_highlight), run_time=0.8)
        self.play(FadeIn(snn_callout, shift=UP * 0.20), run_time=0.7)
        self.wait(11.0)

        # Transition Act 2 → Act 3
        act2_group = Group(
            cal_image, cnn_highlight, cnn_callout,
            snn_highlight, snn_callout,
        )
        self.play(FadeOut(act2_group), run_time=0.8)

        # ---------- Act 3: Why It Matters (~16 s) ----------
        self.play(FadeIn(why_title, scale=1.05), run_time=1.0)
        self.play(Create(why_divider), run_time=0.5)
        for bullet in bullets:
            self.play(FadeIn(bullet, shift=LEFT * 0.20), run_time=0.7)
        self.wait(11.0)
