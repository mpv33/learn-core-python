"""Request/response models."""

from pydantic import BaseModel, Field


class AgentTraceStep(BaseModel):
    agent: str
    action: str
    detail: str
    output: str = ""


class SourceSnippet(BaseModel):
    title: str
    snippet: str


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)
    session_id: str | None = None


class ChatResponse(BaseModel):
    answer: str
    session_id: str
    intent: str
    confidence: float
    agents_used: list[str]
    sources: list[SourceSnippet]
    trace: list[AgentTraceStep]
    metadata: dict = Field(default_factory=dict)


class TicketInfo(BaseModel):
    ticket_id: str
    session_id: str
    reason: str
    customer_message: str
    status: str
    created_at: str
