"""Main entry point."""

from myapp import APP_NAME, VERSION, run  # import package constants and run function
from myapp.utils import format_greeting  # import helper from utils submodule

if __name__ == "__main__":  # execute only when run as script
    run()  # start application via package entry function
    print(format_greeting("Developer"))  # print welcome message for developer
    print(f"\nProject layout:")  # document recommended project structure
    print("  myapp/")
    print("    __init__.py    # package init, exports")
    print("    utils.py       # helper functions")
    print("  main.py          # entry point")
    print("  tests/           # test files")
    print("  requirements.txt # dependencies")
    print("  README.md        # project docs")
