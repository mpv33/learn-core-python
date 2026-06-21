"""
06 — JSON Files
===============

THEORY
------
What:
  JSON (JavaScript Object Notation) is a text format for structured data. Python's
  `json` module maps JSON objects/arrays to dicts/lists and back.

Why:
  JSON is the lingua franca of APIs, config files, and data exchange. Every Python
  developer reads and writes JSON daily.

Key rules:
  - `json.dump(obj, file)` writes to file; `json.load(file)` reads from file.
  - `json.dumps(obj)` → string; `json.loads(string)` → Python object.
  - JSON types: string, number, boolean, null, array, object — maps to Python primitives.
  - `datetime`, custom classes are NOT JSON-serializable — use `default=` handler.
  - `indent=2` pretty-prints; omit for compact production output.

When to use:
  - API request/response bodies, config files, caching structured data.
  - Interchanging data with JavaScript, mobile apps, or other services.

Common mistakes:
  - Forgetting `default=` for datetime/Decimal/custom types — TypeError on dump.
  - Using single quotes in JSON — JSON requires double quotes for strings.
  - Assuming JSON keys stay as integers — JSON object keys are always strings.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/06_json_files.py
"""

import json  # encode/decode JSON data
from datetime import datetime  # datetime needs custom JSON handler
from pathlib import Path  # build filesystem paths


def json_encoder(obj):
    if isinstance(obj, datetime):  # handle datetime instances
        return obj.isoformat()  # convert to ISO 8601 string
    raise TypeError(f"Not serializable: {type(obj)}")  # reject unsupported types


def main() -> None:
    demo_file = Path(__file__).parent / "data.json"  # temporary JSON file beside script

    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — Python object to JSON file")  # label first block
    print("=" * 50)  # close header

    user = {  # nested dict representing a user record
        "name": "Alice",  # string field
        "age": 30,  # integer field
        "skills": ["Python", "SQL", "Git"],  # list of strings
        "active": True,  # boolean field
        "score": None,  # null becomes JSON null
    }
    with open(demo_file, "w", encoding="utf-8") as f:  # open file for writing text
        json.dump(user, f, indent=2)  # serialize with pretty indentation
    print("JSON written.")  # confirm file write

    print("\n" + "=" * 50)  # divider before load demo
    print("PRACTICE 2 — JSON file to Python object")  # label second block
    print("=" * 50)  # close header

    with open(demo_file, "r", encoding="utf-8") as f:  # reopen for reading
        loaded = json.load(f)  # parse JSON into Python dict
    print(f"Loaded: {loaded}")  # show deserialized object
    print(f"Name: {loaded['name']}, Skills: {loaded['skills']}")  # access nested fields

    print("\n" + "=" * 50)  # divider before string conversion demo
    print("PRACTICE 3 — String conversion (no file)")  # label third block
    print("=" * 50)  # close header

    json_str = json.dumps(user, indent=2)  # serialize dict to formatted string
    parsed = json.loads(json_str)  # parse string back into Python object
    print(f"From string: {parsed['name']}")  # demonstrate in-memory round trip
    print(f"JSON string length: {len(json_str)} chars")  # show serialized size

    print("\n" + "=" * 50)  # divider before custom encoder demo
    print("PRACTICE 4 — Custom types with default handler")  # label fourth block
    print("=" * 50)  # close header

    event = {"title": "Meeting", "when": datetime(2026, 6, 21, 10, 0)}  # dict with datetime
    print(f"Custom encode: {json.dumps(event, default=json_encoder)}")  # serialize with handler
    demo_file.unlink()  # remove temporary JSON file
    print("Demo file cleaned up.")  # confirm removal


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
