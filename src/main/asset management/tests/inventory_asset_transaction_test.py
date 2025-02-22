from fastapi.testclient import TestClient
from src.main.asset_management.asset_app import app
from datetime import datetime

client = TestClient(app)


def test_create_inventory_asset_transaction():
    response = client.post("/inventory_asset_transactions/", json={"count": 10,
                                                                   " date_of_transaction": str(datetime.utcnow()),
                                                                   "asset_id": 1,
                                                                   })
    assert response.status_code == 200

    print("Done")
