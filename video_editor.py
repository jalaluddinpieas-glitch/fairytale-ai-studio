"""Assemble pre-rendered MP4 scene clips with FFmpeg concat demuxer."""
from __future__ import annotations
import sys
import subprocess
import tempfile
from pathlib import Path

def main() -> None:
    if len(sys.argv) != 3:
        print("Usage: python -m app.video_editor <clips_folder> <output.mp4>")
        raise SystemExit(2)
    clips_dir = Path(sys.argv[1])
    output = Path(sys.argv[2])
    clips = sorted(clips_dir.glob("scene_*.mp4"))
    if not clips:
        raise SystemExit(f"No scene_*.mp4 clips found in {clips_dir}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        list_file = Path(f.name)
        for clip in clips:
            escaped = str(clip.resolve()).replace("'", r"'\''")
            f.write(f"file '{escaped}'\n")
    try:
        subprocess.run([
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", str(list_file), "-c", "copy", str(output)
        ], check=True)
    except FileNotFoundError:
        raise SystemExit("FFmpeg was not found. Install FFmpeg and add it to PATH.")
    finally:
        list_file.unlink(missing_ok=True)
    print(f"Final video created: {output}")

if __name__ == "__main__":
    main()
