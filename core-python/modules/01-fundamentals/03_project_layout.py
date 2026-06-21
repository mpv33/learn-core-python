"""
03 — Project Layout: Industry-Standard Directory Structure

THEORY
------
What is it?
    A consistent folder layout separates source code, tests, config, and docs.
    The src/ layout keeps packages importable and mirrors how real teams organize
    Python repos. pathlib.Path provides a clean API for navigating this structure.

Why it matters
    Interviewers and code reviewers expect recognizable structure. Tools like pytest,
    mypy, and packaging (pyproject.toml) assume conventional layouts. A messy repo
    signals inexperience.

Key syntax/rules
    - src/<package>/     → installable source (avoids accidental imports from cwd)
    - tests/             → mirror package structure; test_*.py naming for pytest
    - requirements.txt   → pinned deps (or pyproject.toml for modern projects)
    - .venv/             → local venv, always in .gitignore
    - __init__.py        → marks a directory as a Python package
    - Path(__file__).resolve().parents[N] → walk up from current file

When to use
    - Starting any project beyond a single script
    - Contributing to open source (read their layout first)
    - Scaling from notebooks/scripts to maintainable applications

Common mistakes
    - Putting test files inside src/ instead of tests/
    - No __init__.py (or missing pyproject.toml package config in modern setups)
    - Committing .venv/, __pycache__/, or .env files to version control

PRACTICE
--------
Run: python3 core-python/modules/01-fundamentals/03_project_layout.py
"""

from pathlib import Path  # object-oriented API for filesystem paths


def main() -> None:  # entry point that demonstrates project layout concepts
    print("=" * 50)  # print section divider
    print("PRACTICE 1 — Ideal project structure")  # section title
    print("=" * 50)  # close section header
    ideal = [  # list of lines describing a standard Python project tree
        "my_project/",
        "├── .venv/                  # Virtual env (gitignored)",
        "├── src/",
        "│   └── my_project/         # Source package",
        "│       ├── __init__.py",
        "│       ├── main.py",
        "│       └── utils.py",
        "├── tests/",
        "│   ├── __init__.py",
        "│   └── test_utils.py",
        "├── requirements.txt        # or pyproject.toml (modern)",
        "├── .gitignore",
        "└── README.md",
    ]
    for line in ideal:  # print each line of the ideal layout diagram
        print(line)  # display one tree entry

    print("=" * 50)  # print section divider
    print("PRACTICE 2 — This learning repository layout")  # section title
    print("=" * 50)  # close section header
    root = Path(__file__).resolve().parents[3]  # climb to repo root (modules/01-fundamentals → repo)
    print(f"Repo root: {root}\n")  # show absolute path to repository root
    for item in sorted(root.iterdir()):  # walk each entry in root directory alphabetically
        if item.name.startswith("."):  # skip hidden files/folders like .git and .venv
            continue  # move to next item without printing hidden entries
        prefix = "📁" if item.is_dir() else "📄"  # choose folder or file icon for display
        print(f"  {prefix} {item.name}")  # print one repo entry with its icon
    print("\nEach module lives under core-python/modules/ with README + numbered .py examples")  # explain layout

    print("=" * 50)  # print section divider
    print("PRACTICE 3 — pathlib navigation from this file")  # section title
    print("=" * 50)  # close section header
    here = Path(__file__).resolve()  # absolute path to this script file
    print(f"This file:     {here.name}")  # show filename only
    print(f"Parent dir:    {here.parent.name}")  # show immediate parent folder name
    print(f"Module path:   {here.parent.parent.name}/{here.parent.name}")  # show modules/01-fundamentals

    print("=" * 50)  # print section divider
    print("PRACTICE 4 — Practical: find sibling lesson files")  # section title
    print("=" * 50)  # close section header
    lessons = sorted(here.parent.glob("[0-9]*.py"))  # list numbered .py files in same folder
    print(f"Lessons in {here.parent.name}/: {len(lessons)} files")  # count lesson files
    for lesson in lessons[:5]:  # show first five as a sample
        print(f"  📄 {lesson.name}")  # print lesson filename
    if len(lessons) > 5:  # indicate more files exist beyond the sample
        print(f"  ... and {len(lessons) - 5} more")  # summarize remaining lesson count


if __name__ == "__main__":  # run layout demo only when script is executed directly
    main()  # display project structure examples
