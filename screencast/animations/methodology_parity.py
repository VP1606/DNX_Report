"""
Methodology Parity — Sub-beat 5A
DetectorNX Screencast — Beat 5 (Approach)

Visualises strict architectural parity between the SNN and CNN
variants of DetectorNX. Two side-by-side 9-stage columns, vertically
aligned so the audience sees they're mirror images. Only the
paradigm-specific stages (Stem activation + Residual blocks) carry
colour; everything else is shared structure in neutral steel-blue.
The SNN's extra Temporal Fusion stage occupies a row that is
deliberately left empty on the CNN side, making the one
spiking-paradigm-required addition visually salient.

Visual flow:
  1. Title + column headers fade in
  2. Both column skeletons appear in neutral grey via LaggedStart
  3. Paradigm-specific stages animate to colour:
       - CNN: Stem, Block 1, Block 2, High-Res → PURPLE
       - SNN: Stem, Block 1, Block 2, High-Res → GREEN
     Annotation: "Only the activation paradigm changes"
  4. Param parity tags fade in below: 11.73 M ≈ 11.72 M
  5. Parity ticks row: ✓ Same architecture · ✓ Same parameters ·
       ✓ Same hyperparameters · ✓ Same data
  6. Closing caption: "One variable. Variable-isolated comparison."

Total length ~22 sec, paired with the Sub-beat 5A voiceover (~25 sec).

Render commands:
  Preview (fast):
      manim -pql methodology_parity.py MethodologyParity
  Final 1080p:
      manim -pqh methodology_parity.py MethodologyParity

Output goes to:
  media/videos/methodology_parity/{quality}/MethodologyParity.mp4
"""

from manim import *
import numpy as np


