"""Create a simple original fairy-tale story plan from a title.

This is a deterministic starter template, not an AI story-generation model.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

OUT = Path("stories")
OUT.mkdir(exist_ok=True)

def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "fairy-tale"

def build_plan(title: str) -> dict:
    return {
        "title": title,
        "genre": "original fantasy adventure",
        "audience": "family",
        "visual_style": "cinematic stylized 3D animation, expressive original characters, detailed environments, soft volumetric lighting, polished materials",
        "originality_rules": [
            "Use original character designs, names, settings, and plot details.",
            "Do not imitate existing studio characters, films, or copyrighted story adaptations."
        ],
        "logline": f"An unlikely young hero discovers that the mystery behind {title} can only be solved through courage, empathy, and a difficult choice.",
        "characters": [
            {"name": "Mira", "role": "curious young mapmaker", "design": "small adventurous traveler, teal cloak, copper compass, expressive eyes"},
            {"name": "Bramble", "role": "gentle forest guardian", "design": "round moss-covered creature, tiny glowing seed pods, warm amber eyes"}
        ],
        "scenes": [
            {"number": 1, "purpose": "Hook", "beat": "A strange visual event interrupts an ordinary day and reveals the central mystery.", "emotion": "wonder"},
            {"number": 2, "purpose": "Call to adventure", "beat": "The hero discovers a clue and decides to follow it.", "emotion": "curiosity"},
            {"number": 3, "purpose": "First obstacle", "beat": "The path presents a playful but meaningful challenge.", "emotion": "tension"},
            {"number": 4, "purpose": "Complication", "beat": "A wrong assumption causes a setback; the hero must listen and adapt.", "emotion": "concern"},
            {"number": 5, "purpose": "Discovery", "beat": "The companion reveals a hidden truth that reframes the mystery.", "emotion": "surprise"},
            {"number": 6, "purpose": "Climax", "beat": "The hero makes a selfless choice that resolves the central conflict.", "emotion": "courage"},
            {"number": 7, "purpose": "Resolution", "beat": "The world changes for the better and the story ends on a memorable image.", "emotion": "warmth"}
        ]
    }

def main() -> None:
    if len(sys.argv) < 2:
        print('Usage: python -m app.story_planner "Your story title"')
        raise SystemExit(2)
    title = " ".join(sys.argv[1:]).strip()
    plan = build_plan(title)
    path = OUT / f"{slugify(title)}.json"
    path.write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    (OUT / "latest_story.json").write_text(json.dumps(plan, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Story plan saved: {path}")
    print(f"Latest story saved: {OUT / 'latest_story.json'}")

if __name__ == "__main__":
    main()
