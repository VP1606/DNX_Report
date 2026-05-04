"""
Real-Time + Bridge — Sub-beat 6C
DetectorNX Screencast — Beat 6 (Results), closing sub-beat

Three-act animation that closes the Results section and hands off to
Beat 7 (the calibration finding).

Act 1 — Speed reveal (~13 s)
  - Big "259.80" landing as the headline FPS number
  - Horizontal bar from 0 to 300 FPS, with the SNN's 259.80 FPS shown
    as a filled green portion
  - 30 FPS real-time threshold marked as a yellow vertical tick close
    to the left edge of the bar
  - "8.6× safety margin" callout below

Act 2 — Six success criteria (~14 s)
  - Numbered list of the six pre-defined success criteria, each
    landing with a green tick as the voiceover names it
  - The sixth criterion — Confidence calibration — gets a yellow tick
    plus a small "?" marker, visually planting the seed for the
    cliffhanger

Act 3 — Bridge to Beat 7 (~7 s)
  - The other five criteria fade out, leaving Confidence calibration
    centred on screen
  - Italic text fades in below: "...one of those produced a result we
    didn't expect."

Total: ~40 s. Pairs with the Sub-beat 6C voiceover.

Render commands:
  Preview (fast):
      manim -pql realtime_bridge.py RealTimeBridge
  Final 1080p:
      manim -pqh realtime_bridge.py RealTimeBridge
"""

from manim import *
import numpy as np


