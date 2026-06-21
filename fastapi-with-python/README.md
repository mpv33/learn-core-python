# FastAPI with Python

Learn backend development with a **production-style FastAPI project** — full docs and step-by-step guides included.

---

## Start learning

### New to this repo?

1. Finish **core-python** modules 01, 03, 04, 05 first
2. Open the **[Learning Guide](LEARNING-GUIDE.md)** — follow steps 1–12 in order
3. Run the project while you read each guide

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
| **[LEARNING-GUIDE.md](LEARNING-GUIDE.md)** | Master guide — learning path, prerequisites, architecture |
| **[docs/](docs/README.md)** | 12 step-by-step concept guides (theory + practice) |
| **[task-api/README.md](task-api/README.md)** | Project quick reference |

---

## What you'll learn

- REST APIs (HTTP, JSON, CRUD)
- FastAPI project structure (router → service → model)
- Database (SQLAlchemy, Alembic migrations)
- Auth (JWT, bcrypt, OAuth2 Bearer)
- RBAC (roles, permissions, ownership)
- Rate limiting, middleware, CORS
- Error handling and logging
- pytest testing
- Docker + Postgres deployment

---

## Dev accounts

| Email | Password | Role |
|-------|----------|------|
| admin@example.com | admin123 | admin |
| user@example.com | user123 | user |

Auto-created when `ENVIRONMENT=development`.

---

## Project

```
fastapi-with-python/
├── LEARNING-GUIDE.md       ← start here
├── docs/                   ← 12 learning guides
└── task-api/               ← the FastAPI project
```
