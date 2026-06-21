# Setup and Run

Get the RAG platform running locally.

---

## Requirements

- Python 3.10+
- Node.js 18+
- OpenAI API key **or** Ollama running locally

---

## Step 1 — Backend

```bash
cd rag-assistant
python3 -m venv backend/.venv
source backend/.venv/bin/activate
pip install -r backend/requirements.txt
cp backend/.env.example backend/.env
```

Edit `backend/.env`:

```env
OPENAI_API_KEY=sk-your-key-here
LLM_PROVIDER=openai
OPENAI_MODEL=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small
```

---

## Step 2 — Frontend

```bash
cd frontend
npm install
cp .env.local.example .env.local
cd ..
```

`.env.local`:

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

---

## Step 3 — Run

```bash
make dev
```

Or separately:

```bash
make backend   # :8000
make frontend  # :3000
```

---

## Step 4 — Try it

1. Open http://localhost:3000
2. Upload a `.txt` or `.md` file (try `sample-docs/company-policy.txt`)
3. Ask: "What are the key points in this document?"
4. Enable **Compare mode** to see RAG vs plain LLM

---

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `401` from OpenAI | Check `OPENAI_API_KEY` in backend/.env |
| CORS error | Ensure backend running; check `CORS_ORIGINS` |
| Empty answers | Upload a document first; check top-k chunks in response |
| Vector store errors | Delete `backend/data/vectors/` and re-upload |

---

## Tests

```bash
make test
```

---

## Next

Explore `backend/app/services/rag_service.py` while using the app.
