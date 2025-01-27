from fastapi.testclient import TestClient
from datetime import datetime
from src.main.ticketing.ticket_app import app

client = TestClient(app)


def test_create_ticket():
    response = client.post("/tickets/", json={"title": "ticket",
                                              "text": "test ticket",
                                              "created_by": 1,
                                              "assigned_to": 2,
                                              "datetime": datetime.now()
                                              })
    assert response.status_code == 200

print("Done")
