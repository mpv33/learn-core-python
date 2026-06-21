"""
02 — Virtual Environments
=========================

Virtual environments isolate project dependencies.

Setup (run in terminal):
  python -m venv venv
  source venv/bin/activate        # macOS/Linux
  venv\\Scripts\\activate         # Windows
  pip install requests pandas
  pip freeze > requirements.txt
  pip install -r requirements.txt
  deactivate
"""

import sys
import os

print("Python Environment Info:")
print(f"  Executable: {sys.executable}")
print(f"  Version:    {sys.version.split()[0]}")
print(f"  In venv:    {hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)}")

if "VIRTUAL_ENV" in os.environ:
    print(f"  VENV path:  {os.environ['VIRTUAL_ENV']}")
else:
    print("  VENV path:  (not in a virtual environment)")

print("\nRecommended workflow:")
print("  1. Create venv per project")
print("  2. Pin dependencies in requirements.txt")
print("  3. Never install globally unless necessary")
print("  4. Use pyproject.toml for modern projects")

# Check installed packages count
try:
    import pkg_resources
    dists = list(pkg_resources.working_set)
    print(f"\nInstalled packages: {len(dists)}")
except ImportError:
    print("\nInstall setuptools to list packages.")
