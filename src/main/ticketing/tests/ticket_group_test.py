from fastapi.testclient import TestClient
from src.main.ticketing.ticket_app  import app

client = TestClient(app)


def test_create_ticket_group():
    response = client.post("/ticket_groups/", json={"name": "abcd",
                                                    "parent_id": None,
                                                    "child_id": None
                                                    })
    assert response.status_code == 200

print("Done")
