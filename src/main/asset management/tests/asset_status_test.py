from fastapi.testclient import TestClient
from src.main.asset_management.asset_app import app

client = TestClient(app)


def test_create_asset_status():
    response = client.post("/asset_statuses/", json={"status_name": "Available",
                                                     })
    assert response.status_code == 200

    print("Done")
