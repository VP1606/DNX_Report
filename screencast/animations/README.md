# Screencast Animations (Manim)

Manim Community Edition animations for the DetectorNX screencast.

## Files in this folder

| File | Scene class | Used in | Length |
|---|---|---|---|
| `cnn_inference.py` | `CNNInference` | Sub-beat 2C — first half (CNN cost reveal) | ~8.5 s |
| `trajectory_graph.py` | `TrajectoryGraph` | Sub-beat 2C — second half (compute vs budget) | ~13 s |

## Setup (one-time)

Install Manim Community Edition:

```bash
# macOS
brew install py3cairo ffmpeg
pip install manim

# Ubuntu / Debian
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg
pip install manim

# Windows
# See https://docs.manim.community/en/stable/installation/windows.html
```

Verify install:

```bash
manim --version
# Should report: Manim Community v0.18.x or later
```

## Render commands

Replace `<file>.py <Scene>` with whichever animation you're rendering, e.g.
`trajectory_graph.py TrajectoryGraph` or `cnn_inference.py CNNInference`.

### Preview (fast, low-quality, useful for iteration)

```bash
manim -pql trajectory_graph.py TrajectoryGraph
manim -pql cnn_inference.py    CNNInference
```

### Final 1080p MP4 (use these for the screencast)

```bash
manim -pqh trajectory_graph.py TrajectoryGraph
manim -pqh cnn_inference.py    CNNInference
```

### Final 4K MP4 (overkill, but available)

```bash
manim -pqk trajectory_graph.py TrajectoryGraph
manim -pqk cnn_inference.py    CNNInference
```

The `-p` flag opens the rendered video automatically when done.

## Output location

Manim writes the rendered MP4 to:

```
media/videos/trajectory_graph/{quality}/TrajectoryGraph.mp4
```

For example, `-pqh` produces:

```
media/videos/trajectory_graph/1080p60/TrajectoryGraph.mp4
```

You can drag this MP4 directly into a Keynote slide.

## Tweaking the animation

The most likely tweaks for `trajectory_graph.py`:

| What you might change | Where in the file |
|---|---|
| Curve shapes (compute / power) | `power_budget` and `compute_demand` lambda functions |
| Colours | `color=GREEN` / `color=RED` / `color=YELLOW` etc. |
| Animation speeds | `run_time=` parameters in `self.play(...)` calls |
| Final hold time | `self.wait(1.5)` at the end |
| Text sizes | `font_size=` on each `Text()` |
| Background colour | `self.camera.background_color = "#0F1419"` |
| Y-axis range | `y_range=[0, 50, 10]` in the `Axes(...)` definition |
| Year labels | `numbers_to_include` in `x_axis_config` |

## Embedding in Keynote

1. Render the high-quality MP4 with `manim -pqh trajectory_graph.py TrajectoryGraph`
2. Open Keynote, navigate to the Sub-beat 2C slide
3. Drag the MP4 from Finder onto the slide
4. Set the movie to "Start movie on click" (Inspector → Movie tab)
5. Position and size as needed
6. The Manim background colour (`#0F1419`) matches a dark slide; you can match the slide background for seamless integration

## Time alignment

The animation runs ~13 seconds. The voiceover for the trajectory-graph segment of Sub-beat 2C runs from approximately 1:05 to 1:18 in the screencast — matching the animation length.

## Notes

- The numbers in the curve functions are illustrative, not directly fitted to literature data. Adjust the `power_budget` and `compute_demand` functions if you want different shapes.
- The saturation markers (2018 for CPU, 2026 for GPU) are positioned on the compute-demand curve. If you change the curve function, recompute the marker positions.
- The final question mark deliberately sits to the right of the visible curve — the implied "what comes next?" is the bridge to Beat 3 (Aims).
