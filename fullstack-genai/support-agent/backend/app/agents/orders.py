"""Order Agent — look up order status from mock data."""

from app.agents.base import AgentResult, AgentStep
from app.services.llm_client import LLMClient
from app.services.order_store import OrderStore

SYSTEM = """You are the Order Status agent for AcmeShop.
Use ONLY the order JSON provided. Summarize status clearly for the customer.
If order data is missing a field, say so — do not guess tracking numbers or dates."""


class OrderAgent:
    """Fetch order details and explain status to the customer."""

    def __init__(
        self,
        llm: LLMClient | None = None,
        store: OrderStore | None = None,
    ) -> None:
        self._llm = llm or LLMClient()
        self._store = store or OrderStore()

    def run(self, message: str, order_id: str | None = None) -> tuple[AgentResult, AgentStep]:
        oid = order_id or self._store.extract_order_id(message)

        if not oid:
            sample = ", ".join(self._store.list_ids()[:3]) or "ORD-1001"
            answer = (
                f"I can look up your order — please share your order ID (e.g. {sample}). "
                "You'll find it in your confirmation email."
            )
            step = AgentStep(agent="orders", action="request_order_id", detail="no order_id found")
            return AgentResult(agent="orders", answer=answer, metadata={"needs_order_id": True}), step

        order = self._store.get(oid)
        if not order:
            answer = (
                f"I couldn't find order **{oid}**. Please double-check the ID or contact billing "
                "if you were charged recently."
            )
            step = AgentStep(agent="orders", action="lookup_order", detail=f"{oid} not found")
            return AgentResult(agent="orders", answer=answer, metadata={"order_id": oid}), step

        user_prompt = f"Order data:\n{order}\n\nCustomer message:\n{message}"
        answer = self._llm.chat(SYSTEM, user_prompt)

        step = AgentStep(
            agent="orders",
            action="lookup_order",
            detail=f"found {oid} — status={order.get('status')}",
        )
        return (
            AgentResult(
                agent="orders",
                answer=answer,
                sources=[{"title": oid, "snippet": str(order)}],
                metadata={"order_id": oid, "status": order.get("status")},
            ),
            step,
        )
