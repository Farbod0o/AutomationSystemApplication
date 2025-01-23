# tests/test_user.py
from fastapi.testclient import TestClient
from src.main.users.app import app

client = TestClient(app)


def test_create_user():
    response = client.post("/users/", json={"userName": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert response.json()["userName"] == "testuser"
