"""Health check."""

from fastapi import APIRouter

from app.core.config import settings

router = APIRouter(tags=["Health"])


@router.get("/health")
def health() -> dict:
    return {"status": "ok", "app": settings.app_name}
