"""RAG chat endpoint."""

from fastapi import APIRouter, HTTPException

from app.schemas import ChatRequest, ChatResponse, SourceChunk
from app.services.rag_service import RAGService

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    """Ask a question — RAG mode uses indexed documents; plain mode uses LLM only."""
    try:
        result = RAGService().query(payload.question, use_rag=payload.use_rag)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return ChatResponse(
        answer=result["answer"],
        sources=[SourceChunk(**s) for s in result["sources"]],
        mode=result["mode"],
    )
