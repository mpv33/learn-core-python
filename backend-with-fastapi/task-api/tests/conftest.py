"""Shared pytest fixtures for API integration tests."""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.security import hash_password
from app.db.base import Base
from app.db.session import get_db
from app.main import app
from app.models.user import User, UserRole

TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


def _seed_test_users(db) -> dict[str, User]:
    users = {
        "admin": User(
            email="admin@test.com",
            hashed_password=hash_password("admin123"),
            role=UserRole.ADMIN,
            full_name="Test Admin",
        ),
        "user": User(
            email="user@test.com",
            hashed_password=hash_password("user123"),
            role=UserRole.USER,
            full_name="Test User",
        ),
        "other": User(
            email="other@test.com",
            hashed_password=hash_password("other123"),
            role=UserRole.USER,
            full_name="Other User",
        ),
    }
    for user in users.values():
        db.add(user)
    db.commit()
    for user in users.values():
        db.refresh(user)
    return users


@pytest.fixture(autouse=True)
def setup_database():
    from app.core.limiter import limiter

    limiter.enabled = False  # disable rate limits during tests
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db

    db = TestingSessionLocal()
    try:
        users = _seed_test_users(db)
        pytest.test_users = users  # type: ignore[attr-defined]
    finally:
        db.close()

    yield
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def _login(client: TestClient, email: str, password: str) -> str:
    response = client.post(
        "/api/v1/auth/login",
        data={"username": email, "password": password},
    )
    assert response.status_code == 200, response.text
    return response.json()["access_token"]


@pytest.fixture
def admin_token(client: TestClient) -> str:
    return _login(client, "admin@test.com", "admin123")


@pytest.fixture
def user_token(client: TestClient) -> str:
    return _login(client, "user@test.com", "user123")


@pytest.fixture
def other_user_token(client: TestClient) -> str:
    return _login(client, "other@test.com", "other123")


@pytest.fixture
def auth_headers(user_token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {user_token}"}


@pytest.fixture
def admin_headers(admin_token: str) -> dict[str, str]:
    return {"Authorization": f"Bearer {admin_token}"}
