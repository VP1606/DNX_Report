"""
Quantization Diagram — Sub-beat 3B
DetectorNX Screencast — Beat 3 (SNN Introduction, "the catch")

Visualises the lossy 1-bit quantisation that the spiking paradigm
imposes on every activation. The animation pairs with the Sub-beat 3B
voiceover and hands off into Beat 4 (Aims) with the closing question.

Visual flow:
  1. Title fades in
  2. Top plot appears: a smooth blue continuous activation curve with
     a dashed yellow threshold line — labelled "32-bit continuous"
  3. Bottom baseline appears — labelled "1-bit spike"
  4. Subtle dashed grey vertical lines drop from each sample point on
     the curve down to the baseline
  5. At each sample time where the curve sat above threshold, a yellow
     tick appears on the baseline — at the no-spike samples nothing
     appears (deliberately — that absence IS the 1-bit signal)
  6. Caption fades in below: "32-bit continuous   →   1-bit spike"
  7. Plots fade out and the closing question takes the screen:
     "How much does this cost?" — handing off to Beat 4 (Aims)

Total length ~14 sec, paired with the Sub-beat 3B voiceover (~14 sec):

  "But there's a catch. A spike is binary — it either fires or it
   doesn't — so every signal gets quantised to one bit. The question
   is, how much does that actually cost?"

Render commands:
  Preview (fast):
      manim -pql quantization_diagram.py QuantizationDiagram
  Final 1080p:
      manim -pqh quantization_diagram.py QuantizationDiagram

Output goes to:
  media/videos/quantization_diagram/{quality}/QuantizationDiagram.mp4
"""

from manim import *
import numpy as np


