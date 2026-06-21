"""Health and readiness endpoints for monitoring and orchestration."""

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.db.session import check_db_connection
from app.schemas.common import HealthResponse, ReadinessResponse

router = APIRouter(tags=["Health"])


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Liveness probe — process is running (no DB check)."""
    return HealthResponse(
        status="ok",
        app=settings.app_name,
        version=settings.app_version,
        environment=settings.environment,
    )


@router.get("/ready", response_model=ReadinessResponse)
def readiness_check() -> ReadinessResponse | JSONResponse:
    """Readiness probe — verifies database connectivity."""
    db_ok = check_db_connection()
    response = ReadinessResponse(
        status="ready" if db_ok else "not_ready",
        database="connected" if db_ok else "disconnected",
        app=settings.app_name,
        version=settings.app_version,
    )
    if not db_ok:
        return JSONResponse(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, content=response.model_dump())
    return response
