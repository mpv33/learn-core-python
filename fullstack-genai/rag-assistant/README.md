# RAG Assistant

**Phase 3 capstone** — [GenAI Full-Stack Developer Track](../../README.md)

One industry-valuable **RAG (Retrieval-Augmented Generation)** app — upload company documents, chat with grounded answers and citations.

**Stack:** Next.js 15 + FastAPI + vector search + OpenAI (or Ollama)

---

## Features

- Upload PDF, TXT, MD documents
- Automatic chunking + embedding + vector indexing
- Chat with **source citations**
- **Compare mode:** RAG vs plain LLM (see why RAG matters)
- Document list and delete

---

## Quick start

```bash
cp backend/.env.example backend/.env   # add OPENAI_API_KEY
make install
make dev
```

- UI: http://localhost:3000
- API: http://127.0.0.1:8000/docs

Upload `sample-docs/company-policy.txt` and ask: *"What is the refund policy?"*

---

## Learning docs

**Start here:** [LEARNING-GUIDE.md](LEARNING-GUIDE.md)

| Doc | Topic |
|-----|--------|
| [01-rag-concepts](docs/01-rag-concepts.md) | Theory |
| [02-architecture](docs/02-architecture.md) | System design |
| [03-setup-and-run](docs/03-setup-and-run.md) | Install & troubleshooting |
| [04-rag-vs-finetuning-vs-agents](docs/04-rag-vs-finetuning-vs-agents.md) | When to use RAG |
| [05-llm-selection-for-rag](docs/05-llm-selection-for-rag.md) | Model picks |

---

## API

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/api/v1/documents/upload` | Index a file |
| GET | `/api/v1/documents` | List indexed docs |
| DELETE | `/api/v1/documents/{id}` | Remove doc |
| POST | `/api/v1/chat` | Ask question (`use_rag: true/false`) |

---

## Project structure

```
rag-assistant/
├── LEARNING-GUIDE.md
├── docs/
├── backend/app/services/
│   ├── rag_service.py      ← main pipeline
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── llm_client.py
├── frontend/app/page.tsx   ← chat UI
└── sample-docs/            ← test documents
```
