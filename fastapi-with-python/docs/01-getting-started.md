# 01 — Getting Started

Set up the project, run the server, and make your first API calls.

---

## What you'll learn

- Create a virtual environment and install dependencies
- Start the FastAPI dev server
- Use Swagger UI to explore endpoints
- Login and call a protected endpoint

---

## THEORY

### What is FastAPI?

FastAPI is a Python web framework for building **REST APIs** — servers that receive HTTP requests and return JSON. It is:

- **Fast** — high performance (uses Starlette + Pydantic)
- **Auto-documented** — generates Swagger UI at `/docs`
- **Type-safe** — uses Python type hints for validation

### What is uvicorn?

**Uvicorn** is the ASGI server that actually runs your FastAPI app. Think of it as the engine; FastAPI is the car.

```
uvicorn app.main:app --reload
         │      │
         │      └── FastAPI instance named `app`
         └── Python module path
```

`--reload` restarts the server when you save code changes (dev only).

---

## Setup steps

```bash
cd fastapi-with-python/task-api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
make dev
```

You should see:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete.
```

---

## PRACTICE

### 1. Health check (no auth)

```bash
curl http://127.0.0.1:8000/api/v1/health
```

Expected:

```json
{"status":"ok","app":"Task API","version":"1.0.0","environment":"development"}
```

### 2. Readiness check (tests DB connection)

```bash
curl http://127.0.0.1:8000/api/v1/ready
```

Expected: `"database": "connected"`

### 3. Explore Swagger UI

1. Open http://127.0.0.1:8000/docs
2. Expand **Auth** → `POST /api/v1/auth/login`
3. Click **Try it out**
4. Enter:
   - **username:** `user@example.com`
   - **password:** `user123`
5. Click **Execute** — copy the `access_token`

### 4. Authorize in Swagger

1. Click the **Authorize** button (top right)
2. Enter: `Bearer <paste_access_token>`
3. Now try **Tasks** → `GET /api/v1/tasks`

### 5. Create a task via curl

```bash
TOKEN="<your_access_token>"

curl -X POST http://127.0.0.1:8000/api/v1/tasks \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"My first task","status":"pending"}'
```

---

## Code to read

| File | Purpose |
|------|---------|
| `app/main.py` | Entry point — exports `app` for uvicorn |
| `app/factory.py` | `create_app()` — builds and configures FastAPI |
| `app/core/config.py` | Reads settings from `.env` |
| `app/api/v1/endpoints/health.py` | Health + readiness endpoints |

---

## Common mistakes

| Mistake | Fix |
|---------|-----|
| `command not found: uvicorn` | Activate `.venv` first |
| `401 Unauthorized` on tasks | Login and pass Bearer token |
| Login fails with JSON body | Login uses **form data**, not JSON — use `username` + `password` fields |
| Port already in use | Kill old process or change `PORT` in `.env` |

---

## Check your understanding

1. What command starts the dev server?
2. What URL shows interactive API docs?
3. Why does login use `username` instead of `email` in the form?

**Answers:** (1) `make dev` or `uvicorn app.main:app --reload` (2) `/docs` (3) OAuth2 standard uses `username` field — we put email there.

---

## Next

→ [02 — How REST APIs Work](02-how-rest-apis-work.md)
