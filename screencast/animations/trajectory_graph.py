"""
Trajectory Graph — Sub-beat 2C
DetectorNX Screencast — Beat 2 (Motivation + ADAS Demo)

Animates the "compute demand vs onboard power budget" graph that closes
the motivation section. Total animation length ~13 sec, matching the
voiceover timing for the graph segment of Sub-beat 2C.

Render commands:
  Preview (fast, low quality):
      manim -pql trajectory_graph.py TrajectoryGraph

  Final (high quality, 1080p):
      manim -pqh trajectory_graph.py TrajectoryGraph

  Final (4K):
      manim -pqk trajectory_graph.py TrajectoryGraph

Output goes to:
  media/videos/trajectory_graph/{quality}/TrajectoryGraph.mp4

The MP4 can be dragged directly into a Keynote slide.
"""

from manim import *
import numpy as np


class TrajectoryGraph(Scene):
    def construct(self):
        # Pure black background
        self.camera.background_color = "#000000"

        # =====================================================
        # SETUP — Title and Axes
        # =====================================================

        title = Text(
            "Compute demand vs onboard power budget",
            font_size=30,
            color=WHITE,
        ).to_edge(UP, buff=0.4)

        axes = Axes(
            x_range=[2015, 2030, 1],
            y_range=[0, 1100, 200],
            x_length=11,
            y_length=5,
            axis_config={
                "color": GREY_B,
                "include_tip": False,
                "stroke_width": 2,
            },
            x_axis_config={
                "numbers_to_include": [2015, 2018, 2021, 2024, 2027, 2030],
                "decimal_number_config": {
                    "num_decimal_places": 0,
                    "group_with_commas": False,
                },
                "font_size": 24,
            },
            y_axis_config={
                "numbers_to_include": [200, 400, 600, 800, 1000],
                "font_size": 24,
            },
        ).shift(DOWN * 0.4)

        x_label = Text("Year", font_size=24, color=GREY_B).next_to(
            axes.x_axis, DOWN, buff=0.3
        )
        y_label = (
            Text("Power (W)", font_size=24, color=GREY_B)
            .rotate(PI / 2)
            .next_to(axes.y_axis, LEFT, buff=0.3)
        )

        # =====================================================
        # CURVE FUNCTIONS
        # =====================================================

        # Onboard power budget: industry target of ~200 W for
        # mass-market autonomous-perception ECUs. Constrained by
        # thermal envelope, battery range impact, and packaging.
        # Effectively flat across the timeline.
        def power_budget(x):
            return 200

        # Compute demand: exponential rise from conventional
        # ECU territory (~30 W in 2015) toward L4 autonomy
        # (~1000 W in 2030). Crosses the budget around the
        # L3 self-driving transition.
        # Calibrated to: f(2015) = 30 W, f(2030) = 1000 W
        def compute_demand(x):
            return 30 * np.exp((x - 2015) * 0.234)

        budget_curve = axes.plot(
            power_budget,
            x_range=[2015, 2030],
            color=GREEN,
            stroke_width=4,
        )

        compute_curve = axes.plot(
            compute_demand,
            x_range=[2015, 2030],
            color=RED,
            stroke_width=4,
        )

        # Curve labels — placed in EMPTY quadrants of the chart
        # to avoid colliding with markers or each other.

        # Budget label sits ABOVE the budget line on the LEFT,
        # in the gap between the line and where the compute curve
        # arrives — keeps the cramped area below the line free
        # for the L2 marker callout.
        budget_curve_label = Text(
            "Industry power target (~200 W)",
            font_size=22,
            color=GREEN,
        ).next_to(
            axes.coords_to_point(2017, power_budget(2017)),
            UP,
            buff=0.2,
        )

        # Compute-demand label floats in the TOP-LEFT quadrant
        # (years ≈ 2017–2020, watts ≈ 600–800), which is empty
        # — the curve doesn't reach those y values until ~2028.
        compute_curve_label = Text(
            "Compute demand",
            font_size=22,
            color=RED,
        ).move_to(axes.coords_to_point(2018.5, 700))

        # =====================================================
        # AUTONOMY-TIER MARKERS
        # =====================================================

        # Conventional ECU territory (today, well below budget)
        l2_x = 2018
        l2_y = compute_demand(l2_x)
        l2_dot = Dot(
            axes.coords_to_point(l2_x, l2_y),
            color=BLUE,
            radius=0.1,
        )
        # Label sits in the open band between the L2 dot and
        # the budget line, well clear of the "2018" x-axis tick.
        l2_label = VGroup(
            Text("Conventional ECU", font_size=20, color=BLUE),
            Text("(< 50 W)", font_size=14, color=GREY_B),
        ).arrange(DOWN, buff=0.05).move_to(
            axes.coords_to_point(2017.5, 110)
        )
        l2_connector = DashedLine(
            l2_dot.get_center(),
            l2_label.get_bottom(),
            color=BLUE,
            stroke_width=1.5,
            dash_length=0.08,
        )

        # L3 self-driving (crosses budget — saturation point)
        l3_x = 2024
        l3_y = compute_demand(l3_x)
        l3_dot = Dot(
            axes.coords_to_point(l3_x, l3_y),
            color=YELLOW,
            radius=0.1,
        )
        # Label placed straight RIGHT of the dot at roughly
        # the same y-level — keeps the "L3 = crosses the
        # budget" reading visually intact.
        l3_label = VGroup(
            Text("L3 self-driving", font_size=20, color=YELLOW),
            Text("(200–350 W)", font_size=14, color=GREY_B),
        ).arrange(DOWN, buff=0.05).move_to(
            axes.coords_to_point(2026.5, 250)
        )
        l3_connector = DashedLine(
            l3_dot.get_center(),
            l3_label.get_left(),
            color=YELLOW,
            stroke_width=1.5,
            dash_length=0.08,
        )

        # L4 autonomy (far above budget)
        l4_x = 2030
        l4_y = compute_demand(l4_x)
        l4_dot = Dot(
            axes.coords_to_point(l4_x, l4_y),
            color=ORANGE,
            radius=0.1,
        )
        # Label placed straight LEFT of the dot in the open
        # top-band of the chart (above where the curve passes
        # through year 2027 ≈ 500 W).
        l4_label = VGroup(
            Text("L4 autonomy", font_size=20, color=ORANGE),
            Text("(~1000 W)", font_size=14, color=GREY_B),
        ).arrange(DOWN, buff=0.05).move_to(
            axes.coords_to_point(2026.5, 1000)
        )
        l4_connector = DashedLine(
            l4_dot.get_center(),
            l4_label.get_right(),
            color=ORANGE,
            stroke_width=1.5,
            dash_length=0.08,
        )

        # =====================================================
        # FINAL CUE — arrow + question (pointing DOWN)
        # =====================================================
        # Arrow points downward from the L4 dot toward the
        # budget line, gesturing "we need to bring this demand
        # DOWN to fit the budget" — exactly what the spiking
        # paradigm answers.

        arrow_start = axes.coords_to_point(l4_x, l4_y)
        arrow_end = axes.coords_to_point(l4_x, 350)
        forward_arrow = Arrow(
            start=arrow_start,
            end=arrow_end,
            color=WHITE,
            stroke_width=4,
            buff=0.15,
            max_tip_length_to_length_ratio=0.15,
        )
        question_mark = Text(
            "?",
            font_size=64,
            color=WHITE,
            weight=BOLD,
        ).next_to(forward_arrow.get_end(), DOWN, buff=0.15)

        # =====================================================
        # ANIMATION SEQUENCE (~13 sec total)
        # =====================================================

        # Step 1: Title + axes  (1.8 sec)
        self.play(Write(title), run_time=0.8)
        self.play(
            Create(axes),
            Write(x_label),
            Write(y_label),
            run_time=1.0,
        )

        # Step 2: Power budget line  (1.5 sec)
        self.play(
            Create(budget_curve),
            run_time=1.0,
        )
        self.play(
            FadeIn(budget_curve_label, shift=UP * 0.2),
            run_time=0.5,
        )

        # Step 3: Compute demand curve grows  (2.5 sec)
        self.play(
            Create(compute_curve),
            run_time=2.0,
        )
        self.play(
            FadeIn(compute_curve_label, shift=DOWN * 0.2),
            run_time=0.5,
        )

        # Step 4: Conventional ECU marker (well below budget)  (1.3 sec)
        self.play(
            GrowFromCenter(l2_dot),
            Create(l2_connector),
            FadeIn(l2_label),
            run_time=1.3,
        )

        # Step 5: L3 self-driving marker (crosses budget)  (1.3 sec)
        self.play(
            GrowFromCenter(l3_dot),
            Create(l3_connector),
            FadeIn(l3_label),
            run_time=1.3,
        )

        # Step 6: L4 autonomy marker (far above budget)  (1.3 sec)
        self.play(
            GrowFromCenter(l4_dot),
            Create(l4_connector),
            FadeIn(l4_label),
            run_time=1.3,
        )

        # Step 7: Forward arrow + question mark  (1.6 sec)
        self.play(
            GrowArrow(forward_arrow),
            run_time=0.8,
        )
        self.play(
            Write(question_mark),
            run_time=0.8,
        )

        # Step 8: Hold the final composition  (1.0 sec)
        # Allows the voiceover "calling for a fundamentally
        # different approach" to land while the visual rests.
        self.wait(1.0)
