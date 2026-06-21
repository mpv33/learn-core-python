# LLM Selection for RAG

Best models for embeddings, chat, and local development.

---

## RAG uses two models

| Role | Purpose |
|------|---------|
| **Embedding model** | Convert chunks + questions to vectors |
| **Chat model** | Generate answer from retrieved context |

---

## Recommended stacks

### Production (API)

| Component | Model | Why |
|-----------|-------|-----|
| Embeddings | `text-embedding-3-small` | Cheap, good quality |
| Chat | `gpt-4o-mini` | Fast, cheap, strong instruction following |
| Chat (quality) | `gpt-4o` or `claude-3-5-sonnet` | Hard questions |

### Local / private (Ollama)

| Component | Model |
|-----------|-------|
| Embeddings | `nomic-embed-text` |
| Chat | `llama3.1:8b` |

Set in `.env`:

```env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_CHAT_MODEL=llama3.1:8b
OLLAMA_EMBED_MODEL=nomic-embed-text
```

---

## Config in this project

All in `backend/.env` — switch without code changes via `app/services/llm_client.py` and `embeddings.py`.

---

## Cost tips

- Use `gpt-4o-mini` + `text-embedding-3-small` while learning
- Smaller top-k (3–5) = fewer tokens in prompt
- Cache embeddings — re-embed only when documents change

---

## Avoid

- Using chat model for embeddings (wrong tool)
- Huge chunks + large top-k (expensive, noisy context)
- Frontier models for every dev test (use mini or Ollama)
