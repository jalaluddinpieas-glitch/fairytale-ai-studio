# Fairy Tale AI Studio — Starter
This iPhone-friendly starter keeps code files in the repository root.

## What it currently does
- Creates a template-based story outline from a title.
- Creates one text prompt per scene.
- Joins already-rendered MP4 clips with FFmpeg.

## Important
This is not yet an automatic cinematic 3D video generator. No AI video model, Blender rendering pipeline, voice generation, or YouTube uploader is connected yet.

## Run
Install Python 3.10+ and dependencies:
    pip install -r requirements.txt

Create a story plan:
    python story_planner.py "The Moonlit Clockwork Forest"

Create scene prompts:
    python prompt_builder.py stories/latest_story.json

Put rendered clips in outputs/clips/ as scene_01.mp4, scene_02.mp4, etc.
Join them (FFmpeg required):
    python video_editor.py outputs/clips outputs/final_fairy_tale.mp4

Never commit passwords, tokens, or API keys to this public repository.
