"""Mock order lookup for the Order Agent."""

import json
import re
from pathlib import Path

from app.core.config import settings


class OrderStore:
    """Read-only access to sample order records."""

    def __init__(self, path: str | None = None) -> None:
        self._path = Path(path or settings.orders_path)
        self._orders = self._load()

    def _load(self) -> dict[str, dict]:
        if not self._path.exists():
            return {}
        data = json.loads(self._path.read_text(encoding="utf-8"))
        return {o["order_id"].upper(): o for o in data.get("orders", [])}

    @staticmethod
    def extract_order_id(text: str) -> str | None:
        match = re.search(r"\b(ORD-\d{4,})\b", text.upper())
        return match.group(1) if match else None

    def get(self, order_id: str) -> dict | None:
        return self._orders.get(order_id.upper())

    def list_ids(self) -> list[str]:
        return sorted(self._orders.keys())
