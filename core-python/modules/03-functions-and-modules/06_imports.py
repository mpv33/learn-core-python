"""
06 — Import Styles

THEORY
------
What is it?
    Imports load modules (files or packages) so you can use their functions,
    classes, and variables. Python searches sys.path for modules and caches
    loaded ones in sys.modules to avoid reloading.

Why it matters
    Import style affects readability, namespace pollution, and startup time.
    Understanding import paths, aliases, and dynamic imports is key for
    structuring projects and debugging "ModuleNotFoundError".

Key syntax/rules
    - import math — loads module; access as math.sqrt()
    - from math import sqrt — imports name directly into current namespace
    - import json as js — alias for shorter or clearer references
    - from package import * — imports all public names (avoid in production)
    - importlib.import_module("name") — dynamic import by string at runtime
    - sys.path lists directories Python searches (script dir, PYTHONPATH, site-packages)

When to use
    - import module — when using many names from a module (math, os)
    - from module import name — when using one or two names frequently
    - Alias (as js) — when module name is long or conflicts with local names
    - Dynamic import — plugins, lazy loading, or runtime module selection

Common mistakes
    - Circular imports between modules — restructure or use lazy imports
    - from module import * — pollutes namespace, hides name origin
    - Running scripts inside packages without adjusting sys.path
    - Naming a file the same as a stdlib module (e.g., random.py) — shadows stdlib

PRACTICE
--------
Run: python3 core-python/modules/03-functions-and-modules/06_imports.py
"""

import json as js  # import json with shorter alias 'js'
import math  # import entire math module
import os  # import entire os module
import sys  # access sys.path for module search locations
from collections import Counter, defaultdict  # import specific names from collections
from datetime import datetime, timedelta  # import specific names from datetime
from importlib import import_module  # dynamic import by string name at runtime
from math import ceil, floor  # import only floor and ceil from math


def main() -> None:  # entry point that runs all import practice sections
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Standard library imports")  # section title
    print("=" * 50)  # close section header
    print(f"pi = {math.pi:.4f}")  # use math.pi constant
    print(f"sqrt(16) = {math.sqrt(16)}")  # call math.sqrt function
    print(f"Now: {datetime.now().strftime('%Y-%m-%d %H:%M')}")  # format current datetime

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Import specific names")  # section title
    print("=" * 50)  # close section header
    print(f"floor(3.7) = {floor(3.7)}, ceil(3.7) = {ceil(3.7)}")  # use imported functions directly

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Alias imports")  # section title
    print("=" * 50)  # close section header
    data = js.dumps({"key": "value"})  # serialize dict to JSON string using alias
    print(f"JSON: {data}")  # display JSON string

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Inspect modules")  # section title
    print("=" * 50)  # close section header
    print(f"math module location: {math.__file__}")  # show where the math module file is
    attrs = [x for x in dir(math) if not x.startswith("_")][:8]  # list public math attributes
    print(f"math attributes sample: {attrs}")  # show first 8 public names

    print("=" * 50)  # print section divider
    print("PRACTICE 5 — Dynamic import")  # section title
    print("=" * 50)  # close section header
    mod = import_module("math")  # load math module by string name at runtime
    print(f"Dynamic import pi: {mod.pi:.4f}")  # access pi from dynamically imported module

    print("=" * 50)  # print section divider
    print("PRACTICE 6 — sys.path")  # section title
    print("=" * 50)  # close section header
    print("First 3 sys.path entries:")  # label sys.path listing
    for p in sys.path[:3]:  # show first 3 directories Python searches for modules
        print(f"  {p}")  # print each search path entry

    print("=" * 50)  # print section divider
    print("PRACTICE 7 — Practical: Counter and defaultdict")  # section title
    print("=" * 50)  # close section header
    words = ["the", "cat", "sat", "on", "the", "mat"]  # sample word list
    freq = Counter(words)  # count word frequencies using imported Counter
    print(f"Word frequencies: {dict(freq)}")  # show frequency dict
    grouped = defaultdict(list)  # auto-create list values for missing keys
    for word in words:  # iterate words
        grouped[len(word)].append(word)  # group words by their length
    print(f"By length: {dict(grouped)}")  # show words grouped by character length

    print("=" * 50)  # print section divider
    print("PRACTICE 8 — Practical: timedelta date math")  # section title
    print("=" * 50)  # close section header
    today = datetime.now()  # get current datetime
    week_later = today + timedelta(days=7)  # add 7 days using imported timedelta
    print(f"Today:      {today.strftime('%Y-%m-%d')}")  # show today's date
    print(f"One week:   {week_later.strftime('%Y-%m-%d')}")  # show date one week later


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all import practice sections
