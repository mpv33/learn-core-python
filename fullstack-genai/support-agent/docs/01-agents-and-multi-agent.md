# Agents & Multi-Agent Systems

What agents are, how they differ from RAG, and why support desks use multi-agent orchestration.

---

## What is an AI agent?

An **agent** is an LLM that can **decide and act** — not just answer from context, but:

- Classify intent
- Call tools (APIs, databases)
- Route to specialists
- Loop until the task is done

```
User message → LLM + tools → action → observation → next step → final answer
```

**RAG** retrieves documents and answers. **Agents** choose *what to do* with each message.

---

## Single agent vs multi-agent

| Pattern | When to use |
|---------|-------------|
| **Single agent + tools** | One generalist with function calling (search, calculator, CRM) |
| **Multi-agent** | Distinct roles, clearer prompts, easier to test and extend |

**Multi-agent support** (this project):

```
                    ┌─────────────┐
                    │  Supervisor │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
         ┌────────┐  ┌──────────┐  ┌────────────┐
         │ Triage │  │ Knowledge│  │   Orders   │
         └────────┘  └──────────┘  └────────────┘
                           │
                           ▼
                    ┌─────────────┐
                    │ Escalation  │
                    └─────────────┘
```

Each agent has a **narrow job** and **focused system prompt** — better accuracy than one mega-prompt.

---

## Customer support agent pattern

Industry pattern for support bots:

1. **Triage** — intent + urgency + entities (order ID)
2. **Self-service** — KB / FAQ for policy questions
3. **Transactional** — order lookup, refund status (API tools)
4. **Escalation** — ticket when confidence is low or user asks for human

This maps directly to the agents in `support-agent/`.

---

## Tools vs agents

| Concept | Example in this repo |
|---------|---------------------|
| **Tool** | `OrderStore.get("ORD-1001")` — deterministic lookup |
| **Agent** | Order Agent — LLM interprets order JSON + customer tone |
| **Orchestrator** | Supervisor — picks which agent runs |

Agents *use* tools; orchestrators *coordinate* agents.

---

## When to combine RAG + agents

After [rag-assistant](../../rag-assistant/):

- **Knowledge Agent** = RAG-lite (retrieve KB sections → generate answer)
- **Order Agent** = tool use (structured data, not documents)
- **Supervisor** = router + response polish

Production systems often stack: RAG for docs + agents for APIs + escalation for edge cases.

---

## Common mistakes

1. **One agent does everything** — hard to debug, prompt bloat
2. **No escalation path** — users stuck when bot fails
3. **No trace/logging** — can't explain why a route was chosen
4. **Inventing order/policy data** — always ground in KB or API results

---

## Next steps

1. Read [02-architecture.md](02-architecture.md)
2. Run `support-agent` and expand the agent trace in the UI
3. Add a **Billing Agent** that calls a mock payments API
4. Replace keyword KB search with embeddings (reuse patterns from rag-assistant)
