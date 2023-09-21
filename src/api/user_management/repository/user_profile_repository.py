import logging
from sqlalchemy.orm import Session
from src.api.user_management.model.user_profile import UserProfile


def add_user_repository(data: dict, db: Session):
    """
    Add user data in user_profile table.
    param: data
    return user: 
    """
    try:
        logging.info(f"adding data: {data} to user info.")
        user = UserProfile(**data) 
        db.add(user)
        db.commit()
        db.refresh(user)
        logging.info(f"added data: {user} with user id: {user.profile_id}.")
    except Exception as e:
        logging.error(f"Error: add_user: {e}")
        raise Exception("internal_server_error")
    else:
        logging.info("add_user_repository: Success")
        return user

def get_user_info(profile_id: str, db:Session):
    """
    get user data in user_profile table.
    param: profile_id
    return user:
    """
    try:
        logging.info(f"seraching user from database with id: {profile_id}")
        user = db.query(UserProfile).filter(UserProfile.profile_id == profile_id).first()
        logging.info(f"get user data with user_id: {user.profile_id}.")
    except Exception as e:
        logging.error(f"Error: get_user: {e}")
        raise Exception("internal_sever_error")
    else:
        logging.info("get_user_info: Success")
        return user

def get_update_profile(data: dict, db: Session):
    """
    get update data in user_profile table.
    param: data
    return user data:
    """
    try:
        id = data['profile_id']
        data.pop("profile_id")

        logging.info(f"serching user from database with input id: {id}")
        user_data = db.query(UserProfile).filter(UserProfile.profile_id == id).first()

        for key, value in data.items():
            if hasattr(user_data, key):
                setattr(user_data, key, value)

        db.commit()
        db.refresh(user_data)
        return user_data
    except ArithmeticError as e:
        logging.error(f"Error: update_user: {e}")
        raise Exception("internal_server_error")


def get_user(email: str, db:Session):
    """
    get user data in user_profile table.
    param: email
    return user:
    """
    try:
        logging.info(f"seraching user from database with email_id: {email}")
        user = db.query(UserProfile).filter(UserProfile.email == email).first()
        logging.info(f"get user data with email_id: {user.email}.")
    except Exception as e:
        logging.error(f"Error: get_user: {e}")
        raise Exception("internal_sever_error")
    else:
        logging.info("get_user_info: Success")
        return user
    