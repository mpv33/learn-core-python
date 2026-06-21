# 08 — Error Handling & Logging

Return clear HTTP errors and log what happens in your app.

---

## What you'll learn

- Custom domain exceptions
- Global exception handlers
- Structured logging setup
- Mapping errors to HTTP status codes

---

## THEORY

### Domain exceptions

Instead of raising random errors, we use **named exceptions** that map to HTTP codes:

**File:** `app/core/exceptions.py`

| Exception | HTTP Code | When |
|-----------|-----------|------|
| `NotFoundError` | 404 | Task/user not found |
| `UnauthorizedError` | 401 | Bad login or token |
| `ForbiddenError` | 403 | No permission |
| `ConflictError` | 409 | Duplicate email |
| `AppException` | 400 | Generic client error |

**In services:**

```python
raise NotFoundError(f"Task {task_id} not found")
```

**In routers:** Often no try/except needed — global handler catches `AppException`.

### Global exception handlers

**File:** `app/core/exceptions.py` → `register_exception_handlers(app)`

Registered in `app/factory.py`:

```python
register_exception_handlers(app)
```

Also handles:

- `jwt.PyJWTError` → 401
- `RateLimitExceeded` → 429
- Unhandled `Exception` → 500 (hides details in production)

### Logging

**File:** `app/core/logging.py`

```python
logging.basicConfig(
    format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    level=settings.log_level,  # INFO, DEBUG, etc.
)
```

Called on startup in `app/factory.py` lifespan.

**Usage in any file:**

```python
from app.core.logging import get_logger
logger = get_logger(__name__)
logger.info("Something happened")
```

### Pydantic validation errors

FastAPI automatically returns **422** when JSON doesn't match schema:

```json
{
  "detail": [
    {"loc": ["body", "title"], "msg": "String should have at least 1 character"}
  ]
}
```

No extra code needed — Pydantic + FastAPI handle this.

---

## PRACTICE

### 1. Trigger each error type

```bash
# 401 — no token
curl http://127.0.0.1:8000/api/v1/tasks

# 403 — access another user's task (see guide 06)
# 404 — GET /tasks/99999
# 409 — register duplicate email
# 422 — POST task with empty title
```

### 2. Read exception handler code

Open `app/core/exceptions.py` — trace how `NotFoundError` becomes JSON.

### 3. Change log level

In `.env`: `LOG_LEVEL=DEBUG` — restart server, see more output.

---

## Production tip

Set `DEBUG=false` and `ENVIRONMENT=production` — unhandled errors return generic "Internal server error" instead of stack traces.

---

## Next

→ [09 — Testing](09-testing.md)
