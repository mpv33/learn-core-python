"""Health check."""

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["Health"])


@router.get("")
def health() -> dict:
    return {"status": "ok"}
