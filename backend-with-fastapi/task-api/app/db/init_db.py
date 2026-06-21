"""Database initialization and dev seed data."""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.logging import get_logger
from app.core.security import hash_password
from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.models.user import User, UserRole

logger = get_logger(__name__)


def init_db() -> None:
    """Create all tables (dev fallback — use Alembic migrations in production)."""
    import app.models  # noqa: F401

    Base.metadata.create_all(bind=engine)
    _seed_dev_users()


def _seed_dev_users() -> None:
    """Create default admin and user accounts in development."""
    if settings.environment != "development":
        return

    db: Session = SessionLocal()
    try:
        seeds = [
            (settings.seed_admin_email, settings.seed_admin_password, UserRole.ADMIN, "Admin User"),
            (settings.seed_user_email, settings.seed_user_password, UserRole.USER, "Regular User"),
        ]
        for email, password, role, full_name in seeds:
            exists = db.scalar(select(User).where(User.email == email))
            if exists:
                continue
            db.add(
                User(
                    email=email,
                    hashed_password=hash_password(password),
                    role=role,
                    full_name=full_name,
                )
            )
            logger.info("Seeded %s account: %s", role.value, email)
        db.commit()
    finally:
        db.close()
