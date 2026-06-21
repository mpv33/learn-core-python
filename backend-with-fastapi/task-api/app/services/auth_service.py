"""Authentication and user management services."""

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.core.exceptions import ConflictError, NotFoundError, UnauthorizedError
from app.core.security import (
    create_access_token,
    create_refresh_token,
    hash_password,
    verify_access_token,
    verify_password,
)
from app.models.user import User, UserRole
from app.schemas.auth import UserLogin, UserRegister


class AuthService:
    """Handles registration, login, and token refresh."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def register(self, payload: UserRegister) -> User:
        """Create a new user with the default 'user' role."""
        existing = self.db.scalar(select(User).where(User.email == payload.email))
        if existing:
            raise ConflictError("Email already registered")

        user = User(
            email=payload.email,
            hashed_password=hash_password(payload.password),
            full_name=payload.full_name,
            role=UserRole.USER,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def authenticate(self, payload: UserLogin) -> User:
        """Validate credentials and return the user."""
        user = self.db.scalar(select(User).where(User.email == payload.email))
        if user is None or not verify_password(payload.password, user.hashed_password):
            raise UnauthorizedError("Invalid email or password")
        if not user.is_active:
            raise UnauthorizedError("Account is disabled")
        return user

    def create_tokens(self, user: User) -> dict[str, str]:
        """Return access + refresh JWT pair for a user."""
        claims = {"role": user.role.value}
        return {
            "access_token": create_access_token(str(user.id), extra_claims=claims),
            "refresh_token": create_refresh_token(str(user.id)),
            "token_type": "bearer",
        }

    def refresh_access_token(self, refresh_token: str) -> dict[str, str]:
        """Issue a new access token from a valid refresh token."""
        import jwt

        from app.core.config import settings

        try:
            payload = jwt.decode(refresh_token, settings.secret_key, algorithms=[settings.algorithm])
            if payload.get("type") != "refresh":
                raise UnauthorizedError("Invalid refresh token")
            user_id = int(payload["sub"])
        except (jwt.InvalidTokenError, KeyError, ValueError) as exc:
            raise UnauthorizedError("Invalid refresh token") from exc

        user = self.db.get(User, user_id)
        if user is None or not user.is_active:
            raise UnauthorizedError("User not found or inactive")

        return {
            "access_token": create_access_token(str(user.id), extra_claims={"role": user.role.value}),
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }

    def get_user_from_token(self, token: str) -> User:
        """Decode access token and load the user from DB."""
        try:
            payload = verify_access_token(token)
            user_id = int(payload["sub"])
        except Exception as exc:
            raise UnauthorizedError("Could not validate credentials") from exc

        user = self.db.get(User, user_id)
        if user is None or not user.is_active:
            raise UnauthorizedError("User not found or inactive")
        return user


class UserService:
    """Admin user management."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def list_users(self, *, skip: int = 0, limit: int = 100) -> tuple[list[User], int]:
        total = self.db.scalar(select(func.count()).select_from(User)) or 0
        users = self.db.scalars(select(User).order_by(User.id).offset(skip).limit(limit)).all()
        return list(users), total

    def get_user(self, user_id: int) -> User:
        user = self.db.get(User, user_id)
        if user is None:
            raise NotFoundError(f"User {user_id} not found")
        return user
