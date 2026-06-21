# Learn Core Python

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Structured Python learning — **core Python curriculum**, **FastAPI backend project**, and interview prep.

## Repository layout

```
python-learning/
├── core-python/
│   ├── modules/              # 01 → 07 learning curriculum
│   └── interview-prep/       # Master guide + 195+ Q&A
├── fastapi-with-python/
│   ├── LEARNING-GUIDE.md     # Step-by-step backend curriculum
│   ├── docs/                 # 12 concept guides
│   └── task-api/             # FastAPI project
├── README.md
└── LICENSE
```

## Quick start

From the repository root:

```bash
python3 core-python/modules/01-fundamentals/01_verify_installation.py
python3 core-python/modules/01-fundamentals/04_hello_world.py
```

## Learning path (recommended order)

### Phase 1 — Core Python (foundation)

Work through modules **01 → 07** in [core-python/modules/](core-python/modules/). Each lesson has **THEORY** (docstring) + **PRACTICE** (runnable code).

| # | Module | Topics |
|---|--------|--------|
| 01 | [fundamentals](core-python/modules/01-fundamentals/) | Setup, syntax, types, control flow |
| 02 | [data-structures](core-python/modules/02-data-structures/) | List, tuple, set, dict |
| 03 | [functions-and-modules](core-python/modules/03-functions-and-modules/) | Functions, imports, packages |
| 04 | [object-oriented-programming](core-python/modules/04-object-oriented-programming/) | Classes, inheritance, OOP |
| 05 | [data-handling](core-python/modules/05-data-handling/) | Strings, files, exceptions, logging |
| 06 | [intermediate-python](core-python/modules/06-intermediate-python/) | Iterators, decorators, types, stdlib |
| 07 | [advanced-and-production](core-python/modules/07-advanced-and-production/) | Testing, concurrency, performance |

**Interview prep:** [core-python/interview-prep/](core-python/interview-prep/) + per-module `INTERVIEW.md`

### Phase 2 — FastAPI backend (after modules 01, 03, 04, 05)

Full step-by-step guides: **[fastapi-with-python/LEARNING-GUIDE.md](fastapi-with-python/LEARNING-GUIDE.md)**

| Resource | Description |
|----------|-------------|
| [Learning Guide](fastapi-with-python/LEARNING-GUIDE.md) | 12-step curriculum (~10–12 hours) |
| [docs/](fastapi-with-python/docs/README.md) | Theory + practice per concept |
| [task-api/](fastapi-with-python/task-api/) | Hands-on project |

```bash
cd fastapi-with-python/task-api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && cp .env.example .env
make dev
```

Docs: http://127.0.0.1:8000/docs

---

## How core-python lessons work

Every `.py` lesson file follows the same structure:

1. **THEORY** — read the docstring at the top (What, Why, Key rules, When to use, Common mistakes)
2. **PRACTICE** — run the file; numbered sections show runnable examples with line-by-line comments

## License

[MIT](LICENSE)
