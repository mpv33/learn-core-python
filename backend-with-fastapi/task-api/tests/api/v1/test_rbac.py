"""RBAC and admin endpoint tests."""

from fastapi.testclient import TestClient


def test_admin_can_list_users(client: TestClient, admin_headers: dict[str, str]) -> None:
    response = client.get("/api/v1/users", headers=admin_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["total"] >= 3


def test_regular_user_cannot_list_users(client: TestClient, auth_headers: dict[str, str]) -> None:
    response = client.get("/api/v1/users", headers=auth_headers)
    assert response.status_code == 403


def test_admin_can_see_all_tasks(
    client: TestClient,
    auth_headers: dict[str, str],
    admin_headers: dict[str, str],
) -> None:
    client.post("/api/v1/tasks", json={"title": "User task", "status": "pending"}, headers=auth_headers)

    response = client.get("/api/v1/tasks", headers=admin_headers)
    assert response.status_code == 200
    assert response.json()["total"] >= 1
