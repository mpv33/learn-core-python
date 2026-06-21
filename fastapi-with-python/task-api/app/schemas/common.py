"""Shared response schemas."""

from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str


class HealthResponse(BaseModel):
    status: str = Field(examples=["ok"])
    app: str
    version: str
    environment: str


class ReadinessResponse(BaseModel):
    """Readiness probe — checks DB connectivity."""

    status: str = Field(examples=["ready", "not_ready"])
    database: str = Field(examples=["connected", "disconnected"])
    app: str
    version: str


class PaginatedResponse(BaseModel):
    total: int
    skip: int
    limit: int
