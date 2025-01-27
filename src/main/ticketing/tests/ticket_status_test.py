from fastapi.testclient import TestClient
from src.main.ticketing.ticket_status_app import app

client = TestClient(app)


def test_create_ticket_status():
    response = client.post("/ticket_statuses/", json={"title": "ticket",
                                                      "status_name": "Open"
                                                      })
    assert response.status_code == 200

print("Done")
