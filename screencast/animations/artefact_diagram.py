"""
DetectorNX Artefact Diagram — Sub-beat 5B
DetectorNX Screencast — Beat 5 (Approach)

Visualises the full DetectorNX pipeline end-to-end: raw ETraM event
data flows through the BOLT preprocessing pipeline, splits into both
spiking (SNN-G3) and continuous (CNN-G3) backbones in parallel, then
converges through the shared multi-box regression head into bounding-
box predictions. A small inset on the right shows what raw event-
camera data looks like — scattered polarised events with a hint of
vehicle motion, in the same visual language as `cnn_inference.py`.

The evaluation-suite section of the original report figure is
deliberately excluded — those metrics get their reveal moments in
Beats 6 (Results) and 7 (Calibration), so showing them now would
preview content that hasn't been earned yet.

Visual flow:
  1. Title + Raw ETraM box + event-data inset appear
  2. Preprocessing Pipeline (BOLT) container fades in with 3 sub-steps
     cascading
  3. Two backbones land side-by-side (SNN green + CNN purple), arrows
     branch from preprocessing into both
  4. Regression head + bounding-box predictions appear, arrows from
     both backbones converge into the head, head outputs predictions
  5. Light pulse traces the full data flow top-to-bottom
  6. Novelty hedge fades in: "First directly-trained spiking detector
     evaluated on ETraM"

Total length ~22 sec.

Render commands:
  Preview (fast):
      manim -pql artefact_diagram.py ArtefactDiagram
  Final 1080p:
      manim -pqh artefact_diagram.py ArtefactDiagram

Output goes to:
  media/videos/artefact_diagram/{quality}/ArtefactDiagram.mp4
"""

from manim import *
import numpy as np


