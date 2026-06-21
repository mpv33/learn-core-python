"""Shared FastAPI dependencies — DB, auth, RBAC, services."""

from collections.abc import Callable
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.exceptions import ForbiddenError, UnauthorizedError
from app.core.rbac import Permission, user_has_permission
from app.db.session import get_db
from app.models.user import User, UserRole
from app.services.auth_service import AuthService, UserService
from app.services.task_service import TaskService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(db)


def get_user_service(db: Session = Depends(get_db)) -> UserService:
    return UserService(db)


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    auth_service: AuthService = Depends(get_auth_service),
) -> User:
    """Resolve the authenticated user from the Bearer JWT."""
    return auth_service.get_user_from_token(token)


def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)],
) -> User:
    if not current_user.is_active:
        raise UnauthorizedError("Inactive user")
    return current_user


def get_task_service(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user),
) -> TaskService:
    return TaskService(db, current_user)


def require_permission(permission: Permission) -> Callable:
    """Dependency factory — user must have the given RBAC permission."""

    def checker(current_user: Annotated[User, Depends(get_current_active_user)]) -> User:
        if not user_has_permission(current_user, permission):
            raise ForbiddenError(f"Permission denied: {permission.value}")
        return current_user

    return checker


def require_roles(*roles: UserRole) -> Callable:
    """Dependency factory — user must have one of the given roles."""

    def checker(current_user: Annotated[User, Depends(get_current_active_user)]) -> User:
        if current_user.role not in roles:
            raise ForbiddenError(f"Requires role: {', '.join(r.value for r in roles)}")
        return current_user

    return checker


RequireAdmin = Annotated[User, Depends(require_roles(UserRole.ADMIN))]

__all__ = [
    "RequireAdmin",
    "get_auth_service",
    "get_current_active_user",
    "get_current_user",
    "get_db",
    "get_task_service",
    "get_user_service",
    "oauth2_scheme",
    "require_permission",
    "require_roles",
]
