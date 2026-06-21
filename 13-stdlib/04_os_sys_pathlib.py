"""04 — os, sys, pathlib"""

import os
import sys
from pathlib import Path

# os — environment and system
print(f"OS name: {os.name}")
print(f"Current dir: {os.getcwd()}")
print(f"HOME: {os.environ.get('HOME', 'N/A')}")
print(f"CPU count: {os.cpu_count()}")

# os.path (legacy) vs pathlib (modern)
script = Path(__file__)
print(f"\nScript: {script.name}")
print(f"Exists: {script.exists()}")
print(f"Absolute: {script.resolve()}")

# List directory
parent = script.parent.parent
folders = [d.name for d in parent.iterdir() if d.is_dir()]
print(f"\nLearning folders ({len(folders)}): {sorted(folders)[:5]}...")

# sys — interpreter info
print(f"\nPython version: {sys.version.split()[0]}")
print(f"Platform: {sys.platform}")
print(f"Args: {sys.argv[:3]}")

# Environment variables
os.environ["MY_APP_MODE"] = "development"
print(f"MY_APP_MODE: {os.environ.get('MY_APP_MODE')}")

# Walk directory tree
print(f"\n.py files in 01-fundamentals:")
basics = parent / "01-fundamentals"
for f in basics.glob("*.py"):
    print(f"  {f.name} ({f.stat().st_size} bytes)")

# Process ID
print(f"\nProcess ID: {os.getpid()}")
