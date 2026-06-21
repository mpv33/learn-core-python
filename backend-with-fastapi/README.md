# Backend with FastAPI

**Phase 2** of the [GenAI Full-Stack Developer Track](../README.md) — production API skills every GenAI backend needs.

Learn with a **production-style FastAPI project** and 12 step-by-step guides.

---

## Start learning

1. Finish [core-python](../core-python/) modules 01, 03, 04, 05
2. Open **[LEARNING-GUIDE.md](LEARNING-GUIDE.md)** — follow steps 1–12
3. Run [task-api/](task-api/) while you read each guide

### Quick run

```bash
cd task-api
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt && cp .env.example .env
make dev
```

Open http://127.0.0.1:8000/docs

---

## Documentation

| Resource | Description |
|----------|-------------|
| **[LEARNING-GUIDE.md](LEARNING-GUIDE.md)** | Master guide — learning path, architecture |
| **[docs/](docs/README.md)** | 12 concept guides (REST, auth, DB, testing, Docker) |
| **[task-api/README.md](task-api/README.md)** | Project quick reference |

---

## What you'll learn

- REST APIs (HTTP, JSON, CRUD)
- FastAPI project structure (router → service → model)
- Database (SQLAlchemy, Alembic migrations)
- Auth (JWT, bcrypt, OAuth2 Bearer)
- RBAC, rate limiting, middleware, CORS
- Error handling, logging, pytest, Docker

These patterns are reused in **rag-assistant** and **support-agent**.

---

## Dev accounts

| Email | Password | Role |
|-------|----------|------|
| admin@example.com | admin123 | admin |
| user@example.com | user123 | user |

---

## Next — Phase 3 & 4

After this track → [fullstack-genai](../fullstack-genai/) (RAG + multi-agent capstone projects).
