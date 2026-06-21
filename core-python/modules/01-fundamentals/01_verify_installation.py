"""
01 — Verify Installation: Environment Readiness Check

THEORY
------
What is it?
    Before writing Python code, confirm which interpreter is running, its version,
    and whether you are inside a virtual environment. sys and platform expose this
    information without external tools.

Why it matters
    Wrong Python version causes syntax errors (match, union types need 3.10+).
    Running globally instead of in a venv leads to dependency conflicts.
    Interviewers ask how you debug "works on my machine" issues — start here.

Key syntax/rules
    - sys.version_info → (major, minor, micro, ...) tuple for version checks
    - sys.executable → path to the python binary actually running this script
    - sys.prefix != sys.base_prefix → True when inside an activated venv
    - sys.path[0] → first module search path (often the script's directory)
    - platform.system() / platform.machine() → OS name and CPU architecture

When to use
    - First step on a new machine or after installing Python
    - When imports fail mysteriously (wrong interpreter selected in IDE)
    - Before starting a course or project to confirm 3.10+ and venv status

Common mistakes
    - Assuming `python` and `python3` point to the same version
    - Checking version with `python --version` but running code with a different binary
    - Skipping venv setup and polluting the system Python with pip packages

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/01_verify_installation.py
"""

import sys  # access Python version, executable path, and sys.path
import platform  # read OS name and machine architecture


def main() -> None:  # entry point that prints environment diagnostics
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Python version and executable")  # section title
    print("=" * 50)  # close section header
    version = sys.version_info  # tuple of (major, minor, micro, ...) for running Python
    print(f"Version:     {version.major}.{version.minor}.{version.micro}")  # show installed Python version
    print(f"Executable:  {sys.executable}")  # show which python binary is running this script
    print(f"Full info:   {sys.version}")  # show detailed version string including build info

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Platform and module search path")  # section title
    print("=" * 50)  # close section header
    print(f"Platform:    {platform.system()} {platform.machine()}")  # show OS and CPU architecture
    print(f"Python path: {sys.path[0]}")  # show first search path entry (script's directory)
    print(f"Path entries: {len(sys.path)} directories in sys.path")  # count total search locations

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Version compatibility check")  # section title
    print("=" * 50)  # close section header
    if version >= (3, 10):  # check whether modern features like match are supported
        print("✓ Python 3.10+ — match/case, union types (X | Y) supported")  # confirm version meets requirements
    else:
        print("✗ Upgrade to Python 3.10+ for match, union types (X | Y)")  # warn when version is too old
    if version >= (3, 12):  # check for newer f-string and typing features
        print("✓ Python 3.12+ — latest syntax and performance improvements available")  # bonus version note

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Virtual environment detection")  # section title
    print("=" * 50)  # close section header
    in_venv = sys.prefix != sys.base_prefix  # True when running inside an activated virtual environment
    print(f"In venv:     {'Yes' if in_venv else 'No (recommended: create one)'}")  # report venv status to user
    print(f"sys.prefix:  {sys.prefix}")  # show active environment prefix path
    print(f"base_prefix: {sys.base_prefix}")  # show system Python prefix for comparison


if __name__ == "__main__":  # run main() only when file is executed directly, not imported
    main()  # start the environment check
