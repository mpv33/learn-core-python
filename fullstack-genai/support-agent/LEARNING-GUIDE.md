# Support Agent — Learning Guide

Build a **customer support multi-agent system** after completing the RAG project.

---

## What you'll learn

- Single vs multi-agent architectures
- Intent triage and routing
- KB-grounded answers (RAG-lite)
- Tool use for order lookup
- Human escalation and ticket creation
- Supervisor orchestration pattern

---

## Learning path

| Step | Guide | Practice |
|------|-------|----------|
| 1 | [Agents & multi-agent](docs/01-agents-and-multi-agent.md) | Read theory |
| 2 | [Architecture](docs/02-architecture.md) | Explore folder structure |
| 3 | [Setup](docs/03-setup-and-run.md) | `make dev`, try sample prompts |
| 4 | `agents/triage.py` | See intent classification |
| 5 | `agents/knowledge.py` | KB retrieval + LLM answer |
| 6 | `agents/orders.py` | Structured order lookup |
| 7 | `services/orchestrator.py` | Full multi-agent workflow |
| 8 | Frontend agent trace | Inspect routing in UI |
| 9 | Build challenges (below) | Extend the project |

**Time:** ~10–15 hours (after rag-assistant)

---

## Setup

```bash
cd support-agent
cp backend/.env.example backend/.env
# Add OPENAI_API_KEY
make install && make dev
```

---

## Key files

| File | Purpose |
|------|---------|
| `agents/triage.py` | Classify customer intent |
| `agents/knowledge.py` | Answer from support KB |
| `agents/orders.py` | Order status agent |
| `agents/escalation.py` | Create support tickets |
| `services/orchestrator.py` | Supervisor routing |
| `sample-data/` | KB + mock orders |

---

## Build challenges

1. Add a **Billing Agent** with a mock duplicate-charge lookup API
2. Show **confidence threshold** in UI and let user adjust it
3. Replace keyword KB search with embeddings from rag-assistant
4. Add conversation memory (last 5 messages in context)
5. Stream supervisor reply with SSE

---

## How this connects to RAG

| rag-assistant | support-agent |
|---------------|---------------|
| User uploads docs | Pre-loaded support KB |
| Vector search | Keyword section search |
| Single RAG pipeline | Multi-agent routing |
| Compare RAG vs LLM | Compare agent traces |

Both are production patterns — RAG for open-ended knowledge, agents for structured support workflows.