class MethodologyParity(Scene):
    def construct(self):
        self.camera.background_color = "#000000"

        # =====================================================
        # GEOMETRY
        # =====================================================
        BOX_W = 2.5
        BOX_H = 0.40
        ROW_SPACING = 0.50          # centre-to-centre vertical spacing
        COL_X_CNN = -3.4
        COL_X_SNN = 3.4
        TOP_Y = 2.0                 # y-coord of the FIRST box centre

        # =====================================================
        # COLOUR PALETTE
        # =====================================================
        SHARED_FILL = "#243049"     # dark steel-blue for paradigm-agnostic stages
        SHARED_STROKE = "#7A8AAA"   # light blue-grey outline
        SHARED_OPACITY = 0.85

        SE_FILL = "#3A2810"         # warm dark for SE Bridge
        SE_STROKE = "#D4843E"       # orange — matches the existing report diagrams

        CNN_PARADIGM_FILL = "#3A2D5C"   # purple-tinted dark fill
        CNN_PARADIGM_STROKE = "#9888D4" # bright purple outline
        SNN_PARADIGM_FILL = "#1F3D2C"   # green-tinted dark fill
        SNN_PARADIGM_STROKE = "#73C49B" # bright green outline

        TF_FILL = "#1F3D2C"             # same green family as SNN
        TF_STROKE = "#73C49B"

        CNN_HEADER = "#9888D4"
        SNN_HEADER = "#73C49B"

        # =====================================================
        # STAGE DEFINITIONS
        # row_idx is the visual row both columns share. The Temporal
        # Fusion row exists only on the SNN side; the CNN column
        # leaves that row empty (a deliberate visual asymmetry).
        # =====================================================
        # (label,            row_idx, kind)
        # kind ∈ {"paradigm", "se", "shared", "tf_snn_only"}
        stages = [
            ("Stem",           0, "paradigm"),
            ("Block 1",        1, "paradigm"),
            ("Block 2",        2, "paradigm"),
            ("SE Bridge",      3, "se"),
            ("High-Res",       4, "paradigm"),
            ("Temporal Fusion",5, "tf_snn_only"),
            ("Channel Proj",   6, "shared"),
            ("Dual Pool",      7, "shared"),
            ("Regression",     8, "shared"),
        ]
        n_rows = len(stages)

        def row_y(row_idx):
            return TOP_Y - row_idx * ROW_SPACING

        # =====================================================
        # TITLE + COLUMN HEADERS
        # =====================================================
        title = Text(
            "Architectural parity",
            font_size=32,
            color=WHITE,
        ).to_edge(UP, buff=0.30)

        cnn_header = Text(
            "DetectorNX-G3-CNN",
            font_size=20,
            color=CNN_HEADER,
            weight=BOLD,
        ).move_to([COL_X_CNN, TOP_Y + 0.65, 0])

        snn_header = Text(
            "DetectorNX-G3-SNN",
            font_size=20,
            color=SNN_HEADER,
            weight=BOLD,
        ).move_to([COL_X_SNN, TOP_Y + 0.65, 0])

        # =====================================================
        # BOX BUILDER
        # =====================================================
        def make_box(x, y, fill, stroke, opacity=SHARED_OPACITY):
            return Rectangle(
                width=BOX_W,
                height=BOX_H,
                fill_color=fill,
                fill_opacity=opacity,
                stroke_color=stroke,
                stroke_width=1.6,
            ).move_to([x, y, 0])

        cnn_boxes = {}     # label -> Rectangle
        snn_boxes = {}
        cnn_labels = {}    # label -> Text
        snn_labels = {}

        for label, row_idx, kind in stages:
            y = row_y(row_idx)

            # ----- CNN side -----
            if kind == "tf_snn_only":
                pass  # row deliberately empty on CNN side
            elif kind == "se":
                box = make_box(COL_X_CNN, y, SE_FILL, SE_STROKE)
                cnn_boxes[label] = box
            elif kind == "paradigm":
                # Initial state: neutral shared colour. Will recolour later.
                box = make_box(COL_X_CNN, y, SHARED_FILL, SHARED_STROKE)
                cnn_boxes[label] = box
            else:  # shared
                box = make_box(COL_X_CNN, y, SHARED_FILL, SHARED_STROKE)
                cnn_boxes[label] = box

            if label in cnn_boxes:
                cnn_labels[label] = Text(
                    label, font_size=15, color=WHITE,
                ).move_to(cnn_boxes[label].get_center())

            # ----- SNN side -----
            if kind == "se":
                box = make_box(COL_X_SNN, y, SE_FILL, SE_STROKE)
            elif kind == "tf_snn_only":
                box = make_box(COL_X_SNN, y, TF_FILL, TF_STROKE)
            elif kind == "paradigm":
                # Initial state: neutral. Will recolour later.
                box = make_box(COL_X_SNN, y, SHARED_FILL, SHARED_STROKE)
            else:  # shared
                box = make_box(COL_X_SNN, y, SHARED_FILL, SHARED_STROKE)
            snn_boxes[label] = box
            snn_labels[label] = Text(
                label, font_size=15, color=WHITE,
            ).move_to(box.get_center())

        # =====================================================
        # CONNECTING ARROWS BETWEEN STAGES
        # CNN skips the Temporal Fusion row, so its High-Res →
        # Channel Proj arrow visibly spans an extra row's distance.
        # =====================================================
        def make_column_arrows(boxes_dict, ordered_labels):
            arrows = []
            for i in range(len(ordered_labels) - 1):
                top_box = boxes_dict[ordered_labels[i]]
                bot_box = boxes_dict[ordered_labels[i + 1]]
                arrows.append(
                    Arrow(
                        start=top_box.get_bottom(),
                        end=bot_box.get_top(),
                        color=GREY_C,
                        stroke_width=1.6,
                        buff=0.04,
                        max_tip_length_to_length_ratio=0.45,
                    )
                )
            return arrows

        cnn_label_order = [s[0] for s in stages if s[2] != "tf_snn_only"]
        snn_label_order = [s[0] for s in stages]
        cnn_arrows = make_column_arrows(cnn_boxes, cnn_label_order)
        snn_arrows = make_column_arrows(snn_boxes, snn_label_order)

        # =====================================================
        # BELOW-COLUMN LAYOUT — params, ticks, closing
        # =====================================================
        bottom_y = row_y(n_rows - 1)              # centre of last row
        bottom_edge_y = bottom_y - BOX_H / 2      # bottom edge of last box

        params_y = bottom_edge_y - 0.40
        ticks_y = params_y - 0.45
        closing_y = ticks_y - 0.45

        cnn_params = Text(
            "11.73 M params",
            font_size=20, color=CNN_HEADER, weight=BOLD,
        ).move_to([COL_X_CNN, params_y, 0])

        snn_params = Text(
            "11.72 M params",
            font_size=20, color=SNN_HEADER, weight=BOLD,
        ).move_to([COL_X_SNN, params_y, 0])

        approx_symbol = Text(
            "≈", font_size=40, color=WHITE, weight=BOLD,
        ).move_to([0, params_y, 0])

        # Parity-tick row (single VGroup, arranged horizontally)
        parity_ticks = VGroup(
            Text("✓ Same architecture", font_size=16, color=GREY_B),
            Text("·", font_size=16, color=GREY_C),
            Text("✓ Same parameters", font_size=16, color=GREY_B),
            Text("·", font_size=16, color=GREY_C),
            Text("✓ Same hyperparameters", font_size=16, color=GREY_B),
            Text("·", font_size=16, color=GREY_C),
            Text("✓ Same data", font_size=16, color=GREY_B),
        ).arrange(RIGHT, buff=0.20).move_to([0, ticks_y, 0])

        annotation = Text(
            "Only the activation paradigm changes",
            font_size=18, color=GREY_B, slant=ITALIC,
        ).move_to([0, params_y, 0])

        closing = Text(
            "One variable. Variable-isolated comparison.",
            font_size=24, color=WHITE, weight=BOLD,
        ).move_to([0, closing_y, 0])

        # =====================================================
        # ANIMATION SEQUENCE  (~22 sec)
        # =====================================================

        # ---------- Phase 1: Setup  (~4.0 s) ----------

        self.play(Write(title), run_time=0.6)
        self.play(
            FadeIn(cnn_header, shift=DOWN * 0.2),
            FadeIn(snn_header, shift=DOWN * 0.2),
            run_time=0.5,
        )

        # All boxes + labels + arrows fade in via a single LaggedStart
        # so the eye registers two near-mirror columns at once.
        column_objects = []
        for label, _, _ in stages:
            if label in cnn_boxes:
                column_objects.append(cnn_boxes[label])
                column_objects.append(cnn_labels[label])
            column_objects.append(snn_boxes[label])
            column_objects.append(snn_labels[label])
        column_objects.extend(cnn_arrows)
        column_objects.extend(snn_arrows)

        self.play(
            LaggedStart(
                *[FadeIn(o) for o in column_objects],
                lag_ratio=0.025,
            ),
            run_time=2.4,
        )
        self.wait(0.5)

        # ---------- Phase 2: Paradigm reveal  (~5.5 s) ----------

        paradigm_specific = ["Stem", "Block 1", "Block 2", "High-Res"]

        self.play(
            *[
                cnn_boxes[lbl]
                .animate.set_fill(CNN_PARADIGM_FILL, opacity=0.95)
                .set_stroke(CNN_PARADIGM_STROKE, width=2.0)
                for lbl in paradigm_specific
            ],
            *[
                snn_boxes[lbl]
                .animate.set_fill(SNN_PARADIGM_FILL, opacity=0.95)
                .set_stroke(SNN_PARADIGM_STROKE, width=2.0)
                for lbl in paradigm_specific
            ],
            run_time=1.6,
        )
        self.play(FadeIn(annotation, shift=UP * 0.2), run_time=0.7)
        self.wait(3.0)

        # ---------- Phase 3: Param tags + parity ticks  (~7.0 s) ----------

        self.play(FadeOut(annotation, shift=DOWN * 0.2), run_time=0.4)

        self.play(
            FadeIn(cnn_params, shift=UP * 0.2),
            FadeIn(snn_params, shift=UP * 0.2),
            run_time=0.7,
        )
        self.play(FadeIn(approx_symbol, scale=1.4), run_time=0.5)
        self.wait(0.6)

        self.play(
            LaggedStart(
                *[FadeIn(t) for t in parity_ticks],
                lag_ratio=0.18,
            ),
            run_time=2.2,
        )
        self.wait(2.0)

        # ---------- Phase 4: Closing caption  (~6.0 s) ----------
        # Long hold so the voiceover's closing line
        # "...attributable to the spiking mechanism alone" can land
        # while the full composition is on screen.

        self.play(FadeIn(closing, shift=UP * 0.3), run_time=0.7)
        self.wait(5.0)