class QuantizationDiagram(Scene):
    def construct(self):
        # Pure black background — matches the rest of the screencast set
        self.camera.background_color = "#000000"

        # =====================================================
        # PARAMETERS / SAMPLE GENERATION
        # =====================================================
        threshold = 0.5

        def f(t):
            """Smooth continuous activation curve — multi-frequency so
            the binarised pattern below is visibly non-trivial."""
            return (
                0.50
                + 0.32 * np.sin(1.20 * t)
                + 0.16 * np.sin(2.70 * t + 0.7)
            )

        n_samples = 12
        sample_times = np.linspace(0.5, 9.5, n_samples)
        spike_pattern = [f(t) > threshold for t in sample_times]

        # =====================================================
        # TITLE
        # =====================================================
        title = Text(
            "Quantisation: continuous → 1-bit spike",
            font_size=30,
            color=WHITE,
        ).to_edge(UP, buff=0.35)

        # =====================================================
        # TOP PLOT: continuous activation curve
        # =====================================================
        top_axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.0, 0.5],
            x_length=10.0,
            y_length=2.0,
            axis_config={
                "color": GREY_B,
                "include_tip": False,
                "stroke_width": 2,
            },
            x_axis_config={"include_numbers": False},
            y_axis_config={"include_numbers": False},
        ).move_to([0.5, 1.4, 0])

        continuous_curve = top_axes.plot(
            f, x_range=[0, 10, 0.04],
            color=BLUE,
            stroke_width=4,
        )

        # Threshold dashed line stops short of the right edge so the
        # "threshold" label sits inside the plot frame (same fix as
        # the LIF animation).
        threshold_line = DashedLine(
            top_axes.coords_to_point(0, threshold),
            top_axes.coords_to_point(8.6, threshold),
            color=YELLOW,
            stroke_width=2,
            dash_length=0.12,
        )
        threshold_label = Text(
            "threshold",
            font_size=18,
            color=YELLOW,
        ).next_to(threshold_line.get_end(), RIGHT, buff=0.12)

        top_label = Text(
            "32-bit continuous activation",
            font_size=22,
            color=BLUE,
        ).next_to(top_axes, UP, buff=0.18).align_to(top_axes, LEFT)

        # =====================================================
        # BOTTOM BASELINE + LABEL
        # =====================================================
        baseline_y = -1.4
        x_left_screen = top_axes.coords_to_point(0, 0)
        x_right_screen = top_axes.coords_to_point(10, 0)
        baseline_left = np.array([x_left_screen[0], baseline_y, 0])
        baseline_right = np.array([x_right_screen[0], baseline_y, 0])
        bottom_baseline = Line(
            baseline_left, baseline_right,
            color=GREY_B,
            stroke_width=2,
        )
        bottom_label = (
            Text("1-bit spike", font_size=22, color=YELLOW)
            .next_to(bottom_baseline, LEFT, buff=0.25)
        )

        # =====================================================
        # SAMPLE DASHED LINES (subtle, link curve → baseline)
        # =====================================================
        sample_lines = []
        for t_value in sample_times:
            top_pt = top_axes.coords_to_point(t_value, f(t_value))
            bot_pt = np.array(
                [top_axes.coords_to_point(t_value, 0)[0], baseline_y, 0]
            )
            sample_lines.append(
                DashedLine(
                    top_pt, bot_pt,
                    color=GREY_D,
                    stroke_width=1.2,
                    dash_length=0.08,
                )
            )

        # =====================================================
        # SPIKE TICKS — only at sample times where f(t) > threshold
        # =====================================================
        spike_ticks = []
        sample_dots_on_curve = []
        for t_value, has_spike in zip(sample_times, spike_pattern):
            x_screen = top_axes.coords_to_point(t_value, 0)[0]
            # Small dot on the curve at the sample time, indicating
            # "this is where we sampled" — yellow if it spiked, grey otherwise.
            curve_pt = top_axes.coords_to_point(t_value, f(t_value))
            sample_dots_on_curve.append(
                Dot(
                    point=curve_pt,
                    radius=0.06,
                    color=YELLOW if has_spike else GREY_C,
                )
            )
            if has_spike:
                spike_ticks.append(
                    Line(
                        np.array([x_screen, baseline_y, 0]),
                        np.array([x_screen, baseline_y + 0.55, 0]),
                        color=YELLOW,
                        stroke_width=5,
                    )
                )
            else:
                # Placeholder so the index alignment is preserved;
                # not added to the scene.
                spike_ticks.append(None)

        spike_ticks_present = [t for t in spike_ticks if t is not None]

        # =====================================================
        # TRANSITION CAPTION
        # =====================================================
        caption = Text(
            "32-bit continuous   →   1-bit spike",
            font_size=26,
            color=GREY_B,
        ).move_to([0.5, -2.5, 0])

        # =====================================================
        # CLOSING QUESTION (replaces the plots)
        # =====================================================
        question = Text(
            "How much does this cost?",
            font_size=46,
            color=WHITE,
            weight=BOLD,
        ).move_to(ORIGIN)

        # =====================================================
        # ANIMATION SEQUENCE  (~14 sec total)
        # =====================================================

        # Step 1: Title  (0.5 s)
        self.play(Write(title), run_time=0.5)

        # Step 2: Top axes + threshold + top label  (1.1 s)
        self.play(
            Create(top_axes),
            Write(top_label),
            run_time=0.7,
        )
        self.play(
            Create(threshold_line),
            Write(threshold_label),
            run_time=0.4,
        )

        # Step 3: Continuous curve grows  (2.4 s)
        self.play(
            Create(continuous_curve),
            run_time=2.4,
            rate_func=linear,
        )

        # Step 4: Bottom baseline + label  (0.5 s)
        self.play(
            Create(bottom_baseline),
            Write(bottom_label),
            run_time=0.5,
        )

        # Step 5: Sample dashed lines + sample dots on the curve
        # appear together as a left-to-right sweep  (1.6 s)
        self.play(
            LaggedStart(
                *[
                    AnimationGroup(Create(sl), FadeIn(d, scale=0.7))
                    for sl, d in zip(sample_lines, sample_dots_on_curve)
                ],
                lag_ratio=0.18,
            ),
            run_time=1.6,
        )

        # Step 6: Spike ticks land on the baseline (sequentially)  (1.4 s)
        self.play(
            LaggedStart(
                *[Create(t) for t in spike_ticks_present],
                lag_ratio=0.20,
            ),
            run_time=1.4,
        )

        # Step 7: Caption "32-bit → 1-bit"  (0.7 s)
        self.play(FadeIn(caption, shift=UP * 0.2), run_time=0.7)

        # Step 8: Hold the full visual  (1.0 s)
        self.wait(1.0)

        # Step 9: Fade everything except the title-region  (0.7 s)
        self.play(
            FadeOut(top_axes),
            FadeOut(continuous_curve),
            FadeOut(threshold_line),
            FadeOut(threshold_label),
            FadeOut(top_label),
            FadeOut(bottom_baseline),
            FadeOut(bottom_label),
            *[FadeOut(sl) for sl in sample_lines],
            *[FadeOut(d) for d in sample_dots_on_curve],
            *[FadeOut(t) for t in spike_ticks_present],
            FadeOut(caption),
            FadeOut(title),
            run_time=0.7,
        )

        # Step 10: Closing question + hold  (~4.2 s)
        # Extra hold so the voiceover line "The question is, how much
        # does that actually cost?" lands fully before Beat 4 starts.
        self.play(FadeIn(question, shift=UP * 0.3), run_time=0.7)
        self.wait(3.5)
