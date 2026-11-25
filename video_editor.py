import sys, subprocess, tempfile
from pathlib import Path

def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python video_editor.py <clips_folder> <output.mp4>")
    clips_dir, output = Path(sys.argv[1]), Path(sys.argv[2])
    clips = sorted(clips_dir.glob("scene_*.mp4"))
    if not clips: raise SystemExit(f"No scene_*.mp4 clips found in {clips_dir}")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
        listing = Path(f.name)
        for clip in clips:
            f.write("file '" + str(clip.resolve()).replace("'", r"\'\''") + "'\\n")
    try:
        subprocess.run(["ffmpeg","-y","-f","concat","-safe","0","-i",str(listing),"-c","copy",str(output)], check=True)
    except FileNotFoundError:
        raise SystemExit("FFmpeg not found. Install FFmpeg and add it to PATH.")
    finally:
        listing.unlink(missing_ok=True)
    print("Created", output)

if __name__ == "__main__": main()
