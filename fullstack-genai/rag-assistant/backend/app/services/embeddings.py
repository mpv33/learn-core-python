"""Generate vector embeddings via OpenAI or Ollama."""

import httpx
from openai import OpenAI

from app.core.config import settings


class EmbeddingService:
    """Create embeddings for text chunks and queries."""

    def __init__(self) -> None:
        self._openai = OpenAI(api_key=settings.openai_api_key) if settings.openai_api_key else None

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Return embedding vectors for a list of texts."""
        if not texts:
            return []
        if settings.llm_provider == "ollama":
            return [self._ollama_embed(t) for t in texts]
        if not self._openai:
            raise ValueError("OPENAI_API_KEY required when LLM_PROVIDER=openai")
        response = self._openai.embeddings.create(model=settings.embedding_model, input=texts)
        return [item.embedding for item in response.data]

    def _ollama_embed(self, text: str) -> list[float]:
        url = f"{settings.ollama_base_url.rstrip('/')}/api/embeddings"
        with httpx.Client(timeout=60.0) as client:
            resp = client.post(url, json={"model": settings.ollama_embed_model, "prompt": text})
            resp.raise_for_status()
            return resp.json()["embedding"]
