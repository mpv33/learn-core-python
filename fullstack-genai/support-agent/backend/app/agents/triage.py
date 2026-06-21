"""Triage Agent — classify customer intent."""

import re

from app.agents.base import AgentResult, AgentStep
from app.services.llm_client import LLMClient

INTENTS = (
    "order_status",
    "returns",
    "billing",
    "shipping",
    "technical",
    "general",
    "human_handoff",
)

SYSTEM = """You are a customer support triage agent.
Classify the customer message into exactly one intent:
order_status, returns, billing, shipping, technical, general, human_handoff

Use human_handoff when the customer explicitly asks for a person or is angry/frustrated.

Respond with JSON only:
{"intent": "...", "confidence": 0.0-1.0, "summary": "one line", "order_id": "ORD-XXXX or null"}
"""


class TriageAgent:
    """Route incoming messages by intent."""

    def __init__(self, llm: LLMClient | None = None) -> None:
        self._llm = llm or LLMClient()

    def run(self, message: str) -> tuple[AgentResult, AgentStep]:
        try:
            data = self._llm.chat_json(SYSTEM, message)
            intent = data.get("intent", "general")
            if intent not in INTENTS:
                intent = "general"
            confidence = float(data.get("confidence", 0.7))
            order_id = data.get("order_id")
        except (ValueError, KeyError, TypeError):
            intent, confidence, order_id = self._keyword_fallback(message)
            data = {"intent": intent, "confidence": confidence, "summary": message[:80]}

        step = AgentStep(
            agent="triage",
            action="classify_intent",
            detail=f"intent={intent}, confidence={confidence:.2f}",
            output=data.get("summary", ""),
        )
        result = AgentResult(
            agent="triage",
            answer="",
            metadata={"intent": intent, "confidence": confidence, "order_id": order_id},
        )
        return result, step

    @staticmethod
    def _keyword_fallback(message: str) -> tuple[str, float, str | None]:
        text = message.lower()
        match = re.search(r"\b(ORD-\d{4,})\b", message.upper())
        order_id = match.group(1) if match else None

        if any(w in text for w in ("human", "manager", "speak to someone", "real person")):
            return "human_handoff", 0.9, order_id
        if any(w in text for w in ("order", "tracking", "where is my", "delivery status")):
            return "order_status", 0.75, order_id
        if any(w in text for w in ("refund", "return", "exchange", "cancel order")):
            return "returns", 0.75, order_id
        if any(w in text for w in ("charge", "invoice", "payment", "billing", "receipt")):
            return "billing", 0.75, order_id
        if any(w in text for w in ("shipping", "ship", "delayed", "lost package")):
            return "shipping", 0.75, order_id
        if any(w in text for w in ("login", "password", "app", "error", "bug", "not working")):
            return "technical", 0.7, order_id
        return "general", 0.6, order_id
