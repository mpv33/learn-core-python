"""
Industry-Standard Python Project Layout
========================================

my_project/
├── .venv/                  # Virtual env (gitignored)
├── src/
│   └── my_project/         # Source package
│       ├── __init__.py
│       ├── main.py
│       └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_utils.py
├── requirements.txt        # or pyproject.toml (modern)
├── .gitignore
└── README.md
"""

from pathlib import Path


def show_learning_repo_layout() -> None:
    root = Path(__file__).resolve().parents[2]
    print("This learning repository layout:\n")
    for item in sorted(root.iterdir()):
        if item.name.startswith("."):
            continue
        prefix = "📁" if item.is_dir() else "📄"
        print(f"  {prefix} {item.name}")
    print("\nEach module: README.md + numbered .py examples")


if __name__ == "__main__":
    show_learning_repo_layout()
