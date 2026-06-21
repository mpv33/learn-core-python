# Support Agent

**Phase 4 capstone** — [GenAI Full-Stack Developer Track](../../README.md)

Customer support **multi-agent system** — one app combining a support chatbot with specialist agents orchestrated by a supervisor.

**Stack:** Next.js 15 + FastAPI + OpenAI (or Ollama)

---

## What you build

A realistic **AcmeShop support desk** where customer messages flow through multiple agents:

```
Customer message
    → Triage Agent (classify intent)
    → Supervisor (route)
    → Knowledge | Orders | Escalation agent
    → Supervisor (polish reply)
    → Customer-facing answer + agent trace
```

| Agent | Role |
|-------|------|
| **Triage** | Classify intent (returns, billing, order status, …) |
| **Knowledge** | Answer from support KB (returns, shipping, billing policies) |
| **Orders** | Look up mock order data (`ORD-1001`, …) |
| **Escalation** | Create human handoff tickets |
| **Supervisor** | Route + polish final response |

---

## Quick start

```bash
cp backend/.env.example backend/.env    # add OPENAI_API_KEY
make install
make dev
```

- **Support UI:** http://localhost:3001
- **API docs:** http://127.0.0.1:8001/docs

Uses ports **3001 / 8001** so it can run alongside `rag-assistant`.

---

## Try these prompts

| Prompt | Expected routing |
|--------|------------------|
| "What's your refund policy?" | triage → knowledge |
| "Where is order ORD-1001?" | triage → orders |
| "I was charged twice" | triage → knowledge (billing) |
| "I want to speak to a human" | triage → escalation |

Expand the **Agent trace** panel on each reply to see the multi-agent workflow.

---

## Learning docs

**Start here:** [LEARNING-GUIDE.md](LEARNING-GUIDE.md)

| Doc | Topic |
|-----|--------|
| [01-agents-and-multi-agent](docs/01-agents-and-multi-agent.md) | Agents vs RAG, multi-agent patterns |
| [02-architecture](docs/02-architecture.md) | System design |
| [03-setup-and-run](docs/03-setup-and-run.md) | Install & troubleshooting |

---

## Project layout

```
support-agent/
├── LEARNING-GUIDE.md
├── docs/
├── sample-data/
│   ├── knowledge-base.md    # Support policies
│   └── orders.json          # Mock orders
├── backend/
│   ├── app/agents/          # Triage, Knowledge, Orders, Escalation
│   ├── app/services/        # Orchestrator, LLM, stores
│   └── tests/
├── frontend/                # Chat UI + agent trace
└── Makefile
```
