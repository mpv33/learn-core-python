# RAG vs Fine-Tuning vs Agents

When to use RAG (this project) vs other GenAI techniques.

---

## Quick answer

| Technique | Use when |
|-----------|----------|
| **RAG** (this project) | Q&A on your documents, need citations, data changes often |
| **Fine-tuning** | Fixed output format, domain tone, same task millions of times |
| **Agents** | Multi-step tasks, API calls, web search, tool use |

---

## RAG — what you built

**Pros:** Private data, updatable, cite sources, no training  
**Cons:** Retrieval quality depends on chunking; not for live API data alone

**Industry use:** Notion AI, Slack AI, support bots on help centers

---

## Fine-tuning

Train model weights on `(input, output)` pairs.

**Pros:** Cheaper inference at scale for narrow tasks  
**Cons:** Expensive to train; stale when facts change

**Use later if:** You need a custom price predictor or classifier on stable patterns.

---

## Agents

LLM loops with tools (search, calculator, booking API).

**Use later if:** You build on top of this RAG — e.g. agent retrieves policy (RAG) then calls HR API.

---

## Recommended path

```
1. RAG Assistant (rag-assistant)     ← document Q&A + citations
2. Support Agent (support-agent)     ← multi-agent + tools + escalation
3. Fine-tune for specific tasks      ← optional
4. Production orchestration (LangGraph, etc.) ← advanced
```

Full comparison table: see archived concepts in git history or extend this doc as you learn.

---

## Decision

**For company knowledge Q&A → RAG is the correct first production pattern.**

You made the right focus choosing one RAG project over eight scattered demos.