class ArtefactDiagram(Scene):
    def construct(self):
        self.camera.background_color = "#000000"
        np.random.seed(42)

        # =====================================================
        # COLOUR PALETTE  (matches the report's high-level
        # architecture diagram, adapted for dark background)
        # =====================================================
        TAN_FILL = "#3D3225"
        TAN_STROKE = "#C5A87A"

        PREP_STROKE = "#7A6FAF"      # lavender outline for BOLT container
        STEP_FILL = "#332B5C"
        STEP_STROKE = "#9888D4"

        SNN_FILL = "#1F3D2C"
        SNN_STROKE = "#73C49B"
        CNN_FILL = "#2D2658"
        CNN_STROKE = "#9888D4"

        HEAD_FILL = "#3A2810"
        HEAD_STROKE = "#D4843E"

        # =====================================================
        # TITLE
        # =====================================================
        title = Text(
            "DetectorNX",
            font_size=36,
            color=WHITE,
            weight=BOLD,
        ).to_edge(UP, buff=0.30)

        # =====================================================
        # ETraM EVENT-DATA INSET (right side)
        # =====================================================
        inset_centre = np.array([5.0, 2.55, 0])
        inset_box = Rectangle(
            width=1.8, height=1.35,
            stroke_color=TAN_STROKE,
            stroke_width=1.4,
            fill_color=TAN_FILL,
            fill_opacity=0.40,
        ).move_to(inset_centre)

        # Scattered polarised events
        event_dots = VGroup()
        for _ in range(40):
            x = np.random.uniform(-0.78, 0.78)
            y = np.random.uniform(-0.55, 0.55)
            color = WHITE if np.random.random() > 0.5 else BLUE
            event_dots.add(
                Dot(
                    point=inset_centre + np.array([x, y, 0]),
                    radius=0.022,
                    color=color,
                )
            )

        # Vehicle hint inside the inset
        vehicle_hint = Rectangle(
            width=0.55, height=0.20,
            stroke_color=GREY_B,
            stroke_width=1.2,
        ).move_to(inset_centre + np.array([-0.05, -0.10, 0]))

        inset_caption = Text(
            "Raw event stream",
            font_size=12,
            color=GREY_C,
            slant=ITALIC,
        ).next_to(inset_box, UP, buff=0.08)

        # =====================================================
        # CENTRAL PIPELINE (top to bottom)
        # =====================================================
        PIPE_X = -1.0
        BOX_W = 4.2

        # ----- Raw ETraM Data -----
        raw_box = Rectangle(
            width=BOX_W, height=0.55,
            stroke_color=TAN_STROKE, stroke_width=1.5,
            fill_color=TAN_FILL, fill_opacity=0.6,
        ).move_to([PIPE_X, 2.7, 0])
        raw_label = Text(
            "Raw ETraM Data",
            font_size=18, color=WHITE,
        ).move_to(raw_box.get_center())

        # ----- Preprocessing Pipeline (BOLT) container + 3 steps -----
        prep_top = 1.75
        prep_bot = 0.05
        prep_centre_y = (prep_top + prep_bot) / 2
        prep_h = (prep_top - prep_bot) + 0.15
        prep_container = DashedVMobject(
            Rectangle(
                width=BOX_W + 0.20, height=prep_h,
                stroke_color=PREP_STROKE, stroke_width=1.5,
            ).move_to([PIPE_X, prep_centre_y, 0]),
            num_dashes=80,
        )
        # Rotated side-label, like the report figure
        prep_title = (
            Text(
                "PRE-PROCESSING PIPELINE (BOLT)",
                font_size=11, color=PREP_STROKE, weight=BOLD,
            )
            .rotate(PI / 2)
            .next_to(prep_container, LEFT, buff=0.15)
        )

        step_w = BOX_W - 0.40
        step_h = 0.40
        step_y_centres = [
            prep_top - 0.30,
            prep_centre_y,
            prep_bot + 0.30,
        ]
        step_descriptions = [
            "Spatiotemporal Noise Filtering",
            "Voxel Grid Representation",
            "Spatial Downsampling",
        ]
        step_boxes = []
        step_texts = []
        for desc, sy in zip(step_descriptions, step_y_centres):
            sb = Rectangle(
                width=step_w, height=step_h,
                stroke_color=STEP_STROKE, stroke_width=1.2,
                fill_color=STEP_FILL, fill_opacity=0.7,
            ).move_to([PIPE_X, sy, 0])
            step_boxes.append(sb)
            step_texts.append(
                Text(desc, font_size=14, color=WHITE).move_to(sb.get_center())
            )

        # ----- Backbones (side-by-side) -----
        bb_y = -1.05
        bb_w = 1.95
        bb_h = 0.65

        snn_box = Rectangle(
            width=bb_w, height=bb_h,
            stroke_color=SNN_STROKE, stroke_width=1.6,
            fill_color=SNN_FILL, fill_opacity=0.85,
        ).move_to([PIPE_X - 1.10, bb_y, 0])
        snn_label = Text(
            "DetectorNX-G3-SNN",
            font_size=14, color=SNN_STROKE, weight=BOLD,
        ).move_to(snn_box.get_center() + UP * 0.13)
        snn_subtitle = Text(
            "Spiking · 4 × SEWResBlocks",
            font_size=11, color=GREY_B,
        ).move_to(snn_box.get_center() + DOWN * 0.13)

        cnn_box = Rectangle(
            width=bb_w, height=bb_h,
            stroke_color=CNN_STROKE, stroke_width=1.6,
            fill_color=CNN_FILL, fill_opacity=0.85,
        ).move_to([PIPE_X + 1.10, bb_y, 0])
        cnn_label = Text(
            "DetectorNX-G3-CNN",
            font_size=14, color=CNN_STROKE, weight=BOLD,
        ).move_to(cnn_box.get_center() + UP * 0.13)
        cnn_subtitle = Text(
            "Continuous · 4 × ResBlocks",
            font_size=11, color=GREY_B,
        ).move_to(cnn_box.get_center() + DOWN * 0.13)

        # ----- Regression Head -----
        head_y = -2.10
        head_box = Rectangle(
            width=BOX_W * 0.72, height=0.50,
            stroke_color=HEAD_STROKE, stroke_width=1.5,
            fill_color=HEAD_FILL, fill_opacity=0.85,
        ).move_to([PIPE_X, head_y, 0])
        head_label = Text(
            "Multi-Box Regression Head",
            font_size=15, color=HEAD_STROKE, weight=BOLD,
        ).move_to(head_box.get_center())

        # ----- Bounding-Box Predictions -----
        pred_y = -2.95
        pred_box = Rectangle(
            width=BOX_W * 0.55, height=0.40,
            stroke_color=TAN_STROKE, stroke_width=1.4,
            fill_color=TAN_FILL, fill_opacity=0.6,
        ).move_to([PIPE_X, pred_y, 0])
        pred_label = Text(
            "Bounding-Box Predictions",
            font_size=14, color=WHITE,
        ).move_to(pred_box.get_center())

        # =====================================================
        # ARROWS  (data flow connectors)
        # =====================================================
        def make_arrow(start_pt, end_pt):
            return Arrow(
                start=start_pt, end=end_pt,
                color=GREY_C, stroke_width=1.6,
                buff=0.05,
                max_tip_length_to_length_ratio=0.25,
            )

        a_raw_prep = make_arrow(
            raw_box.get_bottom(),
            prep_container.get_top(),
        )
        prep_bottom_pt = np.array([PIPE_X, prep_bot - 0.08, 0])
        a_prep_snn = make_arrow(
            prep_bottom_pt,
            snn_box.get_top() + np.array([0, 0.02, 0]),
        )
        a_prep_cnn = make_arrow(
            prep_bottom_pt,
            cnn_box.get_top() + np.array([0, 0.02, 0]),
        )
        a_snn_head = make_arrow(
            snn_box.get_bottom(),
            head_box.get_top() + np.array([-0.30, 0.02, 0]),
        )
        a_cnn_head = make_arrow(
            cnn_box.get_bottom(),
            head_box.get_top() + np.array([0.30, 0.02, 0]),
        )
        a_head_pred = make_arrow(
            head_box.get_bottom(),
            pred_box.get_top(),
        )

        # =====================================================
        # NOVELTY HEDGE  (bottom)
        # =====================================================
        hedge = Text(
            "First directly-trained spiking detector evaluated on ETraM",
            font_size=18, color=GREY_B, slant=ITALIC,
        ).to_edge(DOWN, buff=0.30)

        # =====================================================
        # ANIMATION SEQUENCE  (~22 s)
        # =====================================================

        # ----- Phase 1: Title + Raw ETraM + ETraM inset  (~3.0 s) -----
        self.play(Write(title), run_time=0.7)
        self.play(
            FadeIn(raw_box),
            Write(raw_label),
            FadeIn(inset_box),
            Write(inset_caption),
            run_time=0.7,
        )
        self.play(
            LaggedStart(
                *[FadeIn(d, scale=0.5) for d in event_dots],
                lag_ratio=0.025,
            ),
            Create(vehicle_hint),
            run_time=1.6,
        )

        # ----- Phase 2: Preprocessing Pipeline  (~4.5 s) -----
        self.play(GrowArrow(a_raw_prep), run_time=0.5)
        self.play(
            Create(prep_container),
            Write(prep_title),
            run_time=1.1,
        )
        for sb, txt in zip(step_boxes, step_texts):
            self.play(
                FadeIn(sb, shift=DOWN * 0.10),
                Write(txt),
                run_time=0.75,
            )
        self.wait(0.3)

        # ----- Phase 3: Two backbones  (~3.5 s) -----
        self.play(
            GrowArrow(a_prep_snn),
            GrowArrow(a_prep_cnn),
            run_time=0.7,
        )
        self.play(
            FadeIn(snn_box, scale=0.95),
            Write(snn_label),
            Write(snn_subtitle),
            FadeIn(cnn_box, scale=0.95),
            Write(cnn_label),
            Write(cnn_subtitle),
            run_time=1.5,
        )
        self.wait(0.4)

        # ----- Phase 4: Regression Head + Predictions  (~3.0 s) -----
        self.play(
            GrowArrow(a_snn_head),
            GrowArrow(a_cnn_head),
            run_time=0.6,
        )
        self.play(
            FadeIn(head_box, shift=DOWN * 0.10),
            Write(head_label),
            run_time=0.8,
        )
        self.play(
            GrowArrow(a_head_pred),
            run_time=0.4,
        )
        self.play(
            FadeIn(pred_box, shift=DOWN * 0.10),
            Write(pred_label),
            run_time=0.7,
        )
        self.wait(0.4)

        # ----- Phase 5: Light pulse traces data flow  (~2.6 s) -----
        def flash_along(arrow_obj):
            return ShowPassingFlash(
                arrow_obj.copy().set_color(WHITE).set_stroke(width=3.5),
                time_width=0.5,
            )

        self.play(flash_along(a_raw_prep), run_time=0.5)
        self.play(
            flash_along(a_prep_snn),
            flash_along(a_prep_cnn),
            run_time=0.6,
        )
        self.play(
            flash_along(a_snn_head),
            flash_along(a_cnn_head),
            run_time=0.6,
        )
        self.play(flash_along(a_head_pred), run_time=0.5)
        self.wait(0.4)

        # ----- Phase 6: Novelty hedge  (~1.0 s) -----
        self.play(FadeIn(hedge, shift=UP * 0.20), run_time=0.8)

        # ----- Phase 7: Hold  (~3.5 s) -----
        self.wait(3.0)
