"""Pydantic schemas for authentication and tokens."""

from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    """Request body for user registration."""

    email: EmailStr
    password: str = Field(..., min_length=6, max_length=128)
    full_name: str | None = Field(default=None, max_length=100)


class UserLogin(BaseModel):
    """Request body for login (OAuth2 password flow compatible)."""

    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    """JWT tokens returned after successful login."""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenRefresh(BaseModel):
    """Request body to exchange refresh token for new access token."""

    refresh_token: str
