from fastapi.testclient import TestClient
from fastapi import status
from app import app

from src.api.user_management.repository.user_profile_repository import get_user_info
from src.api.user_management.schema.user_profile_schema import UserProfile

client = TestClient(app=app)

def test_user_profile():
    response = client.get('/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == "SMS Service is running."


def test_add_user():
    
    user_data = {
        "profile_img": "852",
        "first_name": "test",
        "last_name": "check",   
        "email": "aaa@gmail.com",
        "phone_number": "3692581470",
        "address": "asp"
    }
    response = client.post("/api/user-management/user/add", json=user_data)
    assert response.status_code == status.HTTP_200_OK
    response_data = response.json()
    assert response_data["first_name"] == user_data.get('first_name')


def test_delete_user():

    # SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{setting.POSTGRES_USER}:{setting.POSTGRES_PASSWORD}@{setting.POSTGRES_HOSTNAME}:{setting.POSTGRES_PORT}/{setting.POSTGRES_DB}"
    # engine = create_engine(SQLALCHEMY_DATABASE_URL)
    # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    # db = SessionLocal()
    
# try:    
    user_info = {
        "profile_img": "string",
        "first_name": "hello",
        "last_name": "string",   
        "email": "string",
        "phone_number": "string",
        "address": "string"
    }
        # response = get_user_info(data=user_info, db=db)
    # finally:
        # db.close()  
    response = client.post("/api/use-management/user/add", json=user_info)
    response_data = response.json()
    response= client.delete(f"/api/use-management/user/delete/{response_data}")


def test_update_user():

    user_data = {
        "profile_id": "1677983e-20d1-4ae5-b5fd-e39433c96ae7",
        "profile_img": "string",
        "first_name": "hello",
        "last_name": "string",   
        "email": "mno@gmail.com",   
        "phone_number": "987654321",
        "address": "test"
    }

    response = client.post("/api/user-management/user/add", json=user_data)
    response_update_data = response.json()
    assert response_update_data["first_name"] == user_data.get('first_name')
    # response= client.post(f"/api/use-management/user/delete/{response_update_data}")
