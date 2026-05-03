"""
Sparsity Grid — Sub-beat 3A
DetectorNX Screencast — Beat 3 (SNN Introduction)

Side-by-side comparison of per-frame network activation density:
  - LEFT  (CNN): every cell continuously coloured by a smooth heatmap
                 — "always on", 100% active each frame
  - RIGHT (SNN): mostly black cells; ~5-8% flash white per frame and
                 different cells fire each frame — "mostly silent"
  - Counters under each grid show "% active each frame".
  - Closing card replaces the grids: "no spike → no computation → no power".

Total length ~19.6 sec, paired with the sparsity slot of Sub-beat 3A
(1:55 - 2:15 in the original timeline / wherever this slots in
current_timeline.md).

Render commands:
  Preview (fast):
      manim -pql sparsity_grid.py SparsityGrid

  Final 1080p:
      manim -pqh sparsity_grid.py SparsityGrid

Output goes to:
  media/videos/sparsity_grid/{quality}/SparsityGrid.mp4
"""

from manim import *
import numpy as np


class SparsityGrid(Scene):
    def construct(self):
        # Pure black background — matches lif_neuron.py / cnn_inference.py
        self.camera.background_color = "#000000"
        np.random.seed(42)

        # =====================================================
        # PARAMETERS
        # =====================================================
        grid_size = 12          # 12 x 12 cells per grid
        cell_size = 0.28        # screen units per cell side
        cell_buff = 0.04        # gap between cells

        snn_active_min = 7      # ≈ 4.9% of 144 cells
        snn_active_max = 11     # ≈ 7.6% of 144 cells
        n_snapshots = 14        # number of "frames" of activity to play
        snapshot_dur = 1.0      # seconds per snapshot

        # =====================================================
        # TITLE
        # =====================================================
        title = Text(
            "Per-frame network activation",
            font_size=30,
            color=WHITE,
        ).to_edge(UP, buff=0.35)

        # =====================================================
        # GRID GEOMETRY
        # =====================================================
        # Each grid occupies grid_total_size x grid_total_size units.
        grid_total_size = (
            grid_size * cell_size + (grid_size - 1) * cell_buff
        )
        cnn_centre = np.array([-3.4, -0.3, 0])
        snn_centre = np.array([ 3.4, -0.3, 0])

        def make_grid(centre):
            """Build a list of lists of Square cells centred at `centre`."""
            n = grid_size
            x0 = centre[0] - grid_total_size / 2 + cell_size / 2
            y0 = centre[1] + grid_total_size / 2 - cell_size / 2
            cells = []
            for i in range(n):
                row = []
                for j in range(n):
                    x = x0 + j * (cell_size + cell_buff)
                    y = y0 - i * (cell_size + cell_buff)
                    cell = Square(
                        side_length=cell_size,
                        stroke_color=GREY_E,
                        stroke_width=0.6,
                        fill_color=BLACK,
                        fill_opacity=1.0,
                    ).move_to([x, y, 0])
                    row.append(cell)
                cells.append(row)
            return cells

        # ----- CNN heatmap pattern (always on, varying intensity) -----
        # Smooth pseudo-noise so adjacent cells look related.
        cnn_intensities = np.zeros((grid_size, grid_size))
        for i in range(grid_size):
            for j in range(grid_size):
                v = (
                    0.55
                    + 0.30 * np.sin(0.7 * i + 0.4 * j)
                    + 0.20 * np.cos(0.3 * i - 0.6 * j + 1.0)
                )
                cnn_intensities[i, j] = float(np.clip(v, 0.18, 0.95))

        cnn_grid = make_grid(cnn_centre)
        for i in range(grid_size):
            for j in range(grid_size):
                cnn_grid[i][j].set_fill(RED, opacity=cnn_intensities[i, j])
        cnn_cells_flat = [c for row in cnn_grid for c in row]

        # ----- SNN grid starts entirely black -----
        snn_grid = make_grid(snn_centre)
        snn_cells_flat = [c for row in snn_grid for c in row]

        # =====================================================
        # LABELS
        # =====================================================
        cnn_label = Text(
            "CNN", font_size=28, color=GREY_B,
        ).move_to([cnn_centre[0],
                   cnn_centre[1] + grid_total_size / 2 + 0.42, 0])
        snn_label = Text(
            "SNN", font_size=28, color=GREY_B,
        ).move_to([snn_centre[0],
                   snn_centre[1] + grid_total_size / 2 + 0.42, 0])

        # =====================================================
        # COUNTERS
        # =====================================================
        cnn_counter_value = DecimalNumber(
            100.0,
            num_decimal_places=0,
            color=RED,
            font_size=36,
            unit="\\%",
        )
        cnn_counter_caption = Text(
            "active each frame", font_size=18, color=GREY_B,
        )
        cnn_counter = VGroup(
            cnn_counter_value, cnn_counter_caption
        ).arrange(DOWN, buff=0.10).move_to(
            [cnn_centre[0],
             cnn_centre[1] - grid_total_size / 2 - 0.55, 0]
        )

        snn_counter_value = DecimalNumber(
            0.0,
            num_decimal_places=1,
            color=WHITE,
            font_size=36,
            unit="\\%",
        )
        snn_counter_caption = Text(
            "active each frame", font_size=18, color=GREY_B,
        )
        snn_counter = VGroup(
            snn_counter_value, snn_counter_caption
        ).arrange(DOWN, buff=0.10).move_to(
            [snn_centre[0],
             snn_centre[1] - grid_total_size / 2 - 0.55, 0]
        )

        # =====================================================
        # ANIMATION SEQUENCE  (~19.6 sec)
        # =====================================================

        # ----- SETUP  (~2.6 sec) -----

        # Step 1: Title  (0.5s)
        self.play(Write(title), run_time=0.5)

        # Step 2: CNN/SNN labels  (0.4s)
        self.play(
            Write(cnn_label),
            Write(snn_label),
            run_time=0.4,
        )

        # Step 3: Grids fade in cell-by-cell  (1.2s)
        cnn_grid_group = VGroup(*cnn_cells_flat)
        snn_grid_group = VGroup(*snn_cells_flat)
        self.play(
            FadeIn(cnn_grid_group, lag_ratio=0.005),
            FadeIn(snn_grid_group, lag_ratio=0.005),
            run_time=1.2,
        )

        # Step 4: Counters appear  (0.5s)
        self.play(
            FadeIn(cnn_counter),
            FadeIn(snn_counter),
            run_time=0.5,
        )

        # ----- DYNAMICS  (14 snapshots × 1.0s = 14.0 sec) -----
        # Each snapshot:
        #   (a) ~5-8% of SNN cells flash white; previously-active cells
        #       go back to black
        #   (b) SNN counter updates to the new percentage
        #   (c) Brief hold so the eye registers the new pattern

        prev_active = []
        for snap in range(n_snapshots):
            n_active = np.random.randint(snn_active_min, snn_active_max + 1)
            active_idx = np.random.choice(144, size=n_active, replace=False)
            new_active = [snn_cells_flat[k] for k in active_idx]
            new_pct = (n_active / 144) * 100

            anims = []
            # Deactivate cells that were on but aren't now
            for c in prev_active:
                if c not in new_active:
                    anims.append(c.animate.set_fill(BLACK, opacity=1.0))
            # Activate new cells
            for c in new_active:
                if c not in prev_active:
                    anims.append(c.animate.set_fill(WHITE, opacity=1.0))
            # Update SNN counter
            anims.append(ChangeDecimalToValue(snn_counter_value, new_pct))

            self.play(*anims, run_time=snapshot_dur * 0.35)
            self.wait(snapshot_dur * 0.65)
            prev_active = new_active

        # ----- CLOSING CARD  (~3.0 sec) -----

        closing_card = Text(
            "no spike   →   no computation   →   no power",
            font_size=40,
            color=WHITE,
            weight=BOLD,
        ).move_to(ORIGIN)

        # Fade the grids, labels, counters, and title out together
        self.play(
            FadeOut(cnn_grid_group),
            FadeOut(snn_grid_group),
            FadeOut(cnn_label),
            FadeOut(snn_label),
            FadeOut(cnn_counter),
            FadeOut(snn_counter),
            FadeOut(title),
            run_time=0.7,
        )
        self.play(FadeIn(closing_card, shift=UP * 0.3), run_time=0.7)
        self.wait(1.6)
