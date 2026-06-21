"""Persist escalation tickets to JSON."""

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path

from app.core.config import settings


class TicketStore:
    """Simple file-backed ticket store for human handoff."""

    def __init__(self, data_dir: str | None = None) -> None:
        self._dir = Path(data_dir or settings.data_dir)
        self._dir.mkdir(parents=True, exist_ok=True)
        self._path = self._dir / "tickets.json"
        if not self._path.exists():
            self._path.write_text("[]", encoding="utf-8")

    def _read_all(self) -> list[dict]:
        return json.loads(self._path.read_text(encoding="utf-8"))

    def _write_all(self, tickets: list[dict]) -> None:
        self._path.write_text(json.dumps(tickets, indent=2), encoding="utf-8")

    def create(self, customer_message: str, reason: str, session_id: str) -> dict:
        ticket = {
            "ticket_id": f"TKT-{uuid.uuid4().hex[:8].upper()}",
            "session_id": session_id,
            "reason": reason,
            "customer_message": customer_message,
            "status": "open",
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        tickets = self._read_all()
        tickets.append(ticket)
        self._write_all(tickets)
        return ticket

    def list_open(self) -> list[dict]:
        return [t for t in self._read_all() if t.get("status") == "open"]
