"""Application settings — loaded from environment variables and .env file."""

from functools import lru_cache
from typing import Literal

from pydantic import Field, PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central configuration for all environments (dev, staging, prod)."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # ── App ──────────────────────────────────────────────────────────────
    app_name: str = "Task API"
    app_version: str = "1.0.0"
    environment: Literal["development", "staging", "production"] = "development"
    debug: bool = False
    api_v1_prefix: str = "/api/v1"

    # ── Server ───────────────────────────────────────────────────────────
    host: str = "0.0.0.0"
    port: int = 8000

    # ── Database ─────────────────────────────────────────────────────────
    database_url: str = "sqlite:///./task_api.db"
    db_pool_size: int = 5
    db_max_overflow: int = 10
    db_pool_timeout: int = 30

    postgres_user: str = "taskapi"
    postgres_password: str = "taskapi"
    postgres_db: str = "taskapi"
    postgres_host: str = "db"
    postgres_port: int = 5432

    # ── Auth (JWT) ───────────────────────────────────────────────────────
    secret_key: str = Field(
        default="change-me-in-production-use-openssl-rand-hex-32",
        description="JWT signing secret — MUST override in production",
    )
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # ── Rate limiting ──────────────────────────────────────────────────────
    rate_limit_default: str = "100/minute"
    rate_limit_auth: str = "10/minute"
    rate_limit_register: str = "5/minute"

    # ── CORS ─────────────────────────────────────────────────────────────
    cors_origins: list[str] = Field(default=["http://localhost:3000", "http://127.0.0.1:3000"])

    # ── Logging ──────────────────────────────────────────────────────────
    log_level: str = "INFO"

    # ── Dev seed users ─────────────────────────────────────────────────────
    seed_admin_email: str = "admin@example.com"
    seed_admin_password: str = "admin123"
    seed_user_email: str = "user@example.com"
    seed_user_password: str = "user123"

    @computed_field  # type: ignore[prop-decorator]
    @property
    def is_production(self) -> bool:
        return self.environment == "production"

    @computed_field  # type: ignore[prop-decorator]
    @property
    def sqlalchemy_database_uri(self) -> str:
        return self.database_url

    @computed_field  # type: ignore[prop-decorator]
    @property
    def postgres_dsn(self) -> str:
        return str(
            PostgresDsn.build(
                scheme="postgresql+psycopg2",
                username=self.postgres_user,
                password=self.postgres_password,
                host=self.postgres_host,
                port=self.postgres_port,
                path=self.postgres_db,
            )
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
