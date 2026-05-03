"""
Precision Parity Overlay — Sub-beat 6A
DetectorNX Screencast — Beat 6 (Results)

Manim overlay layer that frames the live SNN+CNN demo footage during
Sub-beat 6A. Provides everything around the demo region:
  - Variant-name headers above each demo panel
  - Subtle outline frames marking where the demo videos sit
  - "Verdict panel" beneath the demo with three precision metrics
    fading in progressively, paired to voiceover beats
  - Acronym legend in the bottom-left corner

The two demo clips are composited UNDER this Manim layer in Final Cut
Pro:
    audit_playback/snn_audit_24.mp4 (1426×846, 24 fps, 8.33 s)
    audit_playback/cnn_audit_24.mp4 (1426×846, 24 fps, 8.33 s)
Each loops ~5× to span the 43 s voiceover.

Visual flow:
  1. Variant headers + demo region outlines + acronym legend appear (0-3 s)
  2. "PRECISION PARITY" panel header appears with flanking lines (3-5 s)
  3. mIoU row fades in: 0.461 ↔ 0.486, 94.9% of baseline (5-15 s)
  4. mAP row fades in: 59.8%, 91.3% of baseline (15-25 s)
  5. Recall row fades in with emphasis: 100% ↔ 100%, every vehicle (25-35 s)
  6. Closing summary footer fades in; hold (35-43 s)

Total: ~43 s, paired with the Sub-beat 6A voiceover.

Render commands:
  Preview (fast):
      manim -pql precision_parity_overlay.py PrecisionParityOverlay
  Final 1080p:
      manim -pqh precision_parity_overlay.py PrecisionParityOverlay

Output goes to:
  media/videos/precision_parity_overlay/{quality}/PrecisionParityOverlay.mp4
"""

from manim import *
import numpy as np


