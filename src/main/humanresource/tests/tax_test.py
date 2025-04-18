from fastapi.testclient import TestClient
from src.main.humanresource.app import app

client = TestClient(app)


def test_creat_tax():
    response = client.post("/taxes",
                           json={"description": "test tax description",
                                 "tax_type": "income"

                                 }

                           )
    assert response.status_code == 200
