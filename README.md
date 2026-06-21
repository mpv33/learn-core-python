# Learn Core Python

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A structured path to learn **core Python** from basics to advanced — with runnable examples and interview prep in every module.

**Python 3.10+** required.

---

## Quick Start

```bash
cd python-learning
python3 --version
python3 00-setup/01_verify_installation.py
python3 01-fundamentals/01_hello_world.py
```

Work through folders **00 → 19** in order. Each folder has a `README.md` and numbered `.py` files you run directly.

---

## Repository Layout

```
python-learning/
├── README.md
├── LICENSE
├── .gitignore
├── interview/              # Master interview guide
├── 00-setup/
├── 01-fundamentals/
├── 02-control-flow/
├── ...
└── 19-best-practices/
```

**Per module:** `README.md` + `01_*.py`, `02_*.py`, … (no nested folders)

---

## Learning Path

### Phase 1 — Foundations
| Module | Folder | Topics |
|--------|--------|--------|
| 00 | [00-setup](00-setup/) | venv, pip, project layout |
| 01 | [01-fundamentals](01-fundamentals/) | types, operators, I/O, bytes |
| 02 | [02-control-flow](02-control-flow/) | if/else, loops, match |
| 03 | [03-data-structures](03-data-structures/) | list, tuple, set, dict, copy |
| 04 | [04-functions](04-functions/) | args, closures, recursion |

### Phase 2 — Core Skills
| Module | Folder | Topics |
|--------|--------|--------|
| 05 | [05-oop](05-oop/) | classes, inheritance, polymorphism |
| 06 | [06-modules](06-modules/) | imports, packages |
| 07 | [07-strings](07-strings/) | formatting, regex |
| 08 | [08-files](08-files/) | JSON, CSV, pathlib |
| 09 | [09-exceptions](09-exceptions/) | try/except, logging |

### Phase 3 — Intermediate
| Module | Folder | Topics |
|--------|--------|--------|
| 10 | [10-iterators](10-iterators/) | comprehensions, generators |
| 11 | [11-decorators](11-decorators/) | decorators, context managers |
| 12 | [12-types](12-types/) | type hints, mypy |
| 13 | [13-stdlib](13-stdlib/) | datetime, collections, os |
| 14 | [14-functional](14-functional/) | map, filter, reduce |

### Phase 4 — Advanced & Production
| Module | Folder | Topics |
|--------|--------|--------|
| 15 | [15-testing](15-testing/) | unittest, pytest, pdb |
| 16 | [16-concurrency](16-concurrency/) | threading, asyncio, GIL |
| 17 | [17-advanced](17-advanced/) | dataclasses, descriptors, metaclasses |
| 18 | [18-performance](18-performance/) | profiling, memory, optimization |
| 19 | [19-best-practices](19-best-practices/) | PEP 8, design patterns |

---

## Interview Prep

- Each module `README.md` includes **theory Q&A** and **coding questions**
- Full guide: [interview/README.md](interview/README.md)

---

## How to Study

1. Open the module folder (start at `00-setup`)
2. Read `README.md`
3. Run each `.py` file and experiment with the code
4. Review the interview section at the bottom of the README
5. Move to the next module

---

## Suggested Timeline

| Weeks | Modules |
|-------|---------|
| 1–2 | 00 – 04 |
| 3–4 | 05 – 09 |
| 5–6 | 10 – 14 |
| 7–8 | 15 – 19 + [interview guide](interview/) |

---

## Tools (Optional)

| Tool | Use |
|------|-----|
| `venv` | Isolate project dependencies |
| `pytest` | Run tests (`15-testing/`) |
| `mypy` | Type checking (`12-types/`) |
| `black` / `ruff` | Formatting and linting |

---

## License

[MIT](LICENSE) — free to use, share, and learn from.
