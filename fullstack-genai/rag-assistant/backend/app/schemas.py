"""Pydantic schemas for API."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=2000)
    use_rag: bool = Field(default=True, description="True=RAG with docs, False=plain LLM")


class SourceChunk(BaseModel):
    text: str
    filename: str
    doc_id: str
    chunk_index: int
    score: float


class ChatResponse(BaseModel):
    answer: str
    sources: list[SourceChunk]
    mode: str


class IngestResponse(BaseModel):
    doc_id: str
    filename: str
    chunks_indexed: int
    characters: int


class DocumentInfo(BaseModel):
    doc_id: str
    filename: str
