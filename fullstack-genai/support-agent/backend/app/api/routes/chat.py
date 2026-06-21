"""Support chat — multi-agent orchestration."""

from fastapi import APIRouter, HTTPException

from app.schemas import AgentTraceStep, ChatRequest, ChatResponse, SourceSnippet
from app.services.orchestrator import SupportOrchestrator

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    """Send a customer message; supervisor routes to specialist agents."""
    try:
        result = SupportOrchestrator().handle(payload.message, payload.session_id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return ChatResponse(
        answer=result["answer"],
        session_id=result["session_id"],
        intent=result["intent"],
        confidence=result["confidence"],
        agents_used=result["agents_used"],
        sources=[SourceSnippet(**s) for s in result["sources"]],
        trace=[AgentTraceStep(**t) for t in result["trace"]],
        metadata=result["metadata"],
    )
