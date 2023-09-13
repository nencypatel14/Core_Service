import logging
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Union
from jose import jwt

from database.db import get_db
from src.api.user_management.repository.user_profile_repository import add_user_repository ,get_user_info ,get_update_profile, get_user
from src.api.user_management.schema.user_profile_schema import UserProfileResponse, UpdateUserProfile, UserProfile
from config.config import setting
from set_response.response import success_response, error_response

router = APIRouter(prefix="/user")


@router.post("/add", response_model=UserProfileResponse)
async def add_user(user_data: UserProfile, db: Session = Depends(get_db)):
    try:
        logging.info(f"add user data: {user_data}")

        if user_data.first_name == None or user_data.email == None: 
            logging.warning("please enter first_name or email.")
            raise Exception("Please Enter valid first_name or email")
        else:
            user = add_user_repository(user_data.__dict__, db)
            logging.info(f"added data: {user} with user id: {user.profile_id}.")
        return user
    except Exception as e:    
        logging.error(f"Error - user_data: {e}")
        return error_response({"message": str(e)})


@router.delete("/delete/")
def delete_user(email:str = None, password: str = None, profile_id: str = None, db: Session = Depends(get_db)):
    if not email or not password:
        return {"message":"Please Enter valid fields."}
    user_info = get_user(email,db)
    if email: 
        if user_info.password == password:
            if user_info.role == "user":
                user = get_user_info(profile_id, db)
                logging.info(f"Deleted data: {user} from table with user id: {user.profile_id}.")
                db.delete(user)
                db.commit()
                logging.info(f"Delete_user: Success")
                return "Delete User Data"
            elif user_info.role == "admin":
                user = get_user_info(profile_id,db)
                user_id = str(user.profile_id)
                if user_id == profile_id:
                    db.delete(user_info)
                    db.commit()
                    return "Data Deleted"
                else:
                    logging.warning("Please Enter profile_id.")
                    return {"message":"Please Enter valid profile_id."}
        else:
            return {"message":"Please Enter valid Username or Password"}


@router.get("/get/{id}")
async def read_data(id: str, db: Session = Depends(get_db)):
    try:
        logging.info(f"get user data for id: {id}")
        user = get_user_info(id, db)
        return success_response(user)
    except Exception as e:
        logging.error(f"Error - id: {e}")
        raise Exception("internal_sever_error")


@router.post("/update/")
async def update_user_profile(user_data: UpdateUserProfile, db: Session = Depends(get_db)):
    try:
        logging.info(f"update user id: {user_data} with data: {user_data}")

        data = {k: v for k, v in user_data.__dict__.items() if v is not None}

        user = get_update_profile(data, db=db)
        if user:
            return success_response(user)
        
        logging.info(f"Updated user data with user id: {user.profile_id}")
    except ArithmeticError as e:
        logging.error(f"Error - id: {e}")
        raise Exception("Internal_server_error")    
    
@router.post("/token")
def create_access_token(data: dict): 
    to_encode = data
    print(data)
    

    encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, algorithm=setting.ALGORITHM)
    return encoded_jwt
