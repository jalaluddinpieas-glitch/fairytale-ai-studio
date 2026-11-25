# Fairy Tale AI Studio

A starter scaffold for an original 3D fairy-tale production workflow.

## What this starter does
- Turns a story title into a structured original story outline (template-based; no external LLM is connected yet).
- Converts story beats into scene prompt files.
- Can assemble already-rendered video clips into one MP4 using FFmpeg.

## What it does NOT do yet
- It does not generate cinematic 3D video by itself.
- It does not include a paid/free AI video model or guarantee Pixar-level output.
- It does not upload videos to YouTube automatically.

## Quick start
1. Install Python 3.10+.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a story plan:
   `python -m app.story_planner "The Moonlit Clockwork Forest"`
4. Build scene prompts:
   `python -m app.prompt_builder stories/latest_story.json`
5. Put your generated/rendered clips in `outputs/clips/` named `scene_01.mp4`, `scene_02.mp4`, etc.
6. Assemble:
   `python -m app.video_editor outputs/clips outputs/final_fairy_tale.mp4`

FFmpeg must be installed separately and available on PATH.

## Project structure
- `app/` workflow scripts
- `characters/characters.json` original character bible template
- `config/settings.json` production defaults
- `stories/` generated story plans
- `scenes/` scene prompts
- `outputs/` rendered clips and final videos

## Next development milestone
Connect an actual story-generation model and a legal video-generation/rendering backend. Keep API keys in environment variables; never commit secrets to GitHub.
