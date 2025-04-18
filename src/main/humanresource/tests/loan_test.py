from fastapi.testclient import TestClient
from src.main.humanresource.app import app

client = TestClient(app)


def test_creat_loan():
    response = client.post("/loans",
                           json={"start_date": "2025-04-12",
                                 "total_amount": 5000000,
                                 "number_of_installment": 12,
                                 "installment_amount": 74444,
                                 "registration_date": "2025-04-12",
                                 "status": "active"

                                 }
                           )
    assert response.status_code == 200