class PrecisionParityOverlay(Scene):
    def construct(self):
        self.camera.background_color = "#000000"

        # =====================================================
        # COLOUR PALETTE  (consistent with the rest of the screencast)
        # =====================================================
        SNN_COLOR = "#73C49B"           # green — SNN throughout the screencast
        CNN_COLOR = "#9888D4"           # purple — CNN throughout the screencast
        DEMO_FRAME_COLOR = "#3A3A3A"    # subtle grey, marks demo region edge
        PANEL_LINE_COLOR = "#7A8AAA"    # steel-blue, decorative panel lines
        PARITY_CALLOUT_COLOR = "#C5BEE0"  # pale lavender, slightly distinct
        LEGEND_COLOR = GREY_C

        # =====================================================
        # GEOMETRY
        # =====================================================
        SNN_X = -3.4
        CNN_X =  3.4
        DEMO_W = 6.2
        DEMO_H = 3.70
        DEMO_Y = 1.20

        HEADER_Y = 3.55

        PANEL_HEADER_Y = -0.95
        ROW_Y_MIOU   = -1.55
        ROW_Y_MAP    = -2.00
        ROW_Y_RECALL = -2.45
        FOOTER_Y     = -2.95

        # Verdict-panel column x-positions
        ROW_LABEL_X = -5.4
        SNN_VAL_X   = -1.70
        ARROW_X     = -0.55
        CNN_VAL_X   =  0.65
        PARITY_X    =  4.20

        # =====================================================
        # VARIANT HEADERS (above the demo panels)
        # =====================================================
        snn_header = Text(
            "DetectorNX-G3-SNN",
            font_size=22, color=SNN_COLOR, weight=BOLD,
        ).move_to([SNN_X, HEADER_Y, 0])
        cnn_header = Text(
            "DetectorNX-G3-CNN",
            font_size=22, color=CNN_COLOR, weight=BOLD,
        ).move_to([CNN_X, HEADER_Y, 0])

        # =====================================================
        # DEMO REGION OUTLINES (subtle frames; demo video sits inside)
        # =====================================================
        snn_frame = Rectangle(
            width=DEMO_W, height=DEMO_H,
            stroke_color=DEMO_FRAME_COLOR, stroke_width=1.6,
            fill_opacity=0,
        ).move_to([SNN_X, DEMO_Y, 0])
        cnn_frame = Rectangle(
            width=DEMO_W, height=DEMO_H,
            stroke_color=DEMO_FRAME_COLOR, stroke_width=1.6,
            fill_opacity=0,
        ).move_to([CNN_X, DEMO_Y, 0])

        # =====================================================
        # VERDICT PANEL HEADER  ("PRECISION PARITY")
        # =====================================================
        panel_header = Text(
            "PRECISION PARITY",
            font_size=22, color=WHITE, weight=BOLD,
        ).move_to([0, PANEL_HEADER_Y, 0])

        # Decorative horizontal lines flanking the header
        line_left = Line(
            np.array([-6.30, PANEL_HEADER_Y, 0]),
            np.array([-2.40, PANEL_HEADER_Y, 0]),
            color=PANEL_LINE_COLOR, stroke_width=1.0,
        )
        line_right = Line(
            np.array([2.40, PANEL_HEADER_Y, 0]),
            np.array([6.30, PANEL_HEADER_Y, 0]),
            color=PANEL_LINE_COLOR, stroke_width=1.0,
        )

        # =====================================================
        # METRIC ROWS — helper builders
        # =====================================================
        def row_label(text, y):
            return Text(
                text, font_size=18, color=GREY_B,
            ).move_to([ROW_LABEL_X, y, 0])

        def snn_value(text, y):
            return Text(
                text, font_size=20, color=SNN_COLOR, weight=BOLD,
            ).move_to([SNN_VAL_X, y, 0])

        def cnn_value(text, y):
            return Text(
                text, font_size=20, color=CNN_COLOR, weight=BOLD,
            ).move_to([CNN_VAL_X, y, 0])

        def arrow_separator(y):
            return Text("↔", font_size=20, color=GREY_C).move_to([ARROW_X, y, 0])

        def parity_callout(text, y, color=None, slant=ITALIC):
            return Text(
                text,
                font_size=16,
                color=color or PARITY_CALLOUT_COLOR,
                slant=slant,
            ).move_to([PARITY_X, y, 0])

        # ----- mIoU row -----
        miou_label  = row_label("mean IoU", ROW_Y_MIOU)
        miou_snn    = snn_value("0.461",    ROW_Y_MIOU)
        miou_arrow  = arrow_separator(      ROW_Y_MIOU)
        miou_cnn    = cnn_value("0.486",    ROW_Y_MIOU)
        miou_parity = parity_callout("94.9% of baseline", ROW_Y_MIOU)

        # ----- mAP row -----
        map_label  = row_label("mAP @ 0.5", ROW_Y_MAP)
        map_snn    = snn_value("59.8%",     ROW_Y_MAP)
        map_arrow  = arrow_separator(       ROW_Y_MAP)
        map_cnn    = cnn_value("65.5%",     ROW_Y_MAP)
        map_parity = parity_callout("91.3% of baseline", ROW_Y_MAP)

        # ----- Recall row (qualifier "IoU > 0.5" baked into the label) -----
        recall_label  = row_label("Recall (IoU > 0.5)", ROW_Y_RECALL)
        recall_snn    = snn_value("100%",    ROW_Y_RECALL)
        recall_arrow  = arrow_separator(    ROW_Y_RECALL)
        recall_cnn    = cnn_value("100%",    ROW_Y_RECALL)
        recall_parity = parity_callout(
            "every vehicle found", ROW_Y_RECALL,
            color=YELLOW,
        )

        # =====================================================
        # CLOSING FOOTER (~optional summary)
        # =====================================================
        closing_footer = Text(
            "~5% precision cost  ·  matched on detection completeness",
            font_size=15, color=GREY_C, slant=ITALIC,
        ).move_to([0, FOOTER_Y, 0])

        # =====================================================
        # ACRONYM LEGEND  (bottom-left corner)
        # =====================================================
        legend = VGroup(
            Text(
                "IoU = Intersection over Union",
                font_size=13, color=LEGEND_COLOR, slant=ITALIC,
            ),
            Text(
                "mAP = mean Average Precision",
                font_size=13, color=LEGEND_COLOR, slant=ITALIC,
            ),
        ).arrange(DOWN, buff=0.10, aligned_edge=LEFT).to_corner(DL, buff=0.30)

        # =====================================================
        # ANIMATION SEQUENCE  (~43 s total)
        # =====================================================

        # ---------- Phase 1: setup (~3.0 s) ----------
        self.play(
            Write(snn_header),
            Write(cnn_header),
            run_time=0.7,
        )
        self.play(
            Create(snn_frame),
            Create(cnn_frame),
            run_time=0.6,
        )
        self.play(
            FadeIn(legend),
            run_time=0.6,
        )
        self.wait(1.1)

        # ---------- Phase 2: panel header (~2.0 s) ----------
        self.play(
            Create(line_left),
            Create(line_right),
            Write(panel_header),
            run_time=1.2,
        )
        self.wait(0.8)

        # ---------- Phase 3: mIoU row (~10.0 s) ----------
        self.play(Write(miou_label), run_time=0.6)
        self.play(
            FadeIn(miou_snn, scale=0.95),
            FadeIn(miou_cnn, scale=0.95),
            FadeIn(miou_arrow),
            run_time=0.8,
        )
        self.play(
            FadeIn(miou_parity, shift=LEFT * 0.20),
            run_time=0.6,
        )
        self.wait(8.0)

        # ---------- Phase 4: mAP row (~10.0 s) ----------
        self.play(Write(map_label), run_time=0.6)
        self.play(
            FadeIn(map_snn, scale=0.95),
            FadeIn(map_cnn, scale=0.95),
            FadeIn(map_arrow),
            run_time=0.8,
        )
        self.play(
            FadeIn(map_parity, shift=LEFT * 0.20),
            run_time=0.6,
        )
        self.wait(8.0)

        # ---------- Phase 5: Recall row + emphasis (~10.0 s) ----------
        self.play(Write(recall_label), run_time=0.6)
        self.play(
            FadeIn(recall_snn, scale=0.95),
            FadeIn(recall_cnn, scale=0.95),
            FadeIn(recall_arrow),
            run_time=0.8,
        )
        self.play(
            FadeIn(recall_parity, shift=LEFT * 0.20),
            Indicate(recall_snn, scale_factor=1.15, color=YELLOW),
            Indicate(recall_cnn, scale_factor=1.15, color=YELLOW),
            run_time=1.0,
        )
        self.wait(7.6)

        # ---------- Phase 6: closing footer + hold (~7.8 s) ----------
        self.play(FadeIn(closing_footer, shift=UP * 0.20), run_time=0.8)
        self.wait(7.0)
