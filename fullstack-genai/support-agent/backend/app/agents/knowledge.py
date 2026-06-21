"""Knowledge Agent — answer from support KB using retrieved sections."""

from app.agents.base import AgentResult, AgentStep
from app.services.knowledge_base import KnowledgeBase
from app.services.llm_client import LLMClient

SYSTEM = """You are a helpful customer support agent for AcmeShop.
Answer using ONLY the provided knowledge base excerpts.
If the answer is not in the excerpts, say you don't have that information and offer to escalate.
Be concise, friendly, and professional. Do not invent policies or order details."""


class KnowledgeAgent:
    """RAG-lite: retrieve KB sections, then generate an answer."""

    def __init__(
        self,
        llm: LLMClient | None = None,
        kb: KnowledgeBase | None = None,
    ) -> None:
        self._llm = llm or LLMClient()
        self._kb = kb or KnowledgeBase()

    def run(self, message: str, intent_hint: str = "general") -> tuple[AgentResult, AgentStep]:
        query = f"{intent_hint} {message}"
        sections = self._kb.search(query, top_k=3)

        if not sections:
            answer = (
                "I couldn't find relevant policy information. "
                "Would you like me to connect you with a human agent?"
            )
            step = AgentStep(agent="knowledge", action="search_kb", detail="no sections found")
            return AgentResult(agent="knowledge", answer=answer, sources=[]), step

        context = "\n\n---\n\n".join(s["text"] for s in sections)
        user_prompt = f"Knowledge base:\n{context}\n\nCustomer question:\n{message}"
        answer = self._llm.chat(SYSTEM, user_prompt)

        sources = [{"title": s["title"], "snippet": s["body"][:200]} for s in sections]
        step = AgentStep(
            agent="knowledge",
            action="search_kb",
            detail=f"retrieved {len(sections)} section(s)",
            output=", ".join(s["title"] for s in sections),
        )
        return AgentResult(agent="knowledge", answer=answer, sources=sources), step
