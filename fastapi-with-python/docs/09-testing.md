# 09 — Testing

Test your API with pytest — auth, RBAC, and CRUD.

---

## What you'll learn

- pytest basics for FastAPI
- TestClient for HTTP requests
- Fixtures for database and auth tokens
- What each test file covers

---

## THEORY

### Why test APIs?

- Catch bugs before deployment
- Document expected behavior
- Safe to refactor when tests pass

### Test stack

| Tool | Purpose |
|------|---------|
| **pytest** | Test runner |
| **TestClient** | Simulates HTTP requests without running server |
| **In-memory SQLite** | Fresh DB per test — no pollution |

### Test structure

```
tests/
├── conftest.py           # Shared fixtures (DB, tokens, client)
└── api/v1/
    ├── test_auth.py      # Register, login, refresh
    ├── test_rbac.py      # Admin vs user permissions
    └── test_tasks.py     # CRUD + ownership
```

### conftest.py explained

**Key fixtures:**

| Fixture | Purpose |
|---------|---------|
| `client` | TestClient for HTTP calls |
| `setup_database` | Creates tables + seed users (autouse) |
| `user_token` | JWT for regular user |
| `admin_token` | JWT for admin |
| `auth_headers` | `{"Authorization": "Bearer ..."}` |

**DB override:**

```python
app.dependency_overrides[get_db] = override_get_db
```

Tests use in-memory SQLite instead of real `task_api.db`.

### Running tests

```bash
make test
# or
pytest tests/ -v
pytest tests/api/v1/test_auth.py -v   # single file
```

---

## PRACTICE

### 1. Run all tests

```bash
cd fastapi-with-python/task-api
source .venv/bin/activate
make test
```

Expected: **15 passed**

### 2. Read one test

Open `tests/api/v1/test_auth.py` → `test_register_and_login` — follow the flow.

### 3. Break something on purpose

Change `TaskService.create_task` to always raise an error — run tests — see which fail — fix it.

### 4. Write a new test (exercise)

Add to `test_tasks.py`:

```python
def test_create_task_requires_title(client, auth_headers):
    response = client.post(
        "/api/v1/tasks",
        json={"title": "", "status": "pending"},
        headers=auth_headers,
    )
    assert response.status_code == 422
```

Run: `pytest tests/api/v1/test_tasks.py::test_create_task_requires_title -v`

---

## Test coverage map

| Test file | Covers |
|-----------|--------|
| `test_auth.py` | Register, login, refresh, /me, duplicate email |
| `test_rbac.py` | Admin list users, user denied, admin sees all tasks |
| `test_tasks.py` | CRUD, pagination, auth required, ownership 403 |
| health/ready | DB connectivity |

---

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Tests hit real database | Use dependency override + in-memory DB |
| Rate limit breaks tests | `limiter.enabled = False` in conftest |
| Forgetting auth headers | Use `auth_headers` fixture |

---

## Next

→ [10 — Docker & Deployment](10-docker-and-deployment.md)
