# 12 — Interview Concepts

Common backend / FastAPI interview questions with answers tied to this project.

---

## FastAPI basics

### Q: What is FastAPI and why use it over Flask/Django REST?

**Answer:** FastAPI is a modern async-capable Python framework for building APIs. Key advantages:

- Automatic OpenAPI docs from type hints
- Pydantic validation built-in
- High performance (Starlette + uvicorn)
- Less boilerplate than Flask for typed APIs

**In this project:** See `app/factory.py` and `/docs` auto-generation.

---

### Q: What is ASGI vs WSGI?

**Answer:**

- **WSGI** (Flask, Django) — synchronous, one request per worker
- **ASGI** (FastAPI, Starlette) — async-capable, WebSockets, higher concurrency

**In this project:** uvicorn is the ASGI server (`uvicorn app.main:app`).

---

## Database

### Q: What is an ORM? Why not raw SQL?

**Answer:** ORM maps Python classes to database tables. Benefits: type safety, less SQL injection risk, database-agnostic code. Raw SQL is fine for complex queries.

**In this project:** SQLAlchemy models in `app/models/`, sessions in `app/db/session.py`.

---

### Q: What are database migrations?

**Answer:** Version-controlled schema changes applied incrementally. Lets teams evolve DB without manual SQL.

**In this project:** Alembic in `alembic/versions/`.

---

## Authentication

### Q: What is JWT? How does it work?

**Answer:** Signed token containing claims (user id, expiry). Server verifies signature with secret key — no DB lookup needed per request (though we still load user for fresh data).

**Structure:** header.payload.signature

**In this project:** `app/core/security.py`

---

### Q: Why hash passwords? Why bcrypt?

**Answer:** Plain passwords in DB = disaster if leaked. bcrypt is slow by design — makes brute-force expensive.

**In this project:** `hash_password()` / `verify_password()` in `security.py`.

---

### Q: Access token vs refresh token?

**Answer:**

- **Access** — short-lived, sent with every API call
- **Refresh** — long-lived, used only to get new access token

Limits damage if access token is stolen.

---

## Authorization (RBAC)

### Q: Authentication vs authorization?

**Answer:**

- **Authentication** — prove identity (login)
- **Authorization** — check permissions (can this user delete this task?)

401 vs 403.

**In this project:** JWT auth + `app/core/rbac.py` + ownership in `TaskService`.

---

### Q: What is RBAC?

**Answer:** Role-Based Access Control — permissions assigned to roles, users get roles. Simpler than per-user permissions for most apps.

**In this project:** `admin` and `user` roles, `Permission` enum.

---

## Architecture

### Q: Why separate router, service, and model layers?

**Answer:**

- **Router** — HTTP concerns only
- **Service** — business logic, testable without HTTP
- **Model** — database schema

**In this project:** `tasks.py` → `TaskService` → `Task` model.

---

### Q: What is dependency injection in FastAPI?

**Answer:** FastAPI resolves `Depends(get_db)` and `Depends(get_current_user)` automatically per request.

**In this project:** `app/api/deps.py`

---

## Production

### Q: What is rate limiting? Why on login?

**Answer:** Caps requests per IP/time window. Login is brute-force target — limit attempts.

**In this project:** slowapi on auth routes, `429` response.

---

### Q: Liveness vs readiness probes?

**Answer:**

- **Liveness** — is process alive? Restart if not.
- **Readiness** — can it serve traffic? (DB connected?) Remove from load balancer if not.

**In this project:** `/health` vs `/ready`

---

### Q: What should never be in git?

**Answer:** `.env`, secrets, `SECRET_KEY`, production passwords, private keys.

**In this project:** `.env.example` is template only — real `.env` is gitignored.

---

## Testing

### Q: How do you test authenticated endpoints?

**Answer:** Override DB dependency, seed test users, login via TestClient, pass Bearer token in headers.

**In this project:** `tests/conftest.py` fixtures.

---

## Practice exercise for interviews

Explain out loud (5 minutes each):

1. Full flow of `POST /api/v1/tasks` from HTTP to database
2. What happens when a user tries to access another user's task
3. How you would add a new `manager` role

---

## Back to guides

→ [LEARNING-GUIDE.md](../LEARNING-GUIDE.md)
