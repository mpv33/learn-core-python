"""Escalation Agent — create a ticket for human handoff."""

from app.agents.base import AgentResult, AgentStep
from app.services.ticket_store import TicketStore


class EscalationAgent:
    """Open a support ticket when automation cannot resolve the issue."""

    def __init__(self, store: TicketStore | None = None) -> None:
        self._store = store or TicketStore()

    def run(self, message: str, session_id: str, reason: str = "customer_request") -> tuple[AgentResult, AgentStep]:
        ticket = self._store.create(message, reason, session_id)
        answer = (
            f"I've escalated this to our support team. Your ticket ID is **{ticket['ticket_id']}**. "
            "A human agent will follow up within 24 hours. Is there anything else I can help with?"
        )
        step = AgentStep(
            agent="escalation",
            action="create_ticket",
            detail=f"ticket={ticket['ticket_id']}, reason={reason}",
        )
        return (
            AgentResult(
                agent="escalation",
                answer=answer,
                metadata={"ticket_id": ticket["ticket_id"], "reason": reason},
            ),
            step,
        )
