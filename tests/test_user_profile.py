from fastapi.testclient import TestClient
from fastapi import status
from app import app

# from src.api.user_management.repository.user_profile_repository import add_user_repository
# from src.api.user_management.schema.user_profile_schema import UserProfile

client = TestClient(app=app)

def test_user_profile():
    response = client.get('/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "SMS Service is running."


def test_add_user():
    
    user_data = {
        "profile_img": "789",
        "first_name": "nency",
        "last_name": "patel",   
        "email": "mno@gmail.com",
        "phone_number": "9865329479",
        "address": "mkn"
    }
    response = client.post("/api/user-management/user/add", json=user_data)
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert response_data["first_name"] == "nency"


def test_delete_user():

    profile_id = "28524483-635f-42a9-a353-ead9c7f3e1a3"
    url = f"/api/user-management/user/delete/{profile_id}"

    response = client.delete(url)
    print(response)
    
    assert response.status_code ==  status.HTTP_200_OK
    response_delete_data = response.json()
    assert response_delete_data ==  "Delete User Data"


def test_update_user():

    user_data = {
        "profile_id": "86a1b032-b61d-4c28-94f8-2820e2c5109b",
        "profile_img": "456",
        "first_name": "nency",
        "last_name": "patel",   
        "email": "qwe@gmail.com",
        "phone_number": "9865329479",
        "address": "qwe"
    }
    response = client.post("/api/user-management/user/add", json=user_data)
    assert response.status_code == status.HTTP_200_OK
    response_update_data = response.json()
    assert response_update_data["email"] == "qwe@gmail.com"
