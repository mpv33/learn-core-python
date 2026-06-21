"""Multi-agent orchestrator — supervisor routes to specialist agents."""

import uuid

from app.agents.base import AgentStep
from app.agents.escalation import EscalationAgent
from app.agents.knowledge import KnowledgeAgent
from app.agents.orders import OrderAgent
from app.agents.triage import TriageAgent
from app.services.llm_client import LLMClient
from app.services.order_store import OrderStore

SUPERVISOR_SYSTEM = """You are the Support Supervisor at AcmeShop.
You receive a customer message and a specialist agent's draft reply.
Polish the draft into a final customer-facing message: friendly, concise, accurate.
Do not add facts that aren't in the draft. Keep ticket IDs and order IDs unchanged."""


class SupportOrchestrator:
    """
    Multi-agent workflow:
    1. Triage Agent classifies intent
    2. Supervisor routes to Knowledge, Order, or Escalation agent
    3. Supervisor polishes the specialist reply
    """

    CONFIDENCE_THRESHOLD = 0.45

    def __init__(self) -> None:
        self._llm = LLMClient()
        self._triage = TriageAgent(self._llm)
        self._knowledge = KnowledgeAgent(self._llm)
        self._orders = OrderAgent(self._llm)
        self._escalation = EscalationAgent()
        self._order_store = OrderStore()

    def handle(self, message: str, session_id: str | None = None) -> dict:
        sid = session_id or str(uuid.uuid4())
        trace: list[AgentStep] = []

        triage_result, triage_step = self._triage.run(message)
        trace.append(triage_step)
        intent = triage_result.metadata["intent"]
        confidence = triage_result.metadata["confidence"]
        order_id = triage_result.metadata.get("order_id") or self._order_store.extract_order_id(message)

        agents_used: list[str] = ["triage", "supervisor"]

        if intent == "human_handoff" or confidence < self.CONFIDENCE_THRESHOLD:
            agent_result, step = self._escalation.run(
                message, sid, reason="low_confidence" if confidence < self.CONFIDENCE_THRESHOLD else "human_request"
            )
            agents_used.append("escalation")
        elif intent == "order_status":
            agent_result, step = self._orders.run(message, order_id)
            agents_used.append("orders")
        else:
            agent_result, step = self._knowledge.run(message, intent_hint=intent)
            agents_used.append("knowledge")

        trace.append(step)

        if agent_result.agent != "escalation" and self._should_escalate(message, agent_result.answer):
            esc_result, esc_step = self._escalation.run(message, sid, reason="agent_recommended_escalation")
            trace.append(esc_step)
            agents_used.append("escalation")
            agent_result = esc_result

        final_answer = self._polish(message, agent_result.answer)

        return {
            "answer": final_answer,
            "session_id": sid,
            "intent": intent,
            "confidence": confidence,
            "agents_used": agents_used,
            "sources": agent_result.sources,
            "metadata": agent_result.metadata,
            "trace": [
                {"agent": s.agent, "action": s.action, "detail": s.detail, "output": s.output}
                for s in trace
            ],
        }

    def _polish(self, message: str, draft: str) -> str:
        try:
            return self._llm.chat(
                SUPERVISOR_SYSTEM,
                f"Customer message:\n{message}\n\nSpecialist draft:\n{draft}",
            )
        except ValueError:
            return draft

    @staticmethod
    def _should_escalate(message: str, answer: str) -> bool:
        text = (message + " " + answer).lower()
        return any(p in text for p in ("speak to human", "talk to a person", "escalate", "human agent"))
