"""
LIF Neuron — Sub-beat 3A
DetectorNX Screencast — Beat 3 (SNN Introduction)

Animates the leaky integrate-and-fire spiking-neuron mechanic that
opens Sub-beat 3A. Total length ~19.8 sec, paired with the LIF slot
of the Sub-beat 3A voiceover (1:35 - 1:55).

Visual flow:
  1. Title fades in
  2. Soma + four input synapse arrows appear on the left
  3. Membrane-potential plot fades in on the right with a dashed
     horizontal threshold line
  4. Output spike-train baseline appears below the plot
  5. Two integrate-fire-reset cycles play out:
       - inputs arrive on synapses (white pulse on the arrow)
       - membrane potential jumps up at each input, leaks toward
         zero between inputs
       - on the input that pushes V above threshold the soma flashes
         yellow, an output tick appears, and the trace resets
  6. Closing caption: "spike  ->  reset  ->  repeat"

Render commands:
  Preview (fast):
      manim -pql lif_neuron.py LIFNeuron

  Final 1080p:
      manim -pqh lif_neuron.py LIFNeuron

  Final 4K:
      manim -pqk lif_neuron.py LIFNeuron

Output goes to:
  media/videos/lif_neuron/{quality}/LIFNeuron.mp4
"""

from manim import *
import numpy as np


