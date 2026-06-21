"""FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import chat, health, tickets
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    description="Customer support multi-agent system — triage, knowledge, orders, escalation.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, prefix="/api/v1")
app.include_router(chat.router, prefix="/api/v1")
app.include_router(tickets.router, prefix="/api/v1")


@app.get("/")
def root() -> dict:
    return {"message": "Support Agent API", "docs": "/docs"}
