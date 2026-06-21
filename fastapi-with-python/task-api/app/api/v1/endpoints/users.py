"""User management endpoints — admin only."""

from fastapi import APIRouter, Depends, Query

from app.api.deps import RequireAdmin, get_user_service
from app.models.user import User
from app.schemas.user import UserListResponse, UserRead
from app.services.auth_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=UserListResponse)
def list_users(
    _admin: RequireAdmin,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=500),
    service: UserService = Depends(get_user_service),
) -> UserListResponse:
    """List all users (admin only)."""
    users, total = service.list_users(skip=skip, limit=limit)
    return UserListResponse(items=users, total=total, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserRead)
def get_user(
    user_id: int,
    _admin: RequireAdmin,
    service: UserService = Depends(get_user_service),
) -> User:
    """Get a user by ID (admin only)."""
    return service.get_user(user_id)
