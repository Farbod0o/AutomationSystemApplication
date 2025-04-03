from fastapi.testclient import TestClient
from src.main.humanresource.app import app


client = TestClient(app)


def test_create_work_shift():
    response = client.post("/work_shift", json={"name": "test1"})
    assert response.status_code == 200