class RealTimeBridge(Scene):
    def construct(self):
        self.camera.background_color = "#000000"

        # =====================================================
        # COLOUR PALETTE
        # =====================================================
        SNN_COLOR = "#73C49B"
        ACCENT_YELLOW = "#F2C94C"
        TICK_COLOR_GREEN = "#73C49B"
        TICK_COLOR_YELLOW = "#F2C94C"

        # =====================================================
        # ACT 1 — SPEED REVEAL ELEMENTS
        # =====================================================
        title_act1 = Text(
            "Real-time throughput",
            font_size=28, color=GREY_B,
        ).to_edge(UP, buff=0.40)

        fps_number = Text(
            "259.80",
            font_size=120, color=SNN_COLOR, weight=BOLD,
        ).move_to([0, 1.30, 0])

        fps_unit = Text(
            "frames per second on GPU hardware",
            font_size=22, color=GREY_B,
        ).next_to(fps_number, DOWN, buff=0.30)

        # Horizontal bar visualisation — 0 to 300 FPS scale
        scale_y = -1.80
        bar_left = -5.0
        bar_right = 5.0
        bar_width_total = bar_right - bar_left  # 10 units = 300 FPS

        # Background scale (empty)
        scale_bg = Rectangle(
            width=bar_width_total, height=0.35,
            fill_color="#1A1A22",
            fill_opacity=0.7,
            stroke_color=GREY_D,
            stroke_width=1,
        ).move_to([0, scale_y, 0])

        # SNN filled bar (0 to 259.80 FPS)
        snn_bar_width = (259.80 / 300.0) * bar_width_total  # ~8.66
        snn_bar = Rectangle(
            width=snn_bar_width, height=0.35,
            fill_color=SNN_COLOR,
            fill_opacity=0.75,
            stroke_color=SNN_COLOR,
            stroke_width=1.5,
        ).move_to([bar_left + snn_bar_width / 2, scale_y, 0])

        # 30 FPS threshold tick (yellow, vertical)
        threshold_x = bar_left + (30.0 / 300.0) * bar_width_total  # -4.0
        threshold_tick = Line(
            np.array([threshold_x, scale_y - 0.30, 0]),
            np.array([threshold_x, scale_y + 0.30, 0]),
            color=ACCENT_YELLOW,
            stroke_width=4,
        )
        threshold_label = Text(
            "30 FPS\nreal-time threshold",
            font_size=14,
            color=ACCENT_YELLOW,
            line_spacing=0.7,
        ).next_to(threshold_tick, DOWN, buff=0.20)

        # SNN value label at end of bar
        snn_value_x = bar_left + snn_bar_width
        snn_value_label = Text(
            "259.80 FPS",
            font_size=14, color=SNN_COLOR, weight=BOLD,
        ).next_to(np.array([snn_value_x, scale_y, 0]), UP, buff=0.30)

        # 8.6× margin callout
        margin_callout = Text(
            "8.6× safety margin over the real-time threshold",
            font_size=22, color=ACCENT_YELLOW, weight=BOLD,
        ).to_edge(DOWN, buff=0.80)

        # =====================================================
        # ACT 2 — SUCCESS CRITERIA TABLE
        # =====================================================
        title_act2 = Text(
            "Six pre-defined success criteria",
            font_size=28, color=WHITE, weight=BOLD,
        ).to_edge(UP, buff=0.40)

        criteria_data = [
            ("Precision parity",          TICK_COLOR_GREEN),
            ("Energy efficiency",         TICK_COLOR_GREEN),
            ("Real-time throughput",      TICK_COLOR_GREEN),
            ("Parameter parity",          TICK_COLOR_GREEN),
            ("Detection completeness",    TICK_COLOR_GREEN),
            ("Confidence calibration",    TICK_COLOR_YELLOW),  # special
        ]
        criteria_rows = []
        for label_text, tick_color in criteria_data:
            tick = Text("✓", font_size=30, color=tick_color, weight=BOLD)
            label = Text(label_text, font_size=24, color=WHITE)
            row = VGroup(tick, label).arrange(RIGHT, buff=0.35)
            criteria_rows.append(row)

        criteria_list = (
            VGroup(*criteria_rows)
            .arrange(DOWN, buff=0.32, aligned_edge=LEFT)
            .move_to([0, -0.30, 0])
        )

        # "?" question marker for the calibration row (added in Act 2 close,
        # held into Act 3 to plant the cliffhanger seed).
        question_marker = Text(
            "?", font_size=28, color=ACCENT_YELLOW, weight=BOLD,
        ).next_to(criteria_rows[-1], RIGHT, buff=0.45)

        # =====================================================
        # ACT 3 — BRIDGE TO BEAT 7
        # =====================================================
        bridge_text = Text(
            "...one of those produced a result we didn't expect.",
            font_size=28, color=WHITE, slant=ITALIC,
        ).move_to([0, -1.50, 0])

        # =====================================================
        # ANIMATION SEQUENCE  (~40 s)
        # =====================================================

        # ---------- Act 1: Speed reveal  (~13 s) ----------
        self.play(Write(title_act1), run_time=0.6)
        self.play(FadeIn(fps_number, scale=1.10), run_time=1.1)
        self.play(Write(fps_unit), run_time=0.6)

        # Bar setup
        self.play(
            FadeIn(scale_bg),
            run_time=0.5,
        )
        self.play(
            FadeIn(threshold_tick, scale=1.2),
            Write(threshold_label),
            run_time=0.8,
        )
        # SNN bar grows from left to right
        self.play(
            GrowFromEdge(snn_bar, LEFT),
            run_time=1.4,
        )
        self.play(Write(snn_value_label), run_time=0.5)
        self.play(FadeIn(margin_callout, shift=UP * 0.20), run_time=0.7)
        self.wait(7.0)

        # ---------- Transition Act 1 → Act 2 (~0.9 s) ----------
        act1_group = VGroup(
            title_act1, fps_number, fps_unit,
            scale_bg, snn_bar,
            threshold_tick, threshold_label,
            snn_value_label, margin_callout,
        )
        self.play(FadeOut(act1_group), run_time=0.9)

        # ---------- Act 2: Success criteria (~14 s) ----------
        self.play(Write(title_act2), run_time=0.7)
        # Reveal first 5 with green ticks, paced to voiceover delivery
        for row in criteria_rows[:-1]:
            self.play(FadeIn(row, shift=LEFT * 0.20), run_time=0.7)
        # Reveal the 6th (calibration) with the yellow tick
        self.play(FadeIn(criteria_rows[-1], shift=LEFT * 0.20), run_time=0.8)
        # Add the "?" marker
        self.play(FadeIn(question_marker, scale=1.30), run_time=0.4)
        self.wait(6.0)

        # ---------- Transition Act 2 → Act 3 (~1.7 s) ----------
        first_five = VGroup(*criteria_rows[:-1])
        self.play(
            FadeOut(first_five),
            FadeOut(title_act2),
            run_time=0.9,
        )
        # Move the calibration row + its "?" marker as a single group
        cal_group = VGroup(criteria_rows[-1], question_marker)
        self.play(
            cal_group.animate.move_to([0, 0.50, 0]),
            run_time=0.8,
        )
        cal_row = criteria_rows[-1]

        # ---------- Act 3: Bridge text (~7 s) ----------
        self.play(
            Indicate(cal_row, scale_factor=1.10, color=ACCENT_YELLOW),
            run_time=0.8,
        )
        self.play(FadeIn(bridge_text, shift=UP * 0.30), run_time=0.8)
        self.wait(4.0)
