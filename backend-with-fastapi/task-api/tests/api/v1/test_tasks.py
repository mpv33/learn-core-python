"""Task API v1 endpoint integration tests."""

from fastapi.testclient import TestClient


def test_health_check(client: TestClient) -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_readiness_check(client: TestClient) -> None:
    response = client.get("/api/v1/ready")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ready"
    assert data["database"] == "connected"


def test_tasks_require_auth(client: TestClient) -> None:
    response = client.get("/api/v1/tasks")
    assert response.status_code == 401


def test_create_and_get_task(client: TestClient, auth_headers: dict[str, str]) -> None:
    create_response = client.post(
        "/api/v1/tasks",
        json={"title": "Write tests", "description": "pytest", "status": "pending"},
        headers=auth_headers,
    )
    assert create_response.status_code == 201
    created = create_response.json()
    assert created["title"] == "Write tests"

    get_response = client.get(f"/api/v1/tasks/{created['id']}", headers=auth_headers)
    assert get_response.status_code == 200


def test_list_tasks_pagination(client: TestClient, auth_headers: dict[str, str]) -> None:
    client.post("/api/v1/tasks", json={"title": "A", "status": "pending"}, headers=auth_headers)
    client.post("/api/v1/tasks", json={"title": "B", "status": "done"}, headers=auth_headers)

    response = client.get("/api/v1/tasks", params={"status": "done"}, headers=auth_headers)
    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 1


def test_update_and_delete_task(client: TestClient, auth_headers: dict[str, str]) -> None:
    created = client.post(
        "/api/v1/tasks",
        json={"title": "Temp", "status": "pending"},
        headers=auth_headers,
    ).json()

    patch = client.patch(
        f"/api/v1/tasks/{created['id']}",
        json={"status": "in_progress"},
        headers=auth_headers,
    )
    assert patch.status_code == 200

    assert client.delete(f"/api/v1/tasks/{created['id']}", headers=auth_headers).status_code == 204


def test_user_cannot_access_other_users_task(
    client: TestClient,
    auth_headers: dict[str, str],
    other_user_token: str,
) -> None:
    created = client.post(
        "/api/v1/tasks",
        json={"title": "Private", "status": "pending"},
        headers=auth_headers,
    ).json()

    other_headers = {"Authorization": f"Bearer {other_user_token}"}
    response = client.get(f"/api/v1/tasks/{created['id']}", headers=other_headers)
    assert response.status_code == 403
