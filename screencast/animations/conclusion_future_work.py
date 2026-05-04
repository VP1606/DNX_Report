"""
Conclusion + Future Work — Beat 8
DetectorNX Screencast — Closing beat

Three-phase animation that closes the screencast.

Phase 1 — Three Takeaways triptych (~42 s)
  Vertical list with three rows, each lighting up as the voiceover
  names it:
    1. THE COST              — ~5% mIoU
    2. THE BENEFIT           — 94% energy reduction
    3. THE UNEXPECTED FINDING — Implicit uncertainty sensor

Phase 2 — Future Work card (~22 s)
  Tricolon "Spiking is viable. Not theoretical. Viable." with the
  final "Viable." in SNN-green for emphasis. Three future-work
  arrows below:
    →  Multi-class generalisation
    →  SNN-native classification head
    →  Neuromorphic hardware deployment (Loihi 2)

Phase 3 — Closing title card (~10 s)
  Centred:
    "Thanks for watching."
    DetectorNX
    Premakantha Varun
    BSc Computer Science · University of Manchester · 2026

Total: ~75 s.

Render commands:
  Preview (fast):
      manim -pql conclusion_future_work.py ConclusionFutureWork
  Final 1080p:
      manim -pqh conclusion_future_work.py ConclusionFutureWork
"""

from manim import *
import numpy as np


class ConclusionFutureWork(Scene):
    def construct(self):
        self.camera.background_color = "#000000"

        # =====================================================
        # COLOUR PALETTE
        # =====================================================
        SNN_COLOR = "#73C49B"
        COST_COLOR = "#E07A5F"
        ACCENT_YELLOW = "#F2C94C"

        # =====================================================
        # PHASE 1 — THREE TAKEAWAYS
        # =====================================================
        title = Text(
            "THE TAKEAWAYS",
            font_size=28, color=GREY_B, weight=BOLD,
        ).to_edge(UP, buff=0.50)

        takeaway_specs = [
            {
                "n": "1",
                "category": "THE COST",
                "headline": "~5% mIoU",
                "subtitle": "precision cost · variable-isolated",
                "color": COST_COLOR,
            },
            {
                "n": "2",
                "category": "THE BENEFIT",
                "headline": "94% energy reduction",
                "subtitle": "+ reactive scalability",
                "color": SNN_COLOR,
            },
            {
                "n": "3",
                "category": "THE UNEXPECTED FINDING",
                "headline": "Implicit uncertainty sensor",
                "subtitle": "safety-critical for ADAS",
                "color": ACCENT_YELLOW,
            },
        ]
        # y-centres for each takeaway block
        y_centres = [2.30, 0.30, -1.70]

        takeaways = []
        for spec, y in zip(takeaway_specs, y_centres):
            cat_label = Text(
                f"{spec['n']}.   {spec['category']}",
                font_size=20, color=GREY_C, weight=BOLD,
            )
            headline = Text(
                spec["headline"],
                font_size=36, color=spec["color"], weight=BOLD,
            )
            subtitle = Text(
                spec["subtitle"],
                font_size=18, color=GREY_B, slant=ITALIC,
            )
            block = VGroup(cat_label, headline, subtitle).arrange(
                DOWN, buff=0.18, aligned_edge=LEFT,
            ).move_to([0, y, 0])
            takeaways.append(block)

        # =====================================================
        # PHASE 2 — FUTURE WORK CARD
        # =====================================================
        viable_line_1 = Text(
            "Spiking is viable.",
            font_size=44, color=WHITE, weight=BOLD,
        )
        viable_line_2 = Text(
            "Not theoretical.",
            font_size=44, color=WHITE, weight=BOLD,
        )
        viable_line_3 = Text(
            "Viable.",
            font_size=52, color=SNN_COLOR, weight=BOLD,
        )
        viable_block = VGroup(
            viable_line_1, viable_line_2, viable_line_3
        ).arrange(DOWN, buff=0.20).move_to([0, 1.50, 0])

        future_divider = Line(
            np.array([-3.5, -0.20, 0]),
            np.array([3.5, -0.20, 0]),
            color=GREY_C, stroke_width=1,
        )

        future_bullets_text = [
            "Multi-class generalisation",
            "SNN-native classification head",
            "Neuromorphic hardware deployment  (Loihi 2)",
        ]
        future_bullets = []
        for text in future_bullets_text:
            arr = Text("→", font_size=24, color=ACCENT_YELLOW, weight=BOLD)
            label = Text(text, font_size=22, color=WHITE)
            row = VGroup(arr, label).arrange(RIGHT, buff=0.30)
            future_bullets.append(row)
        future_bullets_group = (
            VGroup(*future_bullets)
            .arrange(DOWN, buff=0.40, aligned_edge=LEFT)
            .move_to([0, -1.75, 0])
        )

        # =====================================================
        # PHASE 3 — CLOSING TITLE CARD
        # =====================================================
        thanks_line = Text(
            "Thanks for watching.",
            font_size=42, color=WHITE, weight=BOLD,
        ).move_to([0, 2.10, 0])

        project_name = Text(
            "DetectorNX",
            font_size=72, color=WHITE, weight=BOLD,
        ).move_to([0, 0.40, 0])

        author_name = Text(
            "Premakantha Varun",
            font_size=28, color=GREY_B,
        ).move_to([0, -1.20, 0])

        university_line = Text(
            "BSc Computer Science  ·  University of Manchester  ·  2026",
            font_size=20, color=GREY_C,
        ).move_to([0, -1.85, 0])

        # =====================================================
        # ANIMATION SEQUENCE  (~75 s)
        # =====================================================

        # ---------- Phase 1: Three Takeaways  (~46 s) ----------
        self.play(Write(title), run_time=0.7)
        self.wait(2.5)  # voiceover: "So the takeaways are threefold."

        for tk in takeaways:
            cat_label, headline, subtitle = tk[0], tk[1], tk[2]
            self.play(FadeIn(cat_label, shift=LEFT * 0.30), run_time=0.6)
            self.play(FadeIn(headline, scale=1.05), run_time=1.0)
            self.play(FadeIn(subtitle), run_time=0.5)
            self.wait(11.0)

        # ---------- Phase 2 transition: fade out takeaways  (~1 s) ----------
        all_takeaways = VGroup(*takeaways, title)
        self.play(FadeOut(all_takeaways), run_time=0.9)

        # ---------- Phase 2: Future work card  (~22 s) ----------
        # The viable tricolon — three short sentences, last one in green
        self.play(FadeIn(viable_line_1, shift=UP * 0.20), run_time=0.7)
        self.play(FadeIn(viable_line_2, shift=UP * 0.20), run_time=0.7)
        self.play(FadeIn(viable_line_3, shift=UP * 0.20, scale=1.1), run_time=1.0)
        self.wait(3.5)
        self.play(Create(future_divider), run_time=0.5)
        for bullet in future_bullets:
            self.play(FadeIn(bullet, shift=LEFT * 0.20), run_time=0.7)
        self.wait(7.5)

        # ---------- Phase 3 transition: fade to closing card  (~1 s) ----------
        future_work_group = VGroup(
            viable_block, future_divider, future_bullets_group,
        )
        self.play(FadeOut(future_work_group), run_time=0.9)

        # ---------- Phase 3: Closing title card  (~9 s) ----------
        self.play(FadeIn(thanks_line, shift=UP * 0.20), run_time=0.9)
        self.play(FadeIn(project_name, scale=1.05), run_time=1.0)
        self.play(
            FadeIn(author_name),
            FadeIn(university_line),
            run_time=0.8,
        )
        self.wait(5.0)
