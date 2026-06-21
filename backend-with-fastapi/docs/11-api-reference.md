# 11 — API Reference

Complete endpoint reference with curl examples.

---

## Base URL

```
http://127.0.0.1:8000
```

All v1 routes prefixed with `/api/v1`.

---

## Authentication

Most endpoints require:

```
Authorization: Bearer <access_token>
```

Get token via login (see below).

---

## Health

### GET /api/v1/health

Liveness probe — no auth.

```bash
curl http://127.0.0.1:8000/api/v1/health
```

**Response 200:**

```json
{
  "status": "ok",
  "app": "Task API",
  "version": "1.0.0",
  "environment": "development"
}
```

### GET /api/v1/ready

Readiness probe — checks database.

```bash
curl http://127.0.0.1:8000/api/v1/ready
```

**Response 200:**

```json
{
  "status": "ready",
  "database": "connected",
  "app": "Task API",
  "version": "1.0.0"
}
```

---

## Auth

### POST /api/v1/auth/register

Create account. Rate limited.

```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "new@example.com",
    "password": "secret123",
    "full_name": "New User"
  }'
```

**Response 201:** User object (no password).

### POST /api/v1/auth/login

OAuth2 form login. Rate limited.

```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -d "username=user@example.com&password=user123"
```

**Response 200:**

```json
{
  "access_token": "eyJ...",
  "refresh_token": "eyJ...",
  "token_type": "bearer"
}
```

### POST /api/v1/auth/refresh

```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/refresh \
  -H "Content-Type: application/json" \
  -d '{"refresh_token": "<refresh_token>"}'
```

### GET /api/v1/auth/me

Requires auth.

```bash
curl http://127.0.0.1:8000/api/v1/auth/me \
  -H "Authorization: Bearer $TOKEN"
```

---

## Tasks

All task endpoints require auth.

### GET /api/v1/tasks

List tasks with pagination.

| Query param | Type | Description |
|-------------|------|-------------|
| `status` | string | `pending`, `in_progress`, `done` |
| `skip` | int | Offset (default 0) |
| `limit` | int | Page size (default 100, max 500) |

```bash
curl "http://127.0.0.1:8000/api/v1/tasks?status=pending&skip=0&limit=10" \
  -H "Authorization: Bearer $TOKEN"
```

**Response 200:**

```json
{
  "items": [...],
  "total": 5,
  "skip": 0,
  "limit": 10
}
```

### POST /api/v1/tasks

```bash
curl -X POST http://127.0.0.1:8000/api/v1/tasks \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn FastAPI",
    "description": "Complete the learning guide",
    "status": "pending"
  }'
```

**Response 201:** Created task with `id`, `created_at`, `updated_at`.

### GET /api/v1/tasks/{id}

```bash
curl http://127.0.0.1:8000/api/v1/tasks/1 \
  -H "Authorization: Bearer $TOKEN"
```

### PATCH /api/v1/tasks/{id}

Partial update — only send fields to change.

```bash
curl -X PATCH http://127.0.0.1:8000/api/v1/tasks/1 \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"status": "in_progress"}'
```

### DELETE /api/v1/tasks/{id}

```bash
curl -X DELETE http://127.0.0.1:8000/api/v1/tasks/1 \
  -H "Authorization: Bearer $TOKEN"
```

**Response 204:** Empty body.

---

## Users (Admin only)

### GET /api/v1/users

```bash
curl http://127.0.0.1:8000/api/v1/users \
  -H "Authorization: Bearer $ADMIN_TOKEN"
```

### GET /api/v1/users/{id}

```bash
curl http://127.0.0.1:8000/api/v1/users/1 \
  -H "Authorization: Bearer $ADMIN_TOKEN"
```

---

## Error response format

All errors return:

```json
{"detail": "Human readable message"}
```

Validation errors (422) return array in `detail`.

---

## Swagger UI

Interactive docs: http://127.0.0.1:8000/docs

Use **Authorize** button with `Bearer <token>`.

---

## Next

→ [12 — Interview Concepts](12-interview-concepts.md)
