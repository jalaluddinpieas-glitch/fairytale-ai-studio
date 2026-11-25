import json, re, sys
from pathlib import Path

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "fairy-tale"

def main():
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python story_planner.py "Your story title"')
    title = " ".join(sys.argv[1:])
    plan = {
        "title": title,
        "genre": "original family fantasy adventure",
        "visual_style": "cinematic stylized 3D animation, expressive original characters, detailed environments, soft volumetric lighting",
        "characters": [
            {"name":"Mira","design":"small adventurous traveler, teal cloak, copper compass, expressive eyes"},
            {"name":"Bramble","design":"round moss-covered forest guardian, glowing seed pods, warm amber eyes"}
        ],
        "scenes": [
            {"number":1,"purpose":"Hook","beat":"A strange visual event reveals the central mystery.","emotion":"wonder"},
            {"number":2,"purpose":"Adventure","beat":"The hero discovers a clue and follows it.","emotion":"curiosity"},
            {"number":3,"purpose":"Obstacle","beat":"A playful but meaningful challenge blocks the path.","emotion":"tension"},
            {"number":4,"purpose":"Setback","beat":"A wrong assumption causes a setback.","emotion":"concern"},
            {"number":5,"purpose":"Discovery","beat":"A hidden truth reframes the mystery.","emotion":"surprise"},
            {"number":6,"purpose":"Climax","beat":"The hero makes a selfless choice.","emotion":"courage"},
            {"number":7,"purpose":"Resolution","beat":"The world changes for the better.","emotion":"warmth"}
        ]
    }
    out = Path("stories"); out.mkdir(exist_ok=True)
    data = json.dumps(plan, indent=2, ensure_ascii=False)
    (out / (slugify(title)+".json")).write_text(data, encoding="utf-8")
    (out / "latest_story.json").write_text(data, encoding="utf-8")
    print("Story plan saved in stories/")

if __name__ == "__main__": main()
