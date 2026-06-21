# 05 — Auth & JWT

Login, tokens, password security, and protecting routes.

---

## What you'll learn

- Why APIs use tokens instead of sending passwords every time
- JWT structure (header, payload, signature)
- bcrypt password hashing
- OAuth2 Bearer flow in FastAPI

---

## THEORY

### The problem

If you send `email + password` on every request:

- Password exposed repeatedly
- No way to revoke access without changing password
- Server must check password every time (slow)

### The solution: JWT (JSON Web Token)

```
1. User logs in once with email + password
2. Server returns access_token (JWT)
3. Client sends token on every request: Authorization: Bearer <token>
4. Server validates token — no password needed
```

### JWT structure

A JWT has 3 parts separated by dots:

```
eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIiwicm9sZSI6InVzZXIifQ.signature
│                      │                              │
header                 payload                        signature
```

**Payload** in our app:

```json
{
  "sub": "1",           // user id
  "role": "user",       // for RBAC
  "type": "access",     // access vs refresh
  "exp": 1710000000     // expiry timestamp
}
```

**File:** `app/core/security.py` — `create_access_token()`, `verify_access_token()`

### Password hashing

**Never store plain passwords.** We use **bcrypt**:

```python
hashed = hash_password("user123")      # store in DB
verify_password("user123", hashed)     # True on login
```

**File:** `app/core/security.py`

### Auth endpoints

| Endpoint | Purpose |
|----------|---------|
| `POST /auth/register` | Create account |
| `POST /auth/login` | Get tokens (OAuth2 form) |
| `POST /auth/refresh` | New access token from refresh token |
| `GET /auth/me` | Current user profile |

**File:** `app/api/v1/endpoints/auth.py`  
**Service:** `app/services/auth_service.py`

### Protecting routes

**File:** `app/api/deps.py`

```python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), ...):
    return auth_service.get_user_from_token(token)
```

Any route with `Depends(get_current_active_user)` requires a valid token.

### Access vs refresh token

| Token | Lifetime | Use |
|-------|----------|-----|
| Access | 30 min (configurable) | API requests |
| Refresh | 7 days | Get new access token without re-login |

**Config:** `.env` → `ACCESS_TOKEN_EXPIRE_MINUTES`, `REFRESH_TOKEN_EXPIRE_DAYS`

---

## PRACTICE

### 1. Register a new user

```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"learner@example.com","password":"learn123","full_name":"Learner"}'
```

### 2. Login

```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/login \
  -d "username=learner@example.com&password=learn123"
```

Save `access_token` and `refresh_token`.

### 3. Call /me

```bash
curl http://127.0.0.1:8000/api/v1/auth/me \
  -H "Authorization: Bearer <access_token>"
```

### 4. Refresh token

```bash
curl -X POST http://127.0.0.1:8000/api/v1/auth/refresh \
  -H "Content-Type: application/json" \
  -d '{"refresh_token":"<refresh_token>"}'
```

### 5. Decode JWT (learning only)

Paste your token at https://jwt.io — see payload (never do this with production secrets in public).

---

## Security checklist (production)

- [ ] Change `SECRET_KEY` in `.env` (use `openssl rand -hex 32`)
- [ ] Use HTTPS only
- [ ] Short access token lifetime
- [ ] Never log tokens

---

## Common mistakes

| Mistake | Fix |
|---------|-----|
| Sending JSON to `/login` | Use form: `username` + `password` |
| Storing JWT in plain localStorage (XSS risk) | Learn httpOnly cookies for production |
| Using same secret in dev and prod | Separate `.env` per environment |

---

## Next

→ [06 — RBAC](06-rbac.md)
