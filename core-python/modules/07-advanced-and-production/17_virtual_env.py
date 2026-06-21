"""
17 — Virtual Environments

THEORY
------
What: A virtual environment (venv) is an isolated Python installation with its own
      site-packages, separate from the system Python.
Why:  Avoid dependency conflicts between projects; reproduce environments via requirements.txt.
Key rules:
  - Create: python -m venv venv; Activate: source venv/bin/activate (macOS/Linux).
  - pip freeze > requirements.txt pins versions; pip install -r requirements.txt restores.
  - sys.prefix != sys.base_prefix indicates an active venv.
When to use: Every Python project; CI/CD pipelines; sharing reproducible dev environments.
Common mistakes: Installing packages globally; not pinning versions; committing venv/
                 folder to git; forgetting to activate before pip install.

PRACTICE
--------
Run: python3 core-python/modules/07-advanced-and-production/17_virtual_env.py
"""

import sys  # inspect active Python interpreter
import os  # read environment variables


def main() -> None:  # entry point for all practice demos
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Python environment info")  # section header
    print("=" * 50)  # close header divider
    print(f"  Executable: {sys.executable}")  # path to current Python binary
    print(f"  Version:    {sys.version.split()[0]}")  # major.minor.patch version string
    in_venv = hasattr(sys, "real_prefix") or (hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix)  # venv check
    print(f"  In venv:    {in_venv}")  # True when venv active

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 2 — VIRTUAL_ENV variable")  # section header
    print("=" * 50)  # close header divider
    if "VIRTUAL_ENV" in os.environ:  # check standard venv environment variable
        print(f"  VENV path:  {os.environ['VIRTUAL_ENV']}")  # show active virtualenv directory
    else:  # no venv detected
        print("  VENV path:  (not in a virtual environment)")  # report no active venv

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 3 — Recommended workflow")  # section header
    print("=" * 50)  # close header divider
    print("  1. Create venv per project")  # step 1
    print("  2. Pin dependencies in requirements.txt")  # step 2
    print("  3. Never install globally unless necessary")  # step 3
    print("  4. Use pyproject.toml for modern projects")  # step 4

    print("\n" + "=" * 50)  # blank line plus divider
    print("PRACTICE 4 — Installed packages count")  # section header
    print("=" * 50)  # close header divider
    try:  # attempt to enumerate installed distributions
        import pkg_resources  # legacy package metadata API
        dists = list(pkg_resources.working_set)  # collect installed distributions
        print(f"  Installed packages: {len(dists)}")  # report package count
    except ImportError:  # setuptools/pkg_resources unavailable
        print("  Install setuptools to list packages.")  # fallback message


if __name__ == "__main__":  # run main() only when executed directly
    main()  # start all practice sections
