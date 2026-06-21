"""
Verify Python installation and environment readiness.
Run: python3 00-setup/01_verify_installation.py
"""

import sys
import platform

def main() -> None:
    version = sys.version_info
    print("=" * 50)
    print("PYTHON ENVIRONMENT CHECK")
    print("=" * 50)
    print(f"Version:     {version.major}.{version.minor}.{version.micro}")
    print(f"Executable:  {sys.executable}")
    print(f"Platform:    {platform.system()} {platform.machine()}")
    print(f"Python path: {sys.path[0]}")

    if version >= (3, 10):
        print("\n✓ Python 3.10+ — all modules supported")
    else:
        print("\n✗ Upgrade to Python 3.10+ for match, union types (X | Y)")

    in_venv = sys.prefix != sys.base_prefix
    print(f"In venv:     {'Yes' if in_venv else 'No (recommended: create one)'}")

if __name__ == "__main__":
    main()
