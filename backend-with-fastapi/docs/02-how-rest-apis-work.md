# 02 — How REST APIs Work

HTTP basics every backend developer must know.

---

## What you'll learn

- HTTP methods and when to use each
- Status codes (200, 201, 401, 404, etc.)
- JSON request/response bodies
- CRUD mapping to REST endpoints

---

## THEORY

### Client–Server model

```
Client (browser, mobile app, curl)
    │
    │  HTTP Request:  POST /api/v1/tasks  + JSON body + headers
    ▼
Server (FastAPI + uvicorn)
    │
    │  HTTP Response: 201 Created + JSON body
    ▼
Client
```

### HTTP methods

| Method | Purpose | Example in task-api |
|--------|---------|---------------------|
| **GET** | Read data | `GET /api/v1/tasks` — list tasks |
| **POST** | Create new resource | `POST /api/v1/tasks` — create task |
| **PATCH** | Partial update | `PATCH /api/v1/tasks/1` — update status only |
| **PUT** | Full replace | (not used in this project) |
| **DELETE** | Remove resource | `DELETE /api/v1/tasks/1` |

### Status codes

| Code | Meaning | When task-api returns it |
|------|---------|--------------------------|
| **200** | OK | Successful GET, PATCH |
| **201** | Created | Successful POST |
| **204** | No Content | Successful DELETE |
| **401** | Unauthorized | Missing or invalid token |
| **403** | Forbidden | Valid token but no permission |
| **404** | Not Found | Task ID doesn't exist |
| **409** | Conflict | Email already registered |
| **422** | Validation Error | Invalid JSON (Pydantic) |
| **429** | Too Many Requests | Rate limit exceeded |
| **500** | Server Error | Unexpected bug |

### JSON

APIs send data as **JSON** (JavaScript Object Notation):

```json
{
  "title": "Learn FastAPI",
  "description": "Build REST APIs",
  "status": "pending"
}
```

FastAPI uses **Pydantic schemas** (`app/schemas/`) to validate JSON automatically.

### CRUD → REST mapping

| CRUD | REST | Endpoint |
|------|------|----------|
| Create | POST | `/api/v1/tasks` |
| Read (list) | GET | `/api/v1/tasks` |
| Read (one) | GET | `/api/v1/tasks/{id}` |
| Update | PATCH | `/api/v1/tasks/{id}` |
| Delete | DELETE | `/api/v1/tasks/{id}` |

---

## PRACTICE

### Exercise 1: Trace a GET request

```bash
curl -v http://127.0.0.1:8000/api/v1/health
```

The `-v` flag shows headers. Look for:

```
< HTTP/1.1 200 OK
< content-type: application/json
```

### Exercise 2: See a 401

```bash
curl -v http://127.0.0.1:8000/api/v1/tasks
```

No token → **401 Unauthorized**

### Exercise 3: See a 422 validation error

```bash
curl -X POST http://127.0.0.1:8000/api/v1/tasks \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":""}'
```

Empty title → **422** (min_length=1 validation)

### Exercise 4: See a 404

```bash
curl http://127.0.0.1:8000/api/v1/tasks/99999 \
  -H "Authorization: Bearer $TOKEN"
```

Non-existent ID → **404**

---

## Headers you will use

| Header | Purpose | Example |
|--------|---------|---------|
| `Content-Type` | Body format | `application/json` |
| `Authorization` | Auth token | `Bearer eyJhbG...` |
| `X-Process-Time-Ms` | Response time (our middleware) | `12.3` |

---

## Common mistakes

- Using **POST** when you mean **PATCH** for updates
- Sending JSON to `/login` — login expects **form-urlencoded**
- Ignoring status codes — always check `response.status_code` in code

---

## Next

→ [03 — Project Structure](03-project-structure.md)
