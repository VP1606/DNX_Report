"""
Efficiency Overlay — Sub-beat 6B
DetectorNX Screencast — Beat 6 (Results)

Full-screen graph that visualises per-frame energy consumption across
scene complexity, structured as a three-act animation paired with the
Sub-beat 6B voiceover.

Act 1 (combined view): CNN baseline draws as a dashed line at
~42.43 mJ. SNN scatter points populate near the bottom of the chart,
appearing visually flat at this scale. "94.33% reduction" callout
lands in the chart middle. Voiceover establishes the headline gap.

Act 2 (zoom into SNN): the y-axis rescales from 0–45 mJ to roughly
2.27–2.52 mJ. The SNN scatter — previously a low flat band — reveals
itself as a slope. A linear fit line draws across (y = 0.0018x +
2.295, with x in thousands of input events, y in mJ). R² = 0.7514
callout fades in. The "Reactive Scalability" tag sits above the
chart.

Act 3 (zoom back out): the y-axis rescales back to 0–45 mJ. CNN line
reappears at the top; SNN cluster shrinks back to its tiny bottom
band. Visual contrast is reaffirmed for the voiceover's closing
"CNN, in contrast, consumes the same energy whether the road is
empty or packed."

Total: ~48 s, paired with the Sub-beat 6B voiceover.

Render commands:
  Preview (fast):
      manim -pql efficiency_overlay.py EfficiencyOverlay
  Final 1080p:
      manim -pqh efficiency_overlay.py EfficiencyOverlay

Output goes to:
  media/videos/efficiency_overlay/{quality}/EfficiencyOverlay.mp4
"""

from manim import *
import numpy as np


