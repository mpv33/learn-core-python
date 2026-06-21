"""Authentication endpoints — register, login, refresh, profile."""

from typing import Annotated

from fastapi import APIRouter, Depends, Request, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.deps import get_auth_service, get_current_active_user
from app.core.config import settings
from app.core.limiter import limiter
from app.models.user import User
from app.schemas.auth import TokenRefresh, TokenResponse, UserRegister
from app.schemas.user import UserRead
from app.services.auth_service import AuthService

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
@limiter.limit(settings.rate_limit_register)
def register(
    request: Request,
    payload: UserRegister,
    auth_service: AuthService = Depends(get_auth_service),
) -> User:
    """Register a new user account (default role: user)."""
    return auth_service.register(payload)


@router.post("/login", response_model=TokenResponse)
@limiter.limit(settings.rate_limit_auth)
def login(
    request: Request,
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_service: AuthService = Depends(get_auth_service),
) -> TokenResponse:
    """
    Login with email + password (OAuth2 form).

    Swagger: use **username** field for email address.
    """
    from app.schemas.auth import UserLogin

    user = auth_service.authenticate(UserLogin(email=form_data.username, password=form_data.password))
    tokens = auth_service.create_tokens(user)
    return TokenResponse(**tokens)


@router.post("/refresh", response_model=TokenResponse)
@limiter.limit(settings.rate_limit_auth)
def refresh_token(
    request: Request,
    payload: TokenRefresh,
    auth_service: AuthService = Depends(get_auth_service),
) -> TokenResponse:
    """Exchange a refresh token for a new access token."""
    tokens = auth_service.refresh_access_token(payload.refresh_token)
    return TokenResponse(**tokens)


@router.get("/me", response_model=UserRead)
def read_current_user(current_user: Annotated[User, Depends(get_current_active_user)]) -> User:
    """Return the currently authenticated user's profile."""
    return current_user
