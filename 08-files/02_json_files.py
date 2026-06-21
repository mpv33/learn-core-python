"""02 — JSON Files"""

import json
from pathlib import Path

demo_file = Path(__file__).parent / "data.json"

# Python object → JSON
user = {
    "name": "Alice",
    "age": 30,
    "skills": ["Python", "SQL", "Git"],
    "active": True,
    "score": None,
}

with open(demo_file, "w", encoding="utf-8") as f:
    json.dump(user, f, indent=2)
print("JSON written.")

# JSON → Python object
with open(demo_file, "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(f"Loaded: {loaded}")
print(f"Name: {loaded['name']}, Skills: {loaded['skills']}")

# String conversion (no file)
json_str = json.dumps(user, indent=2)
parsed = json.loads(json_str)
print(f"\nFrom string: {parsed['name']}")

# Custom types need default handler
from datetime import datetime

def json_encoder(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Not serializable: {type(obj)}")

event = {"title": "Meeting", "when": datetime(2026, 6, 21, 10, 0)}
print(f"\nCustom encode: {json.dumps(event, default=json_encoder)}")

demo_file.unlink()
