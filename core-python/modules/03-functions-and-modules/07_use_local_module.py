"""
07 — Using a Local Module

THEORY
------
What is it?
    A local module is a .py file or package in your project that you import
    like any other module. Python finds it by searching sys.path — by default
    the script's directory is included, but packages may need explicit path setup.

Why it matters
    Organizing code into modules and packages is how real projects scale.
    Understanding sys.path manipulation and package imports lets you structure
    reusable code and avoid "ModuleNotFoundError" during development.

Key syntax/rules
    - sys.path.insert(0, path) adds a directory to the front of the search path
    - from package import name imports from package/__init__.py or re-exports
    - from package import submodule imports a submodule directly
    - Path(__file__).parent gives the directory containing the current script
    - Packages need __init__.py (or be namespace packages in Python 3.3+)
    - Prefer relative imports within a package; absolute imports from outside

When to use
    - Splitting a project into reusable modules (utils, models, services)
    - Demo packages for learning import mechanics
    - Adding project root to sys.path when running scripts from subdirectories
    - Importing shared helpers across multiple scripts in the same folder

Common mistakes
    - Forgetting to add parent directory to sys.path before importing local packages
    - Naming script the same as module you try to import (shadowing)
    - Using relative imports in scripts run directly (ValueError)
    - Circular imports between local modules — restructure dependencies

PRACTICE
--------
Run: python3 core-python/modules/03-functions-and-modules/07_use_local_module.py
"""

import sys  # modify module search path for local package import
from pathlib import Path  # clean file path handling for cross-platform paths


def main() -> None:  # entry point that runs all local module practice sections
    sys.path.insert(0, str(Path(__file__).parent))  # add this file's directory to sys.path front

    from demo_package import APP_VERSION, add, greet  # import names from local demo_package
    from demo_package import mymodule  # import submodule directly for qualified access

    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Import from local package")  # section title
    print("=" * 50)  # close section header
    print(greet("Learner"))  # call greet function imported from package
    print(f"2 + 3 = {add(2, 3)}")  # call add function imported from package
    print(f"Version: {APP_VERSION}")  # access package version constant

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — Direct submodule import")  # section title
    print("=" * 50)  # close section header
    print(f"Direct: {mymodule.greet('Direct import')}")  # call greet through submodule reference

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — Inspect imported module")  # section title
    print("=" * 50)  # close section header
    print(f"Module file: {mymodule.__file__}")  # show path to the imported module file
    print(f"Module name: {mymodule.__name__}")  # show fully qualified module name

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Practical: reuse package utilities")  # section title
    print("=" * 50)  # close section header
    numbers = [10, 20, 30]  # sample numbers to sum
    total = add(numbers[0], add(numbers[1], numbers[2]))  # chain add calls from imported module
    print(f"Sum of {numbers} = {total}")  # show result of chained add calls
    print(f"Greeting: {greet('Python Learner')}")  # personalized greeting from package


if __name__ == "__main__":  # run main() only when executed directly, not imported
    main()  # start all local module practice sections
