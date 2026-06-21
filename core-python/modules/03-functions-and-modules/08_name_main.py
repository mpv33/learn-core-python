"""
08 — if __name__ == '__main__'

THEORY
------
What is it?
    Every Python module has a __name__ attribute. When a file is run directly,
    __name__ is set to "__main__". When imported, __name__ is the module's
    full dotted path (e.g., "my_module"). The guard if __name__ == "__main__"
    runs code only in direct execution mode.

Why it matters
    This pattern separates reusable library code from script entry points.
    It lets the same file be imported safely (definitions only) or run as a
    CLI tool / demo (main block executes). It is standard in every Python project.

Key syntax/rules
    - def main(): holds the script's entry logic
    - if __name__ == "__main__": main() runs only when executed directly
    - When imported: __name__ == module name — main block is skipped
    - When run directly: __name__ == "__main__" — main block runs
    - Functions and classes at module level are always defined on import
    - Use def main() -> None: with type hint for clarity and tooling support

When to use
    - Any .py file that can both be imported and run as a script
    - CLI tools, demos, and test harnesses at the bottom of modules
    - Keeping side effects (prints, file writes) out of import-time execution
    - Organizing "what runs on startup" in one clear place

Common mistakes
    - Putting all code at module level without the guard — runs on import too
    - Using if __name__ == "__main__" without a main() function — works but less clean
    - Assuming __name__ is always "__main__" inside the guarded block during imports
    - Heavy computation at import time slowing down every import of the module

PRACTICE
--------
Run: python3 core-python/modules/03-functions-and-modules/08_name_main.py
"""


def helper() -> str:  # helper function available when imported or run directly
    return "helper result"  # return a simple string result


def main() -> None:  # main entry point function for this script
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Running as main script")  # section title
    print("=" * 50)  # close section header
    print("Running as main script.")  # confirm direct execution mode
    print("Useful for: CLI tools, tests, demos.")  # explain common use cases

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Module name inspection")  # section title
    print("=" * 50)  # close section header
    print(f"Module name: {__name__}")  # show __name__ value when run directly

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Call helper from main")  # section title
    print("=" * 50)  # close section header
    print(f"Helper says: {helper()}")  # demonstrate calling a module-level function

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Practical: argparse-style entry")  # section title
    print("=" * 50)  # close section header
    import sys  # access command-line arguments
    args = sys.argv[1:]  # collect arguments after script name
    if args:  # if user passed any arguments
        print(f"Arguments received: {args}")  # show parsed arguments
    else:  # no arguments provided
        print("No arguments — run with: python3 .../08_name_main.py hello world")  # usage hint


if __name__ == "__main__":  # this block runs ONLY when file is executed directly
    main()  # call main when script is run directly, not when imported

# When imported: __name__ == "08_name_main"
# When run directly: __name__ == "__main__"
