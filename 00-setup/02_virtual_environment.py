"""
Virtual Environment — Industry Standard Workflow
===================================================

Run this file for instructions. Execute these commands in terminal:

  # Create venv (once per project)
  python3 -m venv .venv

  # Activate
  source .venv/bin/activate          # macOS / Linux
  .venv\\Scripts\\activate            # Windows

  # Install packages
  pip install pytest mypy black ruff

  # Freeze dependencies
  pip freeze > requirements.txt

  # Install from requirements (teammate / CI)
  pip install -r requirements.txt

  # Deactivate
  deactivate
"""

import os
import sys


def main() -> None:
    print(__doc__)
    print("Current state:")
    print(f"  sys.executable = {sys.executable}")
    print(f"  VIRTUAL_ENV    = {os.environ.get('VIRTUAL_ENV', '(not set)')}")
    print(f"  In venv        = {sys.prefix != sys.base_prefix}")


if __name__ == "__main__":
    main()
