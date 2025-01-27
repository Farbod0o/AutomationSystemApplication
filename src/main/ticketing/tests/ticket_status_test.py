from fastapi.testclient import TestClient
from src.main.ticket_status.app import app

client = TestClient(app)


def test_create_ticket_status():
    response = client.post("/ticket_statuses/", json={"title": "ticket",
                                                      "status_name": "Open"
                                                      })
    assert response.status_code == 200


print("Done")
