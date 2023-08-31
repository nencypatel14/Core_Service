import logging
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from database.db import get_db
from src.api.user_management.repository.user_profile_repository import add_user_repository
from src.api.user_management.repository.user_profile_repository import get_user_info
from src.api.user_management.repository.user_profile_repository import get_update_profile
from src.api.user_management.schema.user_profile_schema import UserProfileResponse, UpdateUserProfile, UserProfile
from src.api.user_management.model import user_profile


router = APIRouter(prefix="/user")


@router.post("/add", response_model=UserProfileResponse)
async def add_user(user_data: UserProfile, db: Session = Depends(get_db)):
    try:
        logging.info(f"add user data: {user_data}")
        user = add_user_repository(user_data.__dict__, db)
        logging.info(f"added data: {user} with user id: {user.profile_id}.")
        return user
    except ArithmeticError as e:    
        logging.error(f"Error - user_data: {e}")
        raise Exception("internal_sever_error")


@router.delete("/delete/{profile_id}")
def delete_user(profile_id: str, db: Session = Depends(get_db)):    
    user = get_user_info(profile_id, db)

    db.delete(user)
    db.commit()
    logging.info(f"delete_user: Success")
    return { "ok" : True}


@router.get("/get/{id}")
async def read_data(id: str, db: Session = Depends(get_db)):
    try:
        logging.info(f"get user data for id: {id}")
        user = get_user_info(id, db)
        logging.info(f"get user data with user_id: {user.profile_id}")
        return user
    except Exception as e:
        logging.error(f"Error - id: {e}")
        raise Exception("internal_sever_error")


@router.post("/update/")
async def update_user_profile(user_data: UpdateUserProfile, db: Session = Depends(get_db)):
    try:
        logging.info(f"update user id: {user_data} with data: {user_data}")

        data = {k: v for k, v in user_data.__dict__.items() if v is not None}

        user = get_update_profile(data, db=db)
        # logging.info(f"Updated user info with user id: {user.profile_id}")
        if user:
            return jsonable_encoder(user)
    except ArithmeticError as e:
        logging.error(f"Error - id: {e}")
        raise Exception("Internal_server_error")    
    