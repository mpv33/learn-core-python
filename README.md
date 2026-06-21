# GenAI Full-Stack Developer Track

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Next.js](https://img.shields.io/badge/Next.js-15-black.svg)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A structured learning path from **Python fundamentals** to **production GenAI applications** — covering REST APIs, RAG, and multi-agent systems with **Next.js + FastAPI**.

Every phase includes theory, hands-on practice, and a runnable project. Complete phases in order; Phases 1–2 are required before the GenAI capstone projects.

**Stack:** Python · FastAPI · Next.js · OpenAI / Ollama · **Estimated time:** ~75–110 hours

---

## What you'll learn

| Outcome | Covered in |
|---------|------------|
| Python syntax, OOP, files, testing | Phase 1 |
| Production REST APIs — auth, DB, Docker | Phase 2 |
| RAG — chunking, embeddings, retrieval, citations | Phase 3 |
| Multi-agent orchestration — triage, tools, escalation | Phase 4 |
| Full-stack GenAI apps (Next.js UI + FastAPI backend) | Phases 3–4 |

---

## Learning path

| Phase | Folder | Project / content | Time |
|-------|--------|-------------------|------|
| **1** | [core-python/](core-python/) | 7-module curriculum + interview prep | ~40–60 hrs |
| **2** | [backend-with-fastapi/](backend-with-fastapi/) | Task Management API (auth, RBAC, DB) | ~10–12 hrs |
| **3** | [fullstack-genai/rag-assistant/](fullstack-genai/rag-assistant/) | RAG knowledge assistant | ~15–25 hrs |
| **4** | [fullstack-genai/support-agent/](fullstack-genai/support-agent/) | Multi-agent customer support | ~10–15 hrs |

```
core-python  →  backend-with-fastapi  →  rag-assistant  →  support-agent
  (Python)         (FastAPI API)          (RAG + UI)         (Agents + UI)
```

---

## Repository structure

```
python-learning/
├── core-python/
│   ├── modules/                 # 01 → 07 (THEORY + PRACTICE in each .py file)
│   └── interview-prep/          # Master guide + 195+ Q&A
├── backend-with-fastapi/
│   ├── LEARNING-GUIDE.md        # 12-step curriculum
│   ├── docs/                    # REST, auth, DB, testing, Docker
│   └── task-api/                # FastAPI project
└── fullstack-genai/
    ├── rag-assistant/           # Phase 3 — LEARNING-GUIDE + docs + app
    └── support-agent/           # Phase 4 — LEARNING-GUIDE + docs + app
```

---

## Quick start

Verify Python and run your first lesson:

```bash
python3 core-python/modules/01-fundamentals/01_verify_installation.py
python3 core-python/modules/01-fundamentals/04_hello_world.py
```

Each lesson file: read the **THEORY** docstring at the top, then run the file for **PRACTICE** sections.

---

## Phase 1 — Core Python

**Folder:** [core-python/](core-python/) · **Guide:** [README](core-python/README.md)

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

**Before Phase 2:** complete modules 01, 03, 04, 05.

---

## Phase 2 — Backend with FastAPI

**Folder:** [backend-with-fastapi/](backend-with-fastapi/) · **Guide:** [LEARNING-GUIDE.md](backend-with-fastapi/LEARNING-GUIDE.md)

Production-style **Task Management REST API** — JWT auth, RBAC, SQLAlchemy, Alembic, rate limiting, pytest, Docker. Same patterns used in the GenAI projects.

| Resource | Description |
|----------|-------------|
| [Learning Guide](backend-with-fastapi/LEARNING-GUIDE.md) | 12-step curriculum |
| [docs/](backend-with-fastapi/docs/README.md) | Concept guides (REST → deployment) |
| [task-api/](backend-with-fastapi/task-api/) | Project reference |

```bash
cd backend-with-fastapi/task-api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && cp .env.example .env
make dev
```

**API docs:** http://127.0.0.1:8000/docs

| Email | Password | Role |
|-------|----------|------|
| admin@example.com | admin123 | admin |
| user@example.com | user123 | user |

---

## Phase 3 — RAG Assistant

**Folder:** [fullstack-genai/rag-assistant/](fullstack-genai/rag-assistant/) · **Guide:** [LEARNING-GUIDE.md](fullstack-genai/rag-assistant/LEARNING-GUIDE.md)

Upload documents → chunk & embed → vector search → chat with **grounded answers and source citations**. Includes RAG vs plain LLM compare mode.

| Resource | Description |
|----------|-------------|
| [Learning Guide](fullstack-genai/rag-assistant/LEARNING-GUIDE.md) | RAG theory + build steps |
| [docs/](fullstack-genai/rag-assistant/docs/01-rag-concepts.md) | Chunking, embeddings, LLM selection |
| [README](fullstack-genai/rag-assistant/) | Features, API, structure |

```bash
cd fullstack-genai/rag-assistant
cp backend/.env.example backend/.env   # add OPENAI_API_KEY
make install && make dev
```

| Chat UI | API |
|---------|-----|
| http://localhost:3000 | http://127.0.0.1:8000/docs |

**Prerequisites:** Phase 2 + OpenAI API key (or Ollama).

---

## Phase 4 — Support Agent

**Folder:** [fullstack-genai/support-agent/](fullstack-genai/support-agent/) · **Guide:** [LEARNING-GUIDE.md](fullstack-genai/support-agent/LEARNING-GUIDE.md)

**Multi-agent customer support** — triage → knowledge / orders / escalation agents → supervisor. UI shows full agent trace on every reply.

| Agent | Role |
|-------|------|
| Triage | Classify intent (returns, billing, order status, …) |
| Knowledge | Answer from support KB (RAG-lite) |
| Orders | Look up mock order data |
| Escalation | Create human handoff tickets |
| Supervisor | Route + polish final response |

```bash
cd fullstack-genai/support-agent
cp backend/.env.example backend/.env   # add OPENAI_API_KEY
make install && make dev
```

| Support UI | API |
|------------|-----|
| http://localhost:3001 | http://127.0.0.1:8001/docs |

**Prerequisites:** Phase 3. Runs on separate ports so it can run alongside rag-assistant.

---

## Skills matrix

| Skill | P1 | P2 | P3 | P4 |
|-------|:--:|:--:|:--:|:--:|
| Python & OOP | ✓ | | | |
| REST APIs & HTTP | | ✓ | ✓ | ✓ |
| Auth, DB, pytest, Docker | | ✓ | | |
| Embeddings & vector retrieval | | | ✓ | ✓ |
| LLM prompting & grounding | | | ✓ | ✓ |
| RAG pipelines | | | ✓ | ✓ |
| Multi-agent orchestration | | | | ✓ |
| Next.js + FastAPI full stack | | | ✓ | ✓ |

---

## License

[MIT](LICENSE)
