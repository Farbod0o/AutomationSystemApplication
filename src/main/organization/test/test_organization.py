# tests/test_organization.py
from fastapi.testclient import TestClient
from src.main.organization.app import app

client = TestClient(app)

def test_create_organization():
    response = client.post("/organizations/", json={
        "manager": "John Doe",
        "address": "1234 Main St",
        "phoneNum": "09121231122",
        "logo": "logo.png",
        "task": "Development",
        "departmentNum": 5,
        "description": "A description of the organization"
    })
    assert response.status_code == 200