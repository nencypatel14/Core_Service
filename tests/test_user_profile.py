import json
import shutil
from fastapi import File
from fastapi.testclient import TestClient
from fastapi import status
from app import app

client = TestClient(app=app)

def test_add_user():
    response = client.post(
        "/api/user-management/user/token",
        data={
            "username": "test@gmail.com",
            "password": "Abc@123"
        },
    )
    token_data = json.loads(response.text)
    valid_token = token_data.get('access_token')
    token_type = token_data.get('token_type')


    with open('1.png', 'rb') as filep:
        file_content = filep.read()
    

    user_data = {
        "first_name": "test",
        "last_name": "check",   
        "email": "aaa@mailinator.com",
        "phone_number": "9685741230",
        "address": "asp",
        "password": "123",
        "role": "user"
    }
    response = client.post("/api/user-management/user/add", headers={"Authorization": f"{token_type} {valid_token}"}, data=user_data, files={'profile_img':file_content})
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    breakpoint()
    assert response_data["first_name"] == user_data.get('first_name')


def test_delete_user():
    response = client.post("/api/user-management/user/token",data={"username": "test@gmail.com","password": "Abc@123"})
    token_data = json.loads(response.text)
    valid_token = token_data.get('access_token')
    token_type = token_data.get('token_type')
    with open('1.png', 'rb') as filep:
        file_content = filep.read()
    user_data = {
        "first_name": "test",
        "last_name": "check",   
        "email": "aaa@mailinator.com",
        "phone_number": "9685741230",
        "address": "asp",
        "password": "123",
        "role": "user"
    }
    response = client.post("/api/user-management/user/add", headers={"Authorization": f"{token_type} {valid_token}"}, data=user_data, files={'profile_img':file_content})
    response_data = response.json()
    response= client.delete(f"/api/user-management/user/delete/{response_data}")


def test_update_user():
    response = client.post("/api/user-management/user/token",data={"username": "email@gmail.com","password": "123"})
    token_data = json.loads(response.text)
    valid_token = token_data.get('access_token')
    token_type = token_data.get('token_type')
    with open('1.png', 'rb') as filep:
        file_content = filep.read()
    user_data = {
        "profile_id": "9c2214f3-f1c5-4d3c-bba0-03dbf2736256",
        "profile_img": "123",
        "first_name": "check",
        "last_name": "test",   
        "email": "aaa@gmail.com",   
        "phone_number": "3692581470",
        "address": "asp",
        "password": "123",
        "role": "admin"
    }
    response = client.post("/api/user-management/user/add", headers={"Authorization": f"{token_type} {valid_token}"}, json=user_data)
    response_update_data = response.json()
    breakpoint()
    assert response_update_data["first_name"] == user_data.get('first_name')

