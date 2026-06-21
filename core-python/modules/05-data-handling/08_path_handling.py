"""
08 — Path Handling with pathlib
================================

THEORY
------
What:
  `pathlib.Path` provides an object-oriented interface for filesystem paths.
  It replaces string concatenation with `/` operator joining and rich methods.

Why:
  Cross-platform path handling without manual slash management. Cleaner than
  `os.path.join()` for modern Python code.

Key rules:
  - `Path(__file__).parent` — directory containing the current script.
  - Join with `/`: `base / "data" / "file.txt"` works on Windows and Unix.
  - `.name`, `.stem`, `.suffix`, `.parent` decompose path components.
  - `.exists()`, `.is_file()`, `.is_dir()` check filesystem state.
  - `.mkdir(exist_ok=True)` creates directories; `.glob("*.py")` finds files.
  - `.read_text()` / `.write_text()` for quick file I/O.

When to use:
  - Building file paths relative to a script or project root.
  - Listing, creating, or cleaning up directories in scripts.
  - Any file I/O where you want readable, portable path code.

Common mistakes:
  - Mixing `str` paths and `Path` objects — convert with `str(p)` when needed.
  - Using `Path("/") / user_input` without validation — path traversal risk.
  - Calling `.rmdir()` on non-empty directories — use `shutil.rmtree()` instead.

PRACTICE
--------
Run: python3 core-python/modules/05-data-handling/08_path_handling.py
"""

from pathlib import Path  # high-level path objects with rich methods


def main() -> None:
    here = Path(__file__).parent  # directory containing this script

    print("=" * 50)  # visual section divider
    print("PRACTICE 1 — Build and inspect paths")  # label first block
    print("=" * 50)  # close header

    print(f"This folder: {here}")  # show absolute path to current module folder
    data_dir = here / "data" / "logs"  # join path segments with / operator
    config_file = here / "config" / "settings.ini"  # another joined path example
    print(f"Data dir: {data_dir}")  # display constructed data directory path
    print(f"Config:   {config_file}")  # display constructed config file path
    print(f"Parent: {here.parent.name}")  # name of the parent directory
    print(f"Name:   {here.name}")  # final component of this path
    print(f"Stem:   {Path('report.pdf').stem}")  # filename without extension
    print(f"Suffix: {Path('report.pdf').suffix}")  # file extension including dot

    print("\n" + "=" * 50)  # divider before directory demo
    print("PRACTICE 2 — Create directory and list files")  # label second block
    print("=" * 50)  # close header

    temp_dir = here / "temp_demo"  # temporary folder path for demo I/O
    temp_dir.mkdir(exist_ok=True)  # create directory; no error if already exists
    print(f"Created: {temp_dir.exists()}")  # True after mkdir succeeds
    print("Files in 01-fundamentals:")  # label directory listing demo
    basics = here.parent / "01-fundamentals"  # sibling fundamentals folder
    py_files = sorted(basics.glob("*.py"))  # glob returns matching paths
    for f in py_files[:5]:  # show first five files only
        print(f"  {f.name}")  # print each Python filename
    print(f"  ... ({len(py_files)} total)")  # report total count

    print("\n" + "=" * 50)  # divider before read/write demo
    print("PRACTICE 3 — Read/write with Path shortcuts")  # label third block
    print("=" * 50)  # close header

    test_file = temp_dir / "test.txt"  # file path inside temp directory
    test_file.write_text("Hello from pathlib!", encoding="utf-8")  # write string in one call
    print(f"Read back: {test_file.read_text(encoding='utf-8')}")  # read entire file as string
    print(f"File size: {test_file.stat().st_size} bytes")  # metadata from stat()

    print("\n" + "=" * 50)  # divider before home/resolution demo
    print("PRACTICE 4 — Home directory and resolve")  # label fourth block
    print("=" * 50)  # close header

    print(f"Home: {Path.home()}")  # user's home directory path
    print(f"Resolved: {here.resolve()}")  # absolute path with symlinks resolved
    test_file.unlink()  # delete the temporary text file
    temp_dir.rmdir()  # remove empty temp directory
    print("Temp demo cleaned up.")  # confirm cleanup


if __name__ == "__main__":
    main()  # run all practice sections when executed directly
