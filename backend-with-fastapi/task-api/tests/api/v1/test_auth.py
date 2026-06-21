"""Authentication endpoint tests."""

from fastapi.testclient import TestClient


def test_register_and_login(client: TestClient) -> None:
    register = client.post(
        "/api/v1/auth/register",
        json={"email": "new@test.com", "password": "secret123", "full_name": "New User"},
    )
    assert register.status_code == 201
    assert register.json()["email"] == "new@test.com"
    assert register.json()["role"] == "user"

    login = client.post(
        "/api/v1/auth/login",
        data={"username": "new@test.com", "password": "secret123"},
    )
    assert login.status_code == 200
    tokens = login.json()
    assert "access_token" in tokens
    assert "refresh_token" in tokens


def test_login_invalid_credentials(client: TestClient) -> None:
    response = client.post(
        "/api/v1/auth/login",
        data={"username": "user@test.com", "password": "wrongpassword"},
    )
    assert response.status_code == 401


def test_me_endpoint(client: TestClient, auth_headers: dict[str, str]) -> None:
    response = client.get("/api/v1/auth/me", headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["email"] == "user@test.com"


def test_refresh_token(client: TestClient) -> None:
    login = client.post(
        "/api/v1/auth/login",
        data={"username": "user@test.com", "password": "user123"},
    )
    refresh_token = login.json()["refresh_token"]

    response = client.post("/api/v1/auth/refresh", json={"refresh_token": refresh_token})
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_register_duplicate_email(client: TestClient) -> None:
    response = client.post(
        "/api/v1/auth/register",
        json={"email": "user@test.com", "password": "secret123"},
    )
    assert response.status_code == 409
