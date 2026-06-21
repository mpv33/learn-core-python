"""Role-Based Access Control — roles, permissions, and role-permission mapping."""

import enum

from app.models.user import User, UserRole


class Permission(str, enum.Enum):
    """Fine-grained permissions mapped to roles."""

    TASK_READ = "task:read"
    TASK_WRITE = "task:write"
    TASK_DELETE = "task:delete"
    USER_READ = "user:read"
    USER_MANAGE = "user:manage"


ROLE_PERMISSIONS: dict[UserRole, set[Permission]] = {
    UserRole.USER: {
        Permission.TASK_READ,
        Permission.TASK_WRITE,
        Permission.TASK_DELETE,
    },
    UserRole.ADMIN: set(Permission),
}


def user_has_permission(user: User, permission: Permission) -> bool:
    """Return True if the user's role grants the permission."""
    return permission in ROLE_PERMISSIONS.get(user.role, set())


def is_admin(user: User) -> bool:
    """Return True when user has the admin role."""
    return user.role == UserRole.ADMIN
