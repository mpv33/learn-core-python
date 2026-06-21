# Architecture — Support Agent

How the customer support multi-agent system is structured.

---

## High-level flow

```
┌──────────────┐     POST /api/v1/chat      ┌─────────────────────┐
│  Next.js UI  │ ─────────────────────────► │  SupportOrchestrator │
│  :3001       │ ◄───────────────────────── │  (Supervisor)        │
└──────────────┘     answer + agent trace   └──────────┬──────────┘
                                                        │
                        ┌───────────────────────────────┼───────────────────────────────┐
                        ▼                               ▼                               ▼
                 ┌─────────────┐                ┌─────────────┐                ┌──────────────┐
                 │ TriageAgent │                │KnowledgeAgent│               │  OrderAgent  │
                 └─────────────┘                └──────┬──────┘                └──────┬───────┘
                                                        │                               │
                                                        ▼                               ▼
                                                 knowledge-base.md                  orders.json
```

---

## Backend layout

```
support-agent/backend/app/
├── main.py
├── core/config.py
├── schemas.py
├── api/routes/
│   ├── chat.py          # POST /chat
│   ├── tickets.py       # GET /tickets
│   └── health.py
├── agents/
│   ├── triage.py        # Intent classification
│   ├── knowledge.py     # KB-grounded answers
│   ├── orders.py        # Order status
│   └── escalation.py    # Ticket creation
└── services/
    ├── orchestrator.py  # Multi-agent workflow
    ├── llm_client.py
    ├── knowledge_base.py
    ├── order_store.py
    └── ticket_store.py
```

---

## Routing rules (Supervisor)

| Intent | Route to | Data source |
|--------|----------|-------------|
| `order_status` | Order Agent | `sample-data/orders.json` |
| `returns`, `billing`, `shipping`, `technical`, `general` | Knowledge Agent | `sample-data/knowledge-base.md` |
| `human_handoff` or confidence &lt; 0.45 | Escalation Agent | `backend/data/tickets.json` |

After specialist response, Supervisor **polishes** tone via a final LLM call.

---

## Frontend

- Chat panel with suggested prompts
- **Agent trace** expandable on each reply (intent, confidence, steps)
- Sidebar lists open escalation tickets

---

## Ports & env

| Service | Port |
|---------|------|
| Frontend | 3001 |
| Backend | 8001 |

Copy `backend/.env.example` → `backend/.env` and set `OPENAI_API_KEY`.

Paths `KNOWLEDGE_BASE_PATH` and `ORDERS_PATH` default to `../sample-data/` relative to the backend directory.

---

## Extending the system

1. **New specialist** — add `agents/billing.py`, register in `orchestrator.py`
2. **Real CRM** — replace `TicketStore` with Zendesk/Intercom API
3. **Better retrieval** — swap `KnowledgeBase.search` for embedding search from rag-assistant
4. **Streaming** — SSE from `/chat` for token-by-token UI
