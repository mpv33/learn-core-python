"""LLM chat completion — OpenAI or Ollama."""

import json
import re

import httpx
from openai import OpenAI

from app.core.config import settings


class LLMClient:
    """Generate chat completions."""

    def __init__(self) -> None:
        self._openai = OpenAI(api_key=settings.openai_api_key) if settings.openai_api_key else None

    def chat(self, system: str, user: str, temperature: float = 0.2) -> str:
        if settings.llm_provider == "ollama":
            return self._ollama_chat(system, user)
        if not self._openai:
            raise ValueError("OPENAI_API_KEY required when LLM_PROVIDER=openai")
        response = self._openai.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=temperature,
        )
        return response.choices[0].message.content or ""

    def chat_json(self, system: str, user: str) -> dict:
        """Ask the model for JSON; strips markdown fences if present."""
        raw = self.chat(system, user, temperature=0.0)
        cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", raw.strip(), flags=re.MULTILINE)
        return json.loads(cleaned)

    def _ollama_chat(self, system: str, user: str) -> str:
        url = f"{settings.ollama_base_url.rstrip('/')}/api/chat"
        payload = {
            "model": settings.ollama_chat_model,
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            "stream": False,
        }
        with httpx.Client(timeout=120.0) as client:
            resp = client.post(url, json=payload)
            resp.raise_for_status()
            return resp.json()["message"]["content"]
