"""Pydantic schemas for insert User resource."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr

from app.models.user import UserRole


class UserRead(BaseModel):
    """Public user profile returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    full_name: str | None
    role: UserRole
    is_active: bool
    created_at: datetime


class UserListResponse(BaseModel):
    """Paginated list of users (admin only)."""

    items: list[UserRead]
    total: int
    skip: int
    limit: int
