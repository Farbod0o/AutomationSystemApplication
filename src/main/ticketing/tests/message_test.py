from fastapi.testclient import TestClient
from src.main.ticketing.message_app import app
from datetime import datetime


client = TestClient(app)

def test_create_message():
    response = client.post("/messages/", json={"title": "test message",
                                              "text": "test message",
                                              "date": datetime.now().isoformat()
                                               })
    assert response.status_code == 200

    print("Message created successfully")





