import json, sys
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python prompt_builder.py stories/latest_story.json")
    plan = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    out = Path("scenes"); out.mkdir(exist_ok=True)
    for scene in plan.get("scenes", []):
        chars = ", ".join(c["name"]+" ("+c["design"]+")" for c in plan.get("characters", []))
        prompt = f"""PROJECT: {plan["title"]}
SCENE {scene["number"]:02d}: {scene["purpose"]}
STORY BEAT: {scene["beat"]}
EMOTION: {scene["emotion"]}
CHARACTERS: {chars}
STYLE: {plan["visual_style"]}
Keep character designs consistent. Use expressive facial animation, natural body mechanics,
clear action, motivated camera movement, detailed environments, and cinematic lighting.
No logos, watermarks, subtitles, random extra characters, flicker, malformed anatomy,
or imitation of existing copyrighted characters or films.
"""
        (out / f"scene_{scene['number']:02d}.txt").write_text(prompt, encoding="utf-8")
        print("Created", out / f"scene_{scene['number']:02d}.txt")

if __name__ == "__main__": main()
