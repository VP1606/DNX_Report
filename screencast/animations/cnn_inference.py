"""
CNN Inference Graphic — Sub-beat 2C
DetectorNX Screencast — Beat 2 (Motivation + ADAS Demo)

Animates the "modern ADAS perception runs on dense convolutional
networks" graphic that opens Sub-beat 2C. Total length ~8.5 sec,
matching the voiceover slot before the trajectory graph.

Visual flow:
  1. Event-camera frame appears on the left
  2. Five conv blocks fade in across the middle
  3. Activation pulse cascades left → right (each block lights up)
  4. Output frame on the right gets bounding boxes
  5. FLOP counter at the bottom ticks up to 9.22 G-FLOPs / frame

Render commands:
  Preview (fast):
      manim -pql cnn_inference.py CNNInference

  Final 1080p:
      manim -pqh cnn_inference.py CNNInference

Output goes to:
  media/videos/cnn_inference/{quality}/CNNInference.mp4
"""

from manim import *
import numpy as np


class CNNInference(Scene):
    def construct(self):
        # Pure black background — matches trajectory_graph.py
        self.camera.background_color = "#000000"

        # =====================================================
        # TITLE
        # =====================================================

        title = Text(
            "Convolutional inference per frame",
            font_size=30,
            color=WHITE,
        ).to_edge(UP, buff=0.4)

        # =====================================================
        # INPUT FRAME (left) — stylised event-camera scene
        # =====================================================

        input_box = Rectangle(
            width=2.0,
            height=1.4,
            color=GREY_B,
            stroke_width=2,
            fill_color="#0a0a1a",
            fill_opacity=0.6,
        ).move_to([-5.5, 0, 0])

        # Event-style dots — suggests sparse asynchronous events
        np.random.seed(7)
        event_dots = VGroup()
        for _ in range(45):
            x = np.random.uniform(-0.85, 0.85)
            y = np.random.uniform(-0.55, 0.55)
            color = WHITE if np.random.random() > 0.5 else GREY_C
            dot = Dot(
                point=input_box.get_center() + np.array([x, y, 0]),
                radius=0.025,
                color=color,
            )
            event_dots.add(dot)

        # Hint of a vehicle shape inside the frame
        car_hint = Rectangle(
            width=0.7,
            height=0.3,
            color=WHITE,
            stroke_width=1.5,
        ).move_to(input_box.get_center())

        input_label = Text(
            "Frame in",
            font_size=18,
            color=GREY_B,
        ).next_to(input_box, DOWN, buff=0.18)

        # =====================================================
        # CONV BLOCKS — five blocks across the middle
        # =====================================================
        # Spatial dim shrinks (height decreases), channel count
        # grows (label below shows channels). Each block is a
        # mini stack of 3 rectangles to suggest 3D depth.

        conv_x_positions = [-3.0, -1.5, 0.0, 1.5, 3.0]
        conv_heights = [1.6, 1.3, 1.0, 0.75, 0.55]
        conv_channels = ["64", "128", "256", "512", "1024"]

        def make_conv_block(position, height, width=0.45):
            """Three offset rectangles → 3D feature-map look."""
            back = Rectangle(
                width=width,
                height=height,
                color=GREY_D,
                stroke_width=1.2,
                fill_color="#0f0f1f",
                fill_opacity=0.4,
            )
            mid = Rectangle(
                width=width,
                height=height,
                color=GREY_C,
                stroke_width=1.5,
                fill_color="#0f0f1f",
                fill_opacity=0.5,
            )
            front = Rectangle(
                width=width,
                height=height,
                color=GREY_B,
                stroke_width=2,
                fill_color="#0f0f1f",
                fill_opacity=0.6,
            )
            base = np.array(position)
            back.move_to(base + np.array([0.12, -0.07, 0]))
            mid.move_to(base + np.array([0.06, -0.035, 0]))
            front.move_to(base)
            return VGroup(back, mid, front)

        conv_blocks = []
        block_labels = []
        for i in range(5):
            blk = make_conv_block(
                position=[conv_x_positions[i], 0, 0],
                height=conv_heights[i],
            )
            conv_blocks.append(blk)
            lbl = Text(conv_channels[i], font_size=14, color=GREY_C)
            lbl.next_to(blk, DOWN, buff=0.22)
            block_labels.append(lbl)

        # Connecting arrows between conv blocks
        block_arrows = []
        for i in range(4):
            front_a = conv_blocks[i][-1]    # front rect of left block
            front_b = conv_blocks[i + 1][-1]  # front rect of right block
            arrow = Arrow(
                start=front_a.get_right(),
                end=front_b.get_left(),
                color=GREY_C,
                stroke_width=1.5,
                buff=0.05,
                max_tip_length_to_length_ratio=0.25,
            )
            block_arrows.append(arrow)

        # Input → first conv block
        input_arrow = Arrow(
            start=input_box.get_right(),
            end=conv_blocks[0][-1].get_left(),
            color=GREY_C,
            stroke_width=1.5,
            buff=0.1,
            max_tip_length_to_length_ratio=0.18,
        )

        # =====================================================
        # OUTPUT FRAME (right) — bounding boxes appear
        # =====================================================

        output_box = Rectangle(
            width=2.0,
            height=1.4,
            color=GREY_B,
            stroke_width=2,
            fill_color="#0a0a1a",
            fill_opacity=0.6,
        ).move_to([5.5, 0, 0])

        bbox_car = Rectangle(
            width=0.7,
            height=0.3,
            color=GREEN,
            stroke_width=2.5,
        ).move_to(output_box.get_center())
        bbox_car_label = (
            Text("car 0.94", font_size=12, color=GREEN)
            .next_to(bbox_car, UP, buff=0.03)
            .align_to(bbox_car, LEFT)
        )

        bbox_ped = Rectangle(
            width=0.25,
            height=0.45,
            color=YELLOW,
            stroke_width=2,
        ).move_to(output_box.get_center() + np.array([-0.6, 0.1, 0]))
        bbox_ped_label = (
            Text("ped 0.81", font_size=12, color=YELLOW)
            .next_to(bbox_ped, UP, buff=0.03)
            .align_to(bbox_ped, LEFT)
        )

        output_arrow = Arrow(
            start=conv_blocks[-1][-1].get_right(),
            end=output_box.get_left(),
            color=GREY_C,
            stroke_width=1.5,
            buff=0.1,
            max_tip_length_to_length_ratio=0.18,
        )

        output_label = Text(
            "Detections",
            font_size=18,
            color=GREY_B,
        ).next_to(output_box, DOWN, buff=0.18)

        # =====================================================
        # FLOP COUNTER (bottom)
        # =====================================================

        flop_counter = DecimalNumber(
            0.0,
            num_decimal_places=2,
            color=RED,
            font_size=42,
        )
        flop_unit = Text(
            "  G-FLOPs · per frame",
            font_size=24,
            color=GREY_B,
        )
        flop_group = (
            VGroup(flop_counter, flop_unit)
            .arrange(RIGHT, buff=0.15)
            .to_edge(DOWN, buff=0.6)
        )

        # =====================================================
        # ANIMATION SEQUENCE  (~8.5 sec)
        # =====================================================

        # Step 1: Title  (0.5s)
        self.play(Write(title), run_time=0.5)

        # Step 2: Input frame appears  (1.2s)
        self.play(
            Create(input_box),
            Write(input_label),
            run_time=0.4,
        )
        self.play(
            LaggedStart(
                *[FadeIn(d, scale=0.5) for d in event_dots],
                lag_ratio=0.02,
            ),
            Create(car_hint),
            run_time=0.8,
        )

        # Step 3: Conv block skeleton fades in  (0.8s)
        skeleton = VGroup(
            *conv_blocks,
            *block_labels,
            *block_arrows,
            input_arrow,
        )
        self.play(FadeIn(skeleton, shift=DOWN * 0.15), run_time=0.8)

        # Step 4: Activation pulse cascades through blocks  (~1.9s)
        # Each block's front rect lights up briefly as the
        # "activation wave" passes through. This is the visual
        # parallel to billions of MAC operations firing.
        for block in conv_blocks:
            front = block[-1]
            self.play(
                front.animate.set_fill(BLUE, opacity=0.85)
                .set_stroke(BLUE, width=3),
                run_time=0.20,
            )
            self.play(
                front.animate.set_fill("#0f0f1f", opacity=0.6)
                .set_stroke(GREY_B, width=2),
                run_time=0.15,
            )

        # Step 5: Output frame appears + arrow  (0.6s)
        self.play(
            Create(output_arrow),
            Create(output_box),
            Write(output_label),
            run_time=0.6,
        )

        # Step 6: Bounding boxes draw  (1.0s)
        self.play(
            Create(bbox_car),
            Write(bbox_car_label),
            run_time=0.5,
        )
        self.play(
            Create(bbox_ped),
            Write(bbox_ped_label),
            run_time=0.5,
        )

        # Step 7: FLOP counter ticks up to 9.22  (1.8s)
        self.play(FadeIn(flop_group), run_time=0.3)
        self.play(
            ChangeDecimalToValue(flop_counter, 9.22),
            run_time=1.5,
            rate_func=rate_functions.ease_out_cubic,
        )

        # Step 8: Hold — lets the number land  (0.8s)
        self.wait(0.8)
