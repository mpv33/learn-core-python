"""Search the support knowledge base (markdown sections)."""

import re
from pathlib import Path

from app.core.config import settings


class KnowledgeBase:
    """Load FAQ/policy markdown and retrieve relevant sections by keyword overlap."""

    def __init__(self, path: str | None = None) -> None:
        self._path = Path(path or settings.knowledge_base_path)
        self._sections = self._load_sections()

    def _load_sections(self) -> list[dict]:
        if not self._path.exists():
            return []
        text = self._path.read_text(encoding="utf-8")
        parts = re.split(r"(?=^## )", text, flags=re.MULTILINE)
        sections: list[dict] = []
        for part in parts:
            part = part.strip()
            if not part.startswith("## "):
                continue
            lines = part.splitlines()
            title = lines[0].lstrip("# ").strip()
            body = "\n".join(lines[1:]).strip()
            sections.append({"title": title, "body": body, "text": f"{title}\n{body}"})
        return sections

    def search(self, query: str, top_k: int = 3) -> list[dict]:
        tokens = set(re.findall(r"[a-z0-9]+", query.lower()))
        if not tokens:
            return self._sections[:top_k]

        scored: list[tuple[float, dict]] = []
        for section in self._sections:
            section_tokens = set(re.findall(r"[a-z0-9]+", section["text"].lower()))
            overlap = len(tokens & section_tokens)
            if overlap:
                scored.append((overlap / len(tokens), section))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [s for _, s in scored[:top_k]]
