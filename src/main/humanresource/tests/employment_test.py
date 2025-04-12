from fastapi.testclient import TestClient
from src.main.humanresource.app import app
from datetime import date

client = TestClient(app)


def test_create_employment():
    response = client.post(
        "/employments",
        json={
            "start_date": "2025-01-01",
            "description": "Test employment description"

        }
    )
    assert response.status_code == 200
