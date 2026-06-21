# RAG Concepts

Core ideas behind Retrieval-Augmented Generation.

---

## The problem

| Plain LLM | Issue |
|-----------|--------|
| "What's our vacation policy?" | Model wasn't trained on **your** HR doc — guesses or hallucinates |
| "Summarize Q3 report" | Can't access files on your server |

## The RAG solution

1. **Ingest** — load documents, split into chunks
2. **Embed** — convert each chunk to a vector (list of numbers)
3. **Store** — save vectors in a vector database (ChromaDB)
4. **Retrieve** — embed the user's question, find similar chunks
5. **Generate** — send chunks + question to LLM, get grounded answer

---

## Key terms

| Term | Meaning |
|------|---------|
| **Chunk** | Small piece of text (e.g. 500 tokens) |
| **Embedding** | Numeric representation of meaning |
| **Vector store** | DB optimized for similarity search |
| **Top-k** | Number of chunks retrieved (e.g. 5) |
| **Citation** | Source chunk shown with the answer |

---

## Chunking rules of thumb

| Setting | Typical value | Tradeoff |
|---------|---------------|----------|
| Chunk size | 500–1000 chars | Bigger = more context, less precise retrieval |
| Overlap | 50–100 chars | Prevents cutting sentences mid-thought |
| Top-k | 3–8 | More chunks = more context, more noise |

**Config in this project:** `CHUNK_SIZE`, `CHUNK_OVERLAP` in `backend/.env`

---

## RAG prompt pattern

```
System: Answer only using the context below. If unknown, say "I don't know."
Cite sources as [1], [2].

Context:
[1] {chunk text}
[2] {chunk text}

User: {question}
```

See `backend/app/services/rag_service.py` → `_build_prompt()`

---

## When RAG is the right choice

- Internal docs, wikis, support KB
- Data changes frequently
- Need citations / audit trail
- Can't fine-tune on all company knowledge

Not ideal alone for: real-time prices, live API data (add agents/tools later).

---

## Next

→ [Architecture](02-architecture.md)
