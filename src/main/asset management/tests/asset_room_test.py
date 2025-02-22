from fastapi.testclient import TestClient
from src.main.asset_management.asset_app import app

client = TestClient(app)


def test_create_asset_room():
    response = client.post("/asset_rooms/", json={"title": "room 1",
                                                  "description": "description",
                                                  "address": "12 st",
                                                  "phone": "1234567890"})
    assert response.status_code == 200

    print("Done")
