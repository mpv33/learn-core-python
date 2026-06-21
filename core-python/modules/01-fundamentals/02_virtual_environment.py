"""
02 — Virtual Environment: Isolated Project Dependencies

THEORY
------
What is it?
    A virtual environment (venv) is a self-contained directory with its own Python
    interpreter copy and site-packages. Each project gets its own dependency set
    without affecting system Python or other projects.

Why it matters
    Industry standard for every Python project. Prevents "dependency hell" when
    Project A needs Django 4 and Project B needs Django 3. CI/CD and teammates
    reproduce your environment from requirements.txt.

Key syntax/rules
    - python3 -m venv .venv          → create venv in .venv/ folder
    - source .venv/bin/activate      → activate on macOS/Linux
    - .venv\\Scripts\\activate        → activate on Windows
    - pip install <package>          → install into active venv only
    - pip freeze > requirements.txt  → snapshot installed versions
    - pip install -r requirements.txt → restore exact versions
    - deactivate                     → leave the venv

When to use
    - Starting any new Python project (always)
    - Before pip install in tutorials or production code
    - When collaborating — commit requirements.txt, gitignore .venv/

Common mistakes
    - Forgetting to activate venv before pip install (packages go to system Python)
    - Committing .venv/ to git instead of requirements.txt
    - Creating venv inside a folder that gets synced (Dropbox, iCloud) — slow and fragile

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/02_virtual_environment.py
"""

import os  # read environment variables like VIRTUAL_ENV
import sys  # inspect interpreter path and venv prefix


def main() -> None:  # print venv instructions and current environment state
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Create and activate a venv")  # section title
    print("=" * 50)  # close section header
    print("  python3 -m venv .venv")  # one-time venv creation command
    print("  source .venv/bin/activate          # macOS / Linux")  # activation for Unix
    print("  .venv\\Scripts\\activate            # Windows")  # activation for Windows

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Install and freeze dependencies")  # section title
    print("=" * 50)  # close section header
    print("  pip install pytest mypy black ruff")  # install common dev tools into venv
    print("  pip freeze > requirements.txt")  # save exact versions for teammates/CI
    print("  pip install -r requirements.txt")  # restore versions on another machine

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Deactivate and current state")  # section title
    print("=" * 50)  # close section header
    print("  deactivate")  # leave the virtual environment
    print()  # blank line before live state snapshot
    print("Current state:")  # label the live environment snapshot section
    print(f"  sys.executable = {sys.executable}")  # show which Python binary is active
    print(f"  VIRTUAL_ENV    = {os.environ.get('VIRTUAL_ENV', '(not set)')}")  # show venv path if activated
    in_venv = sys.prefix != sys.base_prefix  # True when a virtual environment is active
    print(f"  In venv        = {in_venv}")  # report whether venv isolation is active
    if in_venv:  # only meaningful when inside a venv
        print(f"  venv prefix    = {sys.prefix}")  # show isolated environment root path

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Practical: verify pip targets venv")  # section title
    print("=" * 50)  # close section header
    pip_cmd = "pip" if in_venv else "pip (may install globally — activate venv first!)"  # warn if not in venv
    print(f"  Recommended:   {pip_cmd}")  # remind user which pip context applies
    print(f"  site-packages: {sys.path[-1] if sys.path else 'unknown'}")  # show where packages install


if __name__ == "__main__":  # run main() only when this file is executed directly
    main()  # print instructions and current venv-related settings
