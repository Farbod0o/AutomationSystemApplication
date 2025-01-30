from fastapi.testclient import TestClient
from src.main.asset_management.asset_app import app

client = TestClient(app)

def test_create_asset():
    response = client.post("/assets/", json={"count": 5,
                                             "reminder": 5,
                                             "limit": 3})
    assert response.status_code == 200

    print("Done")


