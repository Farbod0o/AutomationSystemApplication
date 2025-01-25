from fastapi.testclient import TestClient
from src.main.ticketing.app import app


client = TestClient(app)

def test_creat_ticket_priority():
    response = client.post("/ticket_priority/", json={"priority": "high"})
    assert response.status_code == 200

    print("Priority created successfully")
