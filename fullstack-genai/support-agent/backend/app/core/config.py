"""Application settings."""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "Support Agent"
    environment: str = "development"
    debug: bool = True

    llm_provider: Literal["openai", "ollama"] = "openai"
    openai_api_key: str = ""
    openai_model: str = "gpt-4o-mini"

    ollama_base_url: str = "http://localhost:11434"
    ollama_chat_model: str = "llama3.1:8b"

    knowledge_base_path: str = "../sample-data/knowledge-base.md"
    orders_path: str = "../sample-data/orders.json"
    data_dir: str = "./data"

    cors_origins: list[str] = Field(default=["http://localhost:3001"])


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
