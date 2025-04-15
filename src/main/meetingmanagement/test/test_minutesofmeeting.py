# tests/test_minutesofmeeting.py
from fastapi.testclient import TestClient
from src.main.meetingmanagement.app import app

client = TestClient(app)

def test_create_minutes_of_meeting():
    response = client.post("/minutesofmeeting/", json={
        "listName": "Meeting List 1"
    })
    assert response.status_code == 200