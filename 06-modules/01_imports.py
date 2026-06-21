"""01 — Import Styles"""

# Standard library imports
import math
import os
from datetime import datetime, timedelta
from collections import Counter, defaultdict

print(f"pi = {math.pi:.4f}")
print(f"sqrt(16) = {math.sqrt(16)}")
print(f"Now: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

# Import specific names
from math import floor, ceil
print(f"floor(3.7) = {floor(3.7)}, ceil(3.7) = {ceil(3.7)}")

# Alias
import json as js
data = js.dumps({"key": "value"})
print(f"JSON: {data}")

# Check what's available
print(f"\nmath module location: {math.__file__}")
print(f"math attributes sample: {[x for x in dir(math) if not x.startswith('_')][:8]}")

# Import from local package
from importlib import import_module

# Dynamic import
mod = import_module("math")
print(f"\nDynamic import pi: {mod.pi:.4f}")

# sys.path — where Python looks for modules
import sys
print(f"\nFirst 3 sys.path entries:")
for p in sys.path[:3]:
    print(f"  {p}")