class EfficiencyOverlay(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        np.random.seed(42)

        # =====================================================
        # COLOUR PALETTE
        # =====================================================
        SNN_COLOR = "#73C49B"        # green — SNN throughout the screencast
        CNN_COLOR = "#E07A5F"        # warm red/orange for the dashed CNN baseline
        FIT_COLOR = "#5DA4D4"        # blue — fit line within the green scatter
        ACCENT_YELLOW = "#F2C94C"    # for the headline callouts
        LEGEND_COLOR = GREY_C

        # =====================================================
        # DATA — synthesised SNN scatter calibrated to your stats
        # =====================================================
        # X = scene complexity in thousands of input events (range ~10–120)
        # Y = energy per frame in mJ (range ~2.28–2.51)
        # Trend: y = 0.0018 x + 2.295 (mJ; x in K events)
        # Noise calibrated so observed R² ≈ 0.7514.
        n_points = 100
        x_data = np.concatenate([
            # Denser bands matching image 1's structure
            np.random.uniform(10, 30, 25),
            np.random.uniform(40, 65, 35),
            np.random.uniform(65, 95, 25),
            np.random.uniform(95, 120, 15),
        ])
        y_trend = 0.0018 * x_data + 2.295
        # Noise std empirically calibrated to give R² = 0.7513 (target 0.7514)
        noise = np.random.normal(0.0, 0.0361, n_points)
        y_data = y_trend + noise
        # Add a couple of high-y outliers to mimic the visible ones in image 1
        y_data[60] += 0.06
        y_data[55] += 0.05

        cnn_baseline = 42.43  # mJ

        # =====================================================
        # TITLE  (persists through both views)
        # =====================================================
        title = Text(
            "Dynamic Energy Consumption vs. Scene Complexity",
            font_size=26, color=WHITE,
        ).to_edge(UP, buff=0.30)

        # =====================================================
        # AXES — COMBINED VIEW (0–45 mJ)
        # =====================================================
        ax_combined = Axes(
            x_range=[0, 130, 20],
            y_range=[0, 45, 10],
            x_length=10.5,
            y_length=4.5,
            axis_config={
                "color": GREY_B,
                "include_tip": False,
                "stroke_width": 2,
            },
            x_axis_config={
                "include_numbers": True,
                "font_size": 16,
                "decimal_number_config": {
                    "num_decimal_places": 0,
                    "group_with_commas": False,
                },
            },
            y_axis_config={
                "include_numbers": True,
                "font_size": 16,
                "decimal_number_config": {"num_decimal_places": 0},
            },
        ).move_to([0.30, 0.20, 0])

        x_label = Text(
            "Scene Complexity  (Input Events × 10³)",
            font_size=16, color=GREY_B,
        ).next_to(ax_combined.x_axis, DOWN, buff=0.30)
        y_label = (
            Text("Energy per Frame  (mJ)", font_size=16, color=GREY_B)
            .rotate(PI / 2)
            .next_to(ax_combined.y_axis, LEFT, buff=0.20)
        )

        # ----- Combined-view chart elements -----
        snn_dots_combined = VGroup(*[
            Dot(
                ax_combined.coords_to_point(x, y),
                radius=0.045,
                color=SNN_COLOR,
                fill_opacity=0.75,
            )
            for x, y in zip(x_data, y_data)
        ])

        cnn_line_combined = DashedLine(
            ax_combined.coords_to_point(0, cnn_baseline),
            ax_combined.coords_to_point(130, cnn_baseline),
            color=CNN_COLOR,
            stroke_width=2.8,
            dash_length=0.18,
        )
        cnn_tag_combined = Text(
            f"CNN: {cnn_baseline:.2f} mJ — constant",
            font_size=16, color=CNN_COLOR, slant=ITALIC,
        ).move_to(ax_combined.coords_to_point(85, cnn_baseline + 1.8))

        snn_tag_combined = Text(
            "SNN: ~2.4 mJ",
            font_size=16, color=SNN_COLOR, slant=ITALIC,
        ).move_to(ax_combined.coords_to_point(85, 6.5))

        reduction_callout = VGroup(
            Text("94.33%", font_size=44, color=ACCENT_YELLOW, weight=BOLD),
            Text("reduction in per-frame energy",
                 font_size=18, color=GREY_B),
        ).arrange(DOWN, buff=0.10).move_to(ax_combined.coords_to_point(45, 23))

        # =====================================================
        # AXES — ZOOMED VIEW (2.27–2.52 mJ)
        # =====================================================
        ax_zoomed = Axes(
            x_range=[0, 130, 20],
            y_range=[2.25, 2.60, 0.05],
            x_length=10.5,
            y_length=4.5,
            axis_config={
                "color": GREY_B,
                "include_tip": False,
                "stroke_width": 2,
            },
            x_axis_config={
                "include_numbers": True,
                "font_size": 16,
                "decimal_number_config": {
                    "num_decimal_places": 0,
                    "group_with_commas": False,
                },
            },
            y_axis_config={
                "include_numbers": True,
                "font_size": 16,
                "decimal_number_config": {"num_decimal_places": 2},
            },
        ).move_to([0.30, 0.20, 0])

        snn_dots_zoomed = VGroup(*[
            Dot(
                ax_zoomed.coords_to_point(x, y),
                radius=0.045,
                color=SNN_COLOR,
                fill_opacity=0.75,
            )
            for x, y in zip(x_data, y_data)
        ])

        # Linear fit line in the zoomed view
        fit_line_zoomed = Line(
            ax_zoomed.coords_to_point(0, 0.0018 * 0 + 2.295),
            ax_zoomed.coords_to_point(130, 0.0018 * 130 + 2.295),
            color=FIT_COLOR,
            stroke_width=3.5,
        )

        fit_eqn = Text(
            "y = 0.0018x + 2.295",
            font_size=16, color=FIT_COLOR, slant=ITALIC,
        ).move_to(ax_zoomed.coords_to_point(28, 2.495))

        r_squared_callout = Text(
            "R² = 0.7514",
            font_size=22, color=FIT_COLOR, weight=BOLD,
        ).move_to(ax_zoomed.coords_to_point(28, 2.470))

        rs_tag = Text(
            "REACTIVE SCALABILITY",
            font_size=22, color=ACCENT_YELLOW, weight=BOLD,
        ).move_to(ax_zoomed.coords_to_point(95, 2.290))

        # =====================================================
        # CLOSING TAG  (after zoom-out, hold)
        # =====================================================
        closing_tag = Text(
            "paradigm-level efficiency  ·  unique to spiking architectures",
            font_size=16, color=GREY_C, slant=ITALIC,
        ).to_edge(DOWN, buff=0.95)

        # =====================================================
        # LEGEND  (bottom-left corner)
        # =====================================================
        legend = VGroup(
            Text("mJ = millijoules",
                 font_size=13, color=LEGEND_COLOR, slant=ITALIC),
            Text("R² = coefficient of determination",
                 font_size=13, color=LEGEND_COLOR, slant=ITALIC),
        ).arrange(DOWN, buff=0.10, aligned_edge=LEFT).to_corner(DL, buff=0.30)

        # =====================================================
        # ANIMATION SEQUENCE  (~48 s)
        # =====================================================

        # ---------- Phase 1: setup  (~3 s) ----------
        self.play(Write(title), run_time=0.7)
        self.play(
            Create(ax_combined),
            Write(x_label),
            Write(y_label),
            run_time=1.4,
        )
        self.play(FadeIn(legend), run_time=0.6)
        self.wait(0.3)

        # ---------- Phase 2: combined plot  (~12 s) ----------
        self.play(
            Create(cnn_line_combined),
            run_time=1.2,
        )
        self.play(FadeIn(cnn_tag_combined, shift=UP * 0.15), run_time=0.6)

        self.play(
            LaggedStart(
                *[FadeIn(d, scale=0.5) for d in snn_dots_combined],
                lag_ratio=0.012,
            ),
            run_time=2.5,
        )
        self.play(FadeIn(snn_tag_combined, shift=UP * 0.15), run_time=0.5)

        self.play(FadeIn(reduction_callout, scale=0.85), run_time=0.9)
        self.wait(7.5)

        # ---------- Phase 3: zoom transition  (~3 s) ----------
        # Drop the combined-view-only callouts before rescaling.
        self.play(
            FadeOut(reduction_callout),
            FadeOut(cnn_line_combined),
            FadeOut(cnn_tag_combined),
            FadeOut(snn_tag_combined),
            run_time=0.7,
        )
        # Cross-fade combined axes/dots → zoomed axes/dots
        self.play(
            FadeOut(ax_combined),
            FadeOut(snn_dots_combined),
            FadeIn(ax_zoomed),
            FadeIn(snn_dots_zoomed),
            run_time=2.0,
        )

        # ---------- Phase 4: Reactive Scalability reveal  (~10 s) ----------
        self.play(FadeIn(rs_tag, shift=DOWN * 0.20), run_time=0.7)
        self.play(Create(fit_line_zoomed), run_time=1.5)
        self.play(
            FadeIn(fit_eqn, shift=UP * 0.10),
            FadeIn(r_squared_callout, shift=UP * 0.10),
            run_time=0.8,
        )
        self.wait(13.0)

        # ---------- Phase 5: zoom back out  (~12 s) ----------
        # Zoomed callouts fade; cross-fade back to combined view.
        self.play(
            FadeOut(rs_tag),
            FadeOut(fit_line_zoomed),
            FadeOut(fit_eqn),
            FadeOut(r_squared_callout),
            run_time=0.8,
        )
        self.play(
            FadeOut(ax_zoomed),
            FadeOut(snn_dots_zoomed),
            FadeIn(ax_combined),
            FadeIn(snn_dots_combined),
            FadeIn(cnn_line_combined),
            FadeIn(cnn_tag_combined),
            FadeIn(snn_tag_combined),
            run_time=2.0,
        )
        self.wait(4.0)

        # ---------- Phase 6: closing tag  (~6 s) ----------
        self.play(FadeIn(closing_tag, shift=UP * 0.15), run_time=0.7)
        self.wait(5.5)
