"""Convert a story JSON file into individual scene prompt text files."""
from __future__ import annotations
import json
import sys
from pathlib import Path

OUT = Path("scenes")
OUT.mkdir(exist_ok=True)

def build_prompt(plan: dict, scene: dict) -> str:
    characters = ", ".join(
        f"{c['name']} ({c['design']})" for c in plan.get("characters", [])
    )
    return f"""PROJECT: {plan.get('title', 'Untitled')}
SCENE: {scene.get('number', 0):02d} — {scene.get('purpose', 'Scene')}
STORY BEAT: {scene.get('beat', '')}
EMOTION: {scene.get('emotion', 'wonder')}

CHARACTER CONTINUITY:
{characters}

VISUAL DIRECTION:
{plan.get('visual_style', '')}
Original cinematic 3D animated family fantasy. Maintain identical character proportions,
wardrobe, colors, facial features, and accessories across shots. Clear readable action,
expressive facial animation, natural body mechanics, appealing composition, motivated
camera movement, detailed environment, cinematic lighting.

NEGATIVE DIRECTION:
No logos, no watermarks, no subtitles, no random extra characters, no character redesign,
no flicker, no malformed anatomy, no imitation of existing copyrighted characters or films.
"""

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python -m app.prompt_builder stories/latest_story.json")
        raise SystemExit(2)
    source = Path(sys.argv[1])
    plan = json.loads(source.read_text(encoding="utf-8"))
    for scene in plan.get("scenes", []):
        path = OUT / f"scene_{scene['number']:02d}.txt"
        path.write_text(build_prompt(plan, scene), encoding="utf-8")
        print(f"Created {path}")

if __name__ == "__main__":
    main()
