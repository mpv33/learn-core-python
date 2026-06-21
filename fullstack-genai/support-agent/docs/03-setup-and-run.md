# Setup — Support Agent

Install and run the customer support multi-agent app.

---

## Prerequisites

- Python 3.10+
- Node.js 18+
- OpenAI API key (or Ollama running locally)
- Completed [rag-assistant](../../rag-assistant/) recommended (same stack patterns)

---

## Install

```bash
cd support-agent

cp backend/.env.example backend/.env
# Edit backend/.env — set OPENAI_API_KEY=

make install
```

This creates `backend/.venv` and installs frontend npm packages.

---

## Run

```bash
make dev
```

| URL | Purpose |
|-----|---------|
| http://localhost:3001 | Support chat UI |
| http://127.0.0.1:8001/docs | Swagger API |

Stop with `Ctrl+C` in the terminal.

---

## Run backend / frontend separately

```bash
make backend    # API only on :8001
make frontend   # UI only on :3001
```

---

## Tests (no API key needed)

```bash
make test
```

Covers knowledge base search, order lookup, and triage keyword fallback.

---

## Ollama (optional)

In `backend/.env`:

```
LLM_PROVIDER=ollama
OLLAMA_CHAT_MODEL=llama3.1:8b
```

Triage JSON parsing may be less reliable on smaller models — OpenAI is recommended for learning.

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `OPENAI_API_KEY required` | Set key in `backend/.env` |
| CORS error | Ensure UI uses :3001 and `CORS_ORIGINS` includes it |
| Empty KB answers | Check `KNOWLEDGE_BASE_PATH` points to `sample-data/knowledge-base.md` |
| Order not found | Use sample IDs: ORD-1001 … ORD-1004 |
| Port in use | Change ports in Makefile / `frontend/package.json` |

---

## Sample data

Edit `sample-data/knowledge-base.md` and `sample-data/orders.json` to customize policies and orders without code changes.
