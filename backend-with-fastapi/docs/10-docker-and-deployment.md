# 10 — Docker & Deployment

Run the API with Postgres in production-like environment.

---

## What you'll learn

- Docker basics for Python APIs
- docker-compose with API + Postgres
- Environment variables in production
- Migration on startup

---

## THEORY

### Why Docker?

- Same environment on every machine
- Postgres instead of SQLite for real apps
- Easy deploy to cloud (AWS, GCP, Railway, etc.)

### Files

| File | Purpose |
|------|---------|
| `Dockerfile` | Multi-stage build — install deps, copy app |
| `docker-compose.yml` | Runs API + Postgres together |
| `scripts/prestart.sh` | Runs `alembic upgrade head` before start |
| `.env.example` | Template for all env vars |

### docker-compose services

```yaml
services:
  api:        # FastAPI app on port 8000
  db:         # Postgres 16 on port 5432
```

API waits for DB health check before starting.

### Production env vars

**Must change in production:**

```env
ENVIRONMENT=production
DEBUG=false
SECRET_KEY=<random-32-byte-hex>
DATABASE_URL=postgresql+psycopg2://taskapi:taskapi@db:5432/taskapi
```

Generate secret:

```bash
openssl rand -hex 32
```

### Multi-stage Dockerfile

1. **Builder stage** — install Python packages
2. **Runtime stage** — copy only what's needed (smaller image)

### Startup sequence (Docker)

```
1. Postgres starts → health check passes
2. prestart.sh → alembic upgrade head
3. uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## PRACTICE

### Local dev (SQLite — no Docker)

```bash
make dev
```

### Docker production stack

```bash
cp .env.example .env
# Edit .env: set DATABASE_URL to postgres line (uncomment)
make docker-up
curl http://127.0.0.1:8000/api/v1/ready
make docker-down
```

### Makefile commands

| Command | Action |
|---------|--------|
| `make dev` | Local uvicorn with reload |
| `make test` | Run pytest |
| `make migrate` | alembic upgrade head |
| `make docker-up` | Start Docker stack |
| `make docker-down` | Stop containers |

---

## Dev vs production

| | Development | Production |
|--|-------------|------------|
| Database | SQLite file | Postgres |
| Docs | `/docs` enabled | Disabled |
| Debug | `DEBUG=true` | `DEBUG=false` |
| Seed users | Auto-created | Manual / admin script |
| Migrations | Optional | Required (`alembic upgrade`) |

---

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Default SECRET_KEY in prod | Generate unique key |
| SQLite in production | Use Postgres |
| Skipping migrations | Run alembic in prestart.sh |

---

## Next

→ [11 — API Reference](11-api-reference.md)
