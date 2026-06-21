"""SQLAlchemy engine, session factory, and database connectivity helpers."""

from collections.abc import Generator

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings
from app.core.logging import get_logger

logger = get_logger(__name__)

_connect_args = (
    {"check_same_thread": False}
    if settings.sqlalchemy_database_uri.startswith("sqlite")
    else {}
)

_engine_kwargs: dict = {
    "echo": settings.debug,
    "connect_args": _connect_args,
    "pool_pre_ping": True,
}

if not settings.sqlalchemy_database_uri.startswith("sqlite"):
    _engine_kwargs.update(
        pool_size=settings.db_pool_size,
        max_overflow=settings.db_max_overflow,
        pool_timeout=settings.db_pool_timeout,
    )

engine = create_engine(settings.sqlalchemy_database_uri, **_engine_kwargs)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    """Yield a database session per request; always close after response."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def check_db_connection() -> bool:
    """Ping the database — used by readiness probes."""
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception as exc:
        logger.error("Database connectivity check failed: %s", exc)
        return False
