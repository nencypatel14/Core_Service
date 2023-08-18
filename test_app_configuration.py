from fastapi.testclient import TestClient
from fastapi import status
from app import app

client = TestClient(app=app)

def test_correct():
    response = client.get('/')
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "SMS Service is running."
