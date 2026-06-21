"""
Task API — production-style FastAPI backend.

Package layout:
  app/api/       — HTTP layer (routers, dependencies)
  app/core/      — config, logging, exceptions
  app/db/        — database engine, sessions, migrations hook
  app/models/    — SQLAlchemy ORM models
  app/schemas/   — Pydantic request/response models
  app/services/  — business logic
  app/middleware/ — cross-cutting HTTP middleware
"""

__version__ = "1.0.0"
