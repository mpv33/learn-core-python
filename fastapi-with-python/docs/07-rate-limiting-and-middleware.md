# 07 — Rate Limiting & Middleware

Protect auth endpoints and log every request.

---

## What you'll learn

- What rate limiting is and why it matters
- How slowapi works with FastAPI
- HTTP middleware concept
- CORS basics

---

## THEORY

### Rate limiting

Prevents abuse — e.g. brute-force password attacks on `/login`:

```
Max 10 login attempts per minute per IP address
→ 11th attempt returns 429 Too Many Requests
```

**File:** `app/core/limiter.py`

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
```

**Applied on auth routes** (`app/api/v1/endpoints/auth.py`):

```python
@router.post("/login")
@limiter.limit(settings.rate_limit_auth)   # "10/minute"
def login(request: Request, ...):
```

**Config in `.env`:**

```
RATE_LIMIT_AUTH=10/minute
RATE_LIMIT_REGISTER=5/minute
```

### Middleware

Middleware runs **before and after** every request:

```
Request → [CORS] → [Rate Limit] → [Logging] → Route Handler → Response
```

**Files:**

| Middleware | File | Purpose |
|------------|------|---------|
| CORS | `app/factory.py` | Allow frontend on different port |
| SlowAPI | `app/factory.py` | Rate limit enforcement |
| Request logging | `app/middleware/request_logging.py` | Log method, path, time |

### Request logging

Every request prints to terminal:

```
2026-06-21 10:00:00 | INFO | http | GET /api/v1/tasks -> 200 (15.2ms)
```

Response includes header: `X-Process-Time-Ms: 15.2`

### CORS (Cross-Origin Resource Sharing)

Browsers block requests from `localhost:3000` (React) to `localhost:8000` (API) unless the API allows it.

**File:** `app/factory.py`

```python
CORSMiddleware(
    allow_origins=settings.cors_origins,  # from .env
    allow_credentials=True,
    allow_methods=["*"],
)
```

---

## PRACTICE

### 1. Watch logs

Run `make dev`, make a few API calls — watch terminal output.

### 2. Trigger rate limit (optional)

Run login 11+ times quickly in a loop — eventually get 429:

```bash
for i in $(seq 1 12); do
  curl -s -o /dev/null -w "%{http_code}\n" \
    -X POST http://127.0.0.1:8000/api/v1/auth/login \
    -d "username=user@example.com&password=wrong"
done
```

### 3. Check response time header

```bash
curl -v http://127.0.0.1:8000/api/v1/health 2>&1 | grep X-Process-Time
```

---

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Forgetting `Request` param on rate-limited routes | slowapi requires it |
| Disabling CORS entirely in production | Set specific origins, not `*` with credentials |
| No rate limit on login | Always limit auth endpoints |

---

## Next

→ [08 — Error Handling & Logging](08-error-handling-and-logging.md)
