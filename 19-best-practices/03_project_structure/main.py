"""Main entry point."""

from myapp import APP_NAME, VERSION, run
from myapp.utils import format_greeting

if __name__ == "__main__":
    run()
    print(format_greeting("Developer"))
    print(f"\nProject layout:")
    print("  myapp/")
    print("    __init__.py    # package init, exports")
    print("    utils.py       # helper functions")
    print("  main.py          # entry point")
    print("  tests/           # test files")
    print("  requirements.txt # dependencies")
    print("  README.md        # project docs")
