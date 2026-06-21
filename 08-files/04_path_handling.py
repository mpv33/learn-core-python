"""04 — Path Handling with pathlib"""

from pathlib import Path

# Current file's directory
here = Path(__file__).parent
print(f"This folder: {here}")

# Build paths (cross-platform)
data_dir = here / "data" / "logs"
config_file = here / "config" / "settings.ini"

print(f"Data dir: {data_dir}")
print(f"Config:   {config_file}")

# Path parts
print(f"\nParent: {here.parent.name}")
print(f"Name:   {here.name}")
print(f"Stem:   {Path('report.pdf').stem}")
print(f"Suffix: {Path('report.pdf').suffix}")

# Create directory
temp_dir = here / "temp_demo"
temp_dir.mkdir(exist_ok=True)
print(f"\nCreated: {temp_dir.exists()}")

# List files
print(f"Files in 01-fundamentals:")
basics = here.parent / "01-fundamentals"
for f in sorted(basics.glob("*.py")):
    print(f"  {f.name}")

# Read/write with Path
test_file = temp_dir / "test.txt"
test_file.write_text("Hello from pathlib!", encoding="utf-8")
print(f"\nRead back: {test_file.read_text(encoding='utf-8')}")

# Home directory
print(f"Home: {Path.home()}")

# Cleanup
test_file.unlink()
temp_dir.rmdir()
