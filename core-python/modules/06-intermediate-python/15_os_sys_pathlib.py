"""
15 — os, sys, pathlib

THEORY
------
What: os and sys expose OS and interpreter interfaces; pathlib provides object-oriented
      filesystem paths (preferred over os.path for new code).
Why:  Scripts need env vars, process info, directory traversal, and portable path handling.
Key rules:
  - pathlib.Path: use / operator for joining; .glob(), .iterdir(), .read_text().
  - os.environ: read/write environment variables (strings only).
  - sys.argv, sys.executable, sys.path: runtime configuration and CLI args.
When to use: File discovery, env-based config, cross-platform paths, process diagnostics.
Common mistakes: Hardcoding path separators (use Path); mutating sys.path carelessly;
                 string paths when Path objects are clearer and safer.

PRACTICE
--------
Run: python3 core-python/modules/06-intermediate-python/15_os_sys_pathlib.py
"""

import os  # operating system interface (env vars, paths, process info)
import sys  # interpreter and runtime configuration
from pathlib import Path  # object-oriented filesystem paths


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — os environment and system")  # section header
    print("=" * 50)  # close header divider
    print(f"OS name: {os.name}")  # show OS family (posix, nt, etc.)
    print(f"Current dir: {os.getcwd()}")  # print working directory
    print(f"HOME: {os.environ.get('HOME', 'N/A')}")  # read HOME env var with fallback
    print(f"CPU count: {os.cpu_count()}")  # report available CPU cores

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — pathlib basics")  # section header
    print("=" * 50)  # close header divider
    script = Path(__file__)  # Path object for this script file
    print(f"Script: {script.name}")  # filename without directory
    print(f"Exists: {script.exists()}")  # check whether path exists on disk
    print(f"Absolute: {script.resolve()}")  # resolve to absolute canonical path

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — List directory")  # section header
    print("=" * 50)  # close header divider
    parent = script.parent.parent  # core-python/modules — sibling module folders
    folders = [d.name for d in parent.iterdir() if d.is_dir()]  # collect subdirectory names
    print(f"Learning folders ({len(folders)}): {sorted(folders)[:5]}...")  # show first five sorted

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — sys interpreter info")  # section header
    print("=" * 50)  # close header divider
    print(f"Python version: {sys.version.split()[0]}")  # print major.minor.patch version
    print(f"Platform: {sys.platform}")  # show platform identifier string
    print(f"Args: {sys.argv[:3]}")  # show first three command-line arguments

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 5 — Set environment variable")  # section header
    print("=" * 50)  # close header divider
    os.environ["MY_APP_MODE"] = "development"  # set a custom environment variable
    print(f"MY_APP_MODE: {os.environ.get('MY_APP_MODE')}")  # read back the variable value

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 6 — Walk directory tree with glob")  # section header
    print("=" * 50)  # close header divider
    basics = parent / "01-fundamentals"  # path to fundamentals module folder
    for f in basics.glob("*.py"):  # iterate Python files in that folder
        print(f"  {f.name} ({f.stat().st_size} bytes)")  # print filename and size in bytes

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 7 — Process ID")  # section header
    print("=" * 50)  # close header divider
    print(f"Process ID: {os.getpid()}")  # show current process identifier


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
