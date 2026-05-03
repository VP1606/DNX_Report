#!/usr/bin/env python3
"""Encode an `audit_sample_*.png` frame sequence to an MP4 via ffmpeg."""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

FRAME_GLOB = "audit_sample_*.png"
FRAME_RE = re.compile(r"audit_sample_(\d+)\.png$")


def collect_frames(folder: Path) -> list[Path]:
    frames = sorted(folder.glob(FRAME_GLOB), key=lambda p: int(FRAME_RE.search(p.name).group(1)))
    if not frames:
        sys.exit(f"No frames matching {FRAME_GLOB} in {folder}")
    indices = [int(FRAME_RE.search(p.name).group(1)) for p in frames]
    expected = list(range(indices[0], indices[0] + len(indices)))
    if indices != expected:
        missing = sorted(set(expected) - set(indices))
        sys.exit(f"Frame sequence in {folder} is not contiguous; missing indices: {missing[:10]}{'...' if len(missing) > 10 else ''}")
    return frames


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input_dir", type=Path, help="Folder containing audit_sample_NNN.png frames")
    p.add_argument("--fps", type=float, required=True, help="Output frame rate (frames per second)")
    p.add_argument("-o", "--output", type=Path, help="Output mp4 path (default: <input_dir>.mp4 next to the folder)")
    p.add_argument("--crf", type=int, default=18, help="x264 CRF quality (lower = better, default 18)")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    if not shutil.which("ffmpeg"):
        sys.exit("ffmpeg not found on PATH")
    if not args.input_dir.is_dir():
        sys.exit(f"Not a directory: {args.input_dir}")
    if args.fps <= 0:
        sys.exit("--fps must be positive")

    frames = collect_frames(args.input_dir)
    start_index = int(FRAME_RE.search(frames[0].name).group(1))

    output = args.output or args.input_dir.with_suffix(".mp4")
    output.parent.mkdir(parents=True, exist_ok=True)

    pattern = str(args.input_dir / "audit_sample_%03d.png")
    cmd = [
        "ffmpeg",
        "-y",
        "-framerate", f"{args.fps}",
        "-start_number", str(start_index),
        "-i", pattern,
        "-frames:v", str(len(frames)),
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", str(args.crf),
        "-vf", "pad=ceil(iw/2)*2:ceil(ih/2)*2",
        str(output),
    ]

    print(f"Encoding {len(frames)} frames @ {args.fps} fps -> {output}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
