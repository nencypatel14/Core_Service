import logging
from sqlalchemy.orm import Session

from src.api.user_management.model.user_profile import UserProfile

def add_user_repository(data: dict, db: Session):
    """
    Add user data in user_profile table.
    param: email
    return: 
    """
    try:
        logging.info(f"adding data: {data} to user info.")
        user = UserProfile(**data) 
        db.add(user)
        db.commit()
        db.refresh(user)
        logging.info(f"added data: {user} with user id: {user.profile_id}.")
    except ArithmeticError as e:
        logging.error(f"Error: add_user: {e}")
        raise Exception("internal_server_error")
    else:
        logging.info("add_user_repository: Success")
        return user

def get_user_info(id: str, db:Session):
    """
    get user data in user_profile table.
    param: profile_id
    return:
    """
    try:
        logging.info(f"serach user from database with id: {id}")
        user = db.query(UserProfile).filter(UserProfile.profile_id == id).first()
        logging.info(f"get user data with user_id: {user.profile_id}")
    except ArithmeticError as e:
        logging.error(f"Error: get_user: {e}")
        raise Exception("internal_sever_error")
    else:
        logging.info("get_user_info: Success")
        return user
