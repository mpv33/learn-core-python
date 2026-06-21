# RAG Assistant — Learning Guide

Learn **Retrieval-Augmented Generation** by building one full-stack app used across industry: a **company knowledge assistant**.

---

## What is RAG?

**Problem:** LLMs don't know your private documents and may hallucinate.

**Solution:** RAG retrieves relevant chunks from your files, injects them into the prompt, and the model answers **using your data**.

```
Question → Embed → Search vectors → Top chunks + question → LLM → Answer + citations
```

---

## Learning path

| Step | Guide | Practice |
|------|-------|----------|
| 1 | [RAG concepts](docs/01-rag-concepts.md) | Read theory |
| 2 | [Architecture](docs/02-architecture.md) | Explore folder structure |
| 3 | [Setup](docs/03-setup-and-run.md) | `make dev`, upload a file |
| 4 | Backend: `services/chunker.py` | See how text is split |
| 5 | Backend: `services/embeddings.py` | See embedding calls |
| 6 | Backend: `services/rag_service.py` | Full ingest + query pipeline |
| 7 | Frontend: chat UI | Ask questions, read citations |
| 8 | [RAG vs fine-tuning vs agents](docs/04-rag-vs-finetuning-vs-agents.md) | When RAG wins |
| 9 | [LLM selection for RAG](docs/05-llm-selection-for-rag.md) | Pick models |
| 10 | Build challenges (below) | Extend the project |

**Time:** ~15–25 hours

---

## Setup

```bash
cd rag-assistant
python3 -m venv backend/.venv
source backend/.venv/bin/activate
pip install -r backend/requirements.txt
cp backend/.env.example backend/.env
# Edit .env — add OPENAI_API_KEY

cd frontend && npm install && cd ..
make dev
```

---

## Build challenges

Complete these to master RAG:

1. **Upload 3 company docs** (README, policy PDF, notes) — ask "What is our refund policy?"
2. **Toggle compare mode** — see RAG vs no-RAG answer side by side
3. **Change chunk size** in `.env` — observe answer quality
4. **Add a new file type** (e.g. `.csv`) to the ingest pipeline
5. **Write one pytest** for the chunker service

---

## Key files map

| File | Role |
|------|------|
| `backend/app/services/rag_service.py` | Main RAG orchestration |
| `backend/app/services/chunker.py` | Split documents |
| `backend/app/services/embeddings.py` | Vector embeddings |
| `backend/app/services/vector_store.py` | JSON file vector store (cosine similarity) |
| `backend/app/services/llm_client.py` | Chat completion |
| `backend/app/api/routes/documents.py` | Upload / list / delete |
| `backend/app/api/routes/chat.py` | RAG query endpoint |
| `frontend/app/page.tsx` | Chat + upload UI |

---

## API overview

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/api/v1/documents/upload` | Ingest file into vector store |
| GET | `/api/v1/documents` | List indexed documents |
| DELETE | `/api/v1/documents/{id}` | Remove document + chunks |
| POST | `/api/v1/chat` | Ask question (RAG or plain) |
| GET | `/api/v1/health` | Health check |

---

## Why one RAG project (not 8 separate apps)

Industry teams most often ship **document Q&A** first:

- Fastest path to value with private data
- Teaches embeddings, retrieval, prompting, full-stack integration
- Foundation for agents later (RAG + tools)

Fine-tuning, agents, and multi-modal are advanced layers **on top of** RAG — master this first.

---

## Next step

→ [docs/03-setup-and-run.md](docs/03-setup-and-run.md)
