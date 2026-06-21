# Full-Stack GenAI

**Phases 3 & 4** of the [GenAI Full-Stack Developer Track](../README.md) — two industry-grade capstone projects.

**Stack:** Next.js 15 + FastAPI + OpenAI (or Ollama)

Each project has its own **LEARNING-GUIDE**, **docs**, and runnable app.

---

## Capstone projects

| Project | What you build | Guide | Ports |
|---------|----------------|-------|-------|
| [rag-assistant](rag-assistant/) | RAG knowledge assistant — upload docs, chat with **citations** | [LEARNING-GUIDE.md](rag-assistant/LEARNING-GUIDE.md) | :3000 / :8000 |
| [support-agent](support-agent/) | Multi-agent support desk — triage, tools, escalation | [LEARNING-GUIDE.md](support-agent/LEARNING-GUIDE.md) | :3001 / :8001 |

**Order:** rag-assistant first → support-agent (RAG before agents).

---

## Prerequisites

1. [core-python](../core-python/) modules 01, 03, 05
2. [backend-with-fastapi](../backend-with-fastapi/LEARNING-GUIDE.md) — task-api completed
3. OpenAI API key (or Ollama)

---

## Quick start — RAG Assistant

```bash
cd rag-assistant
cp backend/.env.example backend/.env    # add OPENAI_API_KEY
make install && make dev
```

- **UI:** http://localhost:3000 · **Docs:** [rag-assistant/docs/](rag-assistant/docs/01-rag-concepts.md)

---

## Quick start — Support Agent

```bash
cd support-agent
cp backend/.env.example backend/.env    # add OPENAI_API_KEY
make install && make dev
```

- **UI:** http://localhost:3001 · **Docs:** [support-agent/docs/](support-agent/docs/01-agents-and-multi-agent.md)

---

## Layout

```
fullstack-genai/
├── rag-assistant/       # Phase 3 — RAG
└── support-agent/       # Phase 4 — Multi-agent
```