class LIFNeuron(Scene):
    def construct(self):
        # Pure black background — matches cnn_inference.py / trajectory_graph.py
        self.camera.background_color = "#000000"

        # =====================================================
        # PARAMETERS
        # =====================================================
        # Leak time constant. Larger → slower decay between inputs.
        tau = 6.0
        # Potential jump per input arrival.
        delta_V = 0.4
        # Spike threshold (V/V_threshold ratio normalised to 1.0).
        threshold = 1.0
        # Input-arrival schedule.
        # 'input_spike' = an input that pushes V above threshold and
        # therefore triggers a fire+reset on this same time-step.
        events = [
            (0.5, "input",       0),
            (2.0, "input",       1),
            (3.5, "input",       2),
            (5.0, "input_spike", 3),
            (6.5, "input",       0),
            (7.5, "input",       1),
            (8.5, "input_spike", 2),
            (9.5, "input",       3),
        ]
        # Each unit of data-time → animation_time_scale seconds of
        # animation. Set so total runtime lands ~19.8 s.
        animation_time_scale = 1.2

        # =====================================================
        # TITLE
        # =====================================================

        title = Text(
            "Leaky integrate-and-fire spiking neuron",
            font_size=30,
            color=WHITE,
        ).to_edge(UP, buff=0.35)

        # =====================================================
        # NEURON (LEFT) — soma + four input synapse arrows
        # =====================================================

        soma_centre = np.array([-5.1, 0.5, 0])
        soma = Circle(
            radius=0.55,
            color=BLUE,
            stroke_width=3,
            fill_color="#0a0a1a",
            fill_opacity=0.7,
        ).move_to(soma_centre)
        soma_label = Text(
            "Neuron", font_size=18, color=GREY_B,
        ).next_to(soma, DOWN, buff=0.20)

        # Four incoming synapse arrows fanning in from the upper-
        # left and lower-left of the soma.
        synapse_anchor_offsets = [
            np.array([-1.5,  0.85, 0]),
            np.array([-1.7,  0.30, 0]),
            np.array([-1.7, -0.30, 0]),
            np.array([-1.5, -0.85, 0]),
        ]
        synapse_arrows = []
        for off in synapse_anchor_offsets:
            start = soma_centre + off
            direction = soma_centre - start
            unit = direction / np.linalg.norm(direction)
            end = soma_centre - unit * (soma.radius + 0.02)
            arr = Arrow(
                start=start,
                end=end,
                color=GREY_B,
                stroke_width=2,
                buff=0.0,
                max_tip_length_to_length_ratio=0.18,
            )
            synapse_arrows.append(arr)

        # =====================================================
        # MEMBRANE POTENTIAL PLOT (RIGHT)
        # =====================================================

        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 1.4, 0.5],
            x_length=8.0,
            y_length=2.0,
            axis_config={
                "color": GREY_B,
                "include_tip": False,
                "stroke_width": 2,
            },
            x_axis_config={"include_numbers": False},
            y_axis_config={"include_numbers": False},
        ).move_to([2.2, 1.5, 0])

        v_title = (
            Text("Membrane potential  V(t)", font_size=24, color=GREY_B)
            .next_to(axes, UP, buff=0.18)
            .align_to(axes, LEFT)
        )
        time_axis_label = Text(
            "time", font_size=20, color=GREY_B,
        ).next_to(axes.x_axis.get_right(), DOWN, buff=0.18)

        # Threshold dashed line at V = threshold.
        # Stop short of x=10 so the "threshold" label can sit inside
        # the plot frame rather than colliding with the right edge.
        threshold_line = DashedLine(
            start=axes.coords_to_point(0, threshold),
            end=axes.coords_to_point(8.6, threshold),
            color=YELLOW,
            stroke_width=2,
            dash_length=0.12,
        )
        threshold_label = Text(
            "threshold", font_size=18, color=YELLOW,
        ).next_to(threshold_line.get_end(), RIGHT, buff=0.12)

        # =====================================================
        # OUTPUT SPIKE TRAIN (BELOW V(t) PLOT)
        # =====================================================

        x_left_screen = axes.coords_to_point(0, 0)
        x_right_screen = axes.coords_to_point(10, 0)
        train_y = x_left_screen[1] - 1.7
        train_left = np.array([x_left_screen[0], train_y, 0])
        train_right = np.array([x_right_screen[0], train_y, 0])
        train_axis = Line(
            train_left, train_right,
            color=GREY_B,
            stroke_width=2,
        )
        train_label = (
            Text("Output spike train", font_size=20, color=GREY_B)
            .next_to(train_axis, LEFT, buff=0.25)
        )

        def output_tick(t_value):
            """Vertical YELLOW tick mark at output-spike time."""
            base_x = axes.coords_to_point(t_value, 0)[0]
            return Line(
                np.array([base_x, train_y, 0]),
                np.array([base_x, train_y + 0.55, 0]),
                color=YELLOW,
                stroke_width=5,
            )

        # =====================================================
        # TRACE BUILDERS
        # =====================================================

        def leak_curve(t_a, V_a, t_b):
            """Smooth exponential leak from (t_a, V_a) toward zero
            sampled out to t_b."""
            if abs(t_b - t_a) < 1e-6:
                return None
            return axes.plot(
                lambda t: V_a * np.exp(-(t - t_a) / tau),
                x_range=[t_a, t_b, 0.05],
                color=BLUE,
                stroke_width=4,
            )

        def jump_line(t_value, V_from, V_to, color=BLUE):
            """Vertical line representing an instantaneous jump at t."""
            return Line(
                axes.coords_to_point(t_value, V_from),
                axes.coords_to_point(t_value, V_to),
                color=color,
                stroke_width=4,
            )

        def synapse_pulse(synapse_idx):
            """Brief white flash on a synapse arrow."""
            arr = synapse_arrows[synapse_idx]
            return arr.animate(
                run_time=0.2, rate_func=there_and_back,
            ).set_color(WHITE)

        # =====================================================
        # ANIMATION SEQUENCE  (~19.8 sec total)
        # =====================================================

        # ----- SETUP  (~3.4 sec) -----

        # Step 1: Title  (0.6s)
        self.play(Write(title), run_time=0.6)

        # Step 2: Neuron + synapses  (1.0s)
        self.play(
            Create(soma),
            Write(soma_label),
            *[GrowArrow(a) for a in synapse_arrows],
            run_time=1.0,
        )

        # Step 3: Plot axes + V(t) label  (1.0s)
        self.play(
            Create(axes),
            Write(v_title),
            Write(time_axis_label),
            run_time=1.0,
        )

        # Step 4: Threshold line  (0.4s)
        self.play(
            Create(threshold_line),
            Write(threshold_label),
            run_time=0.4,
        )

        # Step 5: Output train baseline  (0.4s)
        self.play(
            Create(train_axis),
            Write(train_label),
            run_time=0.4,
        )

        # ----- MAIN DYNAMICS  (~13.7 sec) -----
        # Two integrate-fire-reset cycles plus a trailing input
        # that leaves the trace climbing again.

        prev_t = 0.0
        prev_V = 0.0
        for (t_value, etype, syn_idx) in events:

            # 1. Leak segment from (prev_t, prev_V) up to t_value
            seg = leak_curve(prev_t, prev_V, t_value)
            V_pre = prev_V * np.exp(-(t_value - prev_t) / tau)
            if seg is not None:
                seg_run = max(0.2, (t_value - prev_t) * animation_time_scale)
                self.play(Create(seg), run_time=seg_run, rate_func=linear)

            # 2. Synapse pulse + input jump from V_pre to V_post
            V_post = V_pre + delta_V
            jump_up = jump_line(t_value, V_pre, V_post, color=BLUE)
            self.play(
                synapse_pulse(syn_idx),
                Create(jump_up),
                run_time=0.2,
            )

            if etype == "input_spike":
                # Trace is now above threshold — fire and reset.
                tick = output_tick(t_value)
                jump_down = jump_line(t_value, V_post, 0, color=BLUE)
                self.play(
                    Indicate(soma, scale_factor=1.18, color=YELLOW),
                    Create(tick),
                    Create(jump_down),
                    run_time=0.5,
                )
                prev_V = 0.0
            else:
                prev_V = V_post

            prev_t = t_value

        # ----- CLOSING CAPTION  (~2.7 sec) -----

        caption = Text(
            "spike  →  reset  →  repeat",
            font_size=34,
            color=WHITE,
            weight=BOLD,
        ).to_edge(DOWN, buff=0.5)

        self.play(FadeIn(caption, shift=UP * 0.3), run_time=0.7)
        self.wait(1.7)
