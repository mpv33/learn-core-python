# 04 — Database & SQLAlchemy

Connect to a database, define models, and run migrations.

---

## What you'll learn

- SQLAlchemy ORM basics
- Database sessions and dependency injection
- Connection pooling and health checks
- Alembic migrations
- Dev seed data

---

## THEORY

### What is an ORM?

**ORM (Object-Relational Mapping)** lets you use Python classes instead of writing SQL:

```python
# Instead of: SELECT * FROM tasks WHERE id = 1
task = db.get(Task, 1)
```

### Key files

| File | Role |
|------|------|
| `app/db/base.py` | `Base` class — all models inherit from this |
| `app/db/session.py` | Engine, connection pool, `get_db()` |
| `app/models/user.py` | `users` table |
| `app/models/task.py` | `tasks` table (with `owner_id` FK) |
| `app/db/init_db.py` | Creates tables + seeds dev users |

### Database session lifecycle

Each HTTP request gets **one database session**:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db          # route handler uses db
    finally:
        db.close()        # always close after response
```

FastAPI injects this via `Depends(get_db)`.

### Connection pooling (Postgres)

In `app/db/session.py`:

```python
engine = create_engine(
    url,
    pool_pre_ping=True,    # test connection before use
    pool_size=5,           # Postgres only
    max_overflow=10,
)
```

`pool_pre_ping` avoids "connection lost" errors in production.

### Readiness vs liveness

| Endpoint | Checks | Use case |
|----------|--------|----------|
| `/api/v1/health` | App is running | Kubernetes liveness |
| `/api/v1/ready` | App + DB connected | Kubernetes readiness |

**File:** `app/api/v1/endpoints/health.py` + `check_db_connection()` in `session.py`

### Alembic migrations

**Never** change production DB with `create_all()` — use versioned migrations:

```bash
alembic upgrade head     # apply all migrations
```

Migrations live in `alembic/versions/`:

- `001_initial_tasks_table.py` — tasks table
- `002_users_and_task_ownership.py` — users + owner_id on tasks

### Models in this project

**User** (`app/models/user.py`):

- `email`, `hashed_password`, `role` (admin/user)
- One user → many tasks (relationship)

**Task** (`app/models/task.py`):

- `title`, `description`, `status`
- `owner_id` → foreign key to `users.id`

---

## PRACTICE

### 1. Check DB readiness

```bash
curl http://127.0.0.1:8000/api/v1/ready
```

### 2. Inspect SQLite file (dev)

After creating tasks, the file `task_api.db` appears in `task-api/`:

```bash
sqlite3 task_api.db ".tables"
# users  tasks  alembic_version
```

### 3. Run migrations

```bash
cd backend-with-fastapi/task-api
source .venv/bin/activate
alembic upgrade head
alembic current    # shows current revision
```

### 4. Read the seed logic

Open `app/db/init_db.py` — see how admin/user accounts are created on startup in development.

---

## Pydantic vs SQLAlchemy

| | SQLAlchemy Model | Pydantic Schema |
|--|------------------|-----------------|
| Purpose | Database table | API JSON validation |
| Location | `app/models/` | `app/schemas/` |
| Example | `Task` (ORM) | `TaskCreate`, `TaskRead` |

**Why both?** API shape ≠ database shape. You might hide `hashed_password` from responses.

---

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Forgetting to import models before `create_all` | `init_db.py` imports `app.models` |
| Sharing one session across requests | Use `get_db()` per request |
| Editing DB schema without migration | Create Alembic revision |

---

## Next

→ [05 — Auth & JWT](05-auth-and-jwt.md)
