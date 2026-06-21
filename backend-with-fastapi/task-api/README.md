# Task API

Production-style **Task Management REST API** — the hands-on project for the [Backend with FastAPI learning guides](../docs/README.md).

> **Learning?** Start with the [Learning Guide](../LEARNING-GUIDE.md), not this file.

---

## Quick start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
make dev
```

- **Swagger UI:** http://127.0.0.1:8000/docs
- **Learning guides:** [../docs/](../docs/README.md)

---

## Dev accounts

| Email | Password | Role |
|-------|----------|------|
| admin@example.com | admin123 | admin |
| user@example.com | user123 | user |

---

## Commands

| Command | Action |
|---------|--------|
| `make dev` | Start dev server (SQLite) |
| `make test` | Run pytest (15 tests) |
| `make migrate` | Apply Alembic migrations |
| `make docker-up` | Start API + Postgres |

---

## Concepts → code map

| Concept | Guide | Code |
|---------|-------|------|
| Project structure | [03](../docs/03-project-structure.md) | `app/factory.py`, `app/api/` |
| Database | [04](../docs/04-database-and-sqlalchemy.md) | `app/db/`, `app/models/` |
| Auth & JWT | [05](../docs/05-auth-and-jwt.md) | `app/core/security.py`, `app/api/v1/endpoints/auth.py` |
| RBAC | [06](../docs/06-rbac.md) | `app/core/rbac.py`, `app/services/task_service.py` |
| Rate limiting | [07](../docs/07-rate-limiting-and-middleware.md) | `app/core/limiter.py` |
| Errors & logging | [08](../docs/08-error-handling-and-logging.md) | `app/core/exceptions.py` |
| Testing | [09](../docs/09-testing.md) | `tests/` |
| Docker | [10](../docs/10-docker-and-deployment.md) | `Dockerfile`, `docker-compose.yml` |
| API reference | [11](../docs/11-api-reference.md) | all endpoints |

---

## Project structure

```
task-api/
├── app/
│   ├── main.py / factory.py
│   ├── api/v1/endpoints/     # HTTP routes
│   ├── core/                 # config, security, rbac, errors
│   ├── db/                   # SQLAlchemy sessions
│   ├── models/               # User, Task
│   ├── schemas/              # Pydantic validation
│   ├── services/             # Business logic
│   └── middleware/           # Request logging
├── alembic/                  # Migrations
├── tests/
├── Dockerfile
└── docker-compose.yml
```

---

## API endpoints (summary)

| Method | Path | Auth |
|--------|------|------|
| GET | `/api/v1/health` | No |
| GET | `/api/v1/ready` | No |
| POST | `/api/v1/auth/register` | No |
| POST | `/api/v1/auth/login` | No |
| GET | `/api/v1/auth/me` | Yes |
| CRUD | `/api/v1/tasks` | Yes |
| GET | `/api/v1/users` | Admin |

Full reference: [docs/11-api-reference.md](../docs/11-api-reference.md)
