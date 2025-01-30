from fastapi.testclient import TestClient
from src.main.asset_management.asset_transaction_app import app
from datetime import datetime

client = TestClient(app)

def test_create_asset_transaction():
    response = client.post("/asset_transactions", json={"count": 2,
                                                        "date of transaction":datetime.now()})

    assert response.status_code == 200

    print("Done")

