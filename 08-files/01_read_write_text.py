"""01 — Read and Write Text Files"""

from pathlib import Path

# Use a temp file in this folder for demo
demo_file = Path(__file__).parent / "sample.txt"

# Write
with open(demo_file, "w", encoding="utf-8") as f:
    f.write("Line 1: Hello\n")
    f.write("Line 2: Python\n")
    f.writelines(["Line 3: Files\n", "Line 4: Done\n"])
print(f"Written to {demo_file.name}")

# Read entire file
with open(demo_file, "r", encoding="utf-8") as f:
    content = f.read()
print(f"\nFull content:\n{content}")

# Read line by line (memory efficient)
print("Line by line:")
with open(demo_file, "r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, 1):
        print(f"  {line_num}: {line.rstrip()}")

# Read all lines as list
with open(demo_file, "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"Total lines: {len(lines)}")

# Append
with open(demo_file, "a", encoding="utf-8") as f:
    f.write("Line 5: Appended\n")

# Check file exists
print(f"\nExists: {demo_file.exists()}")
print(f"Size: {demo_file.stat().st_size} bytes")

# Cleanup
demo_file.unlink()
print("Demo file cleaned up.")
