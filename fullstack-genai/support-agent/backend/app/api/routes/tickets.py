"""List escalation tickets."""

from fastapi import APIRouter

from app.schemas import TicketInfo
from app.services.ticket_store import TicketStore

router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.get("", response_model=list[TicketInfo])
def list_tickets() -> list[TicketInfo]:
    """Open tickets created by the Escalation Agent."""
    return [TicketInfo(**t) for t in TicketStore().list_open()]
