import logging
from fastapi import APIRouter, Depends, BackgroundTasks, UploadFile
from sqlalchemy.orm import Session
from datetime import timedelta
from typing_extensions import Annotated

from database.db import get_db
from src.api.user_management.repository.user_profile_repository import add_user_repository ,get_user_info ,get_update_profile, get_user, send_email, upload_file
from src.api.user_management.schema.user_profile_schema import UserProfileResponse, UpdateUserProfile, UserProfile, loginSchema
from set_response.response import success_response, error_response
from src.api.user_management.sevices.password_service import verify_password
from src.api.user_management.sevices.token_auth_service import create_access_token,get_current_user
from config.config import settings

router = APIRouter(prefix="/user")

@router.post("/token")
async def login(User_data: loginSchema ,db: Session = Depends(get_db)):
    user_dict = get_user(User_data.username, db)
    try:
        if not user_dict:
            raise Exception("Incorrect username or password")
        
        if not verify_password(plain_password=User_data.password, hashed_password=user_dict.password):
            raise Exception("Incorrect username or password")
    
        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"email": user_dict.email}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception as e:
        logging.error(f"Error - user_dict: {e}")
        return error_response(str(e))

@router.post("/add", response_model=UserProfileResponse)
async def add_user(token: Annotated[str, Depends(get_current_user)], user_data: UserProfile , db: Session = Depends(get_db)):
    user = token
    try:
        logging.info(f"add user data: {user_data}")
        if user_data.first_name == None or user_data.email == None: 
            logging.warning("please enter first_name or email.")    
            raise Exception("Please Enter valid first_name or email.")
        
        existing_user = get_user(user_data.email, db=db)
        if existing_user:
            logging.warning("Email already exists in the database.")
            raise Exception("Email already exists.")

        else:
            # user_data_dict = user_data.__dict__
            # file = user_data_dict['profile_img']
            # user_data_dict['profile_img'] = user_data_dict['profile_img'].filename

            user = add_user_repository(user_data.__dict__, db)
            # with open("image/"+file.filename, "wb") as f:
            #     shutil.copyfileobj(file.file , f)

            logging.info(f"added data: {user} with user id: {user.profile_id}.")    
        return user
    except Exception as e:    
        logging.error(f"Error - user_data: {e}")
        return error_response(str(e))

@router.delete("/delete/")
def delete_user(token: Annotated[str, Depends(get_current_user)], profile_id: str , db: Session = Depends(get_db)):
    user_info = token
    if user_info.role == "Admin":
        user = get_user_info(profile_id,db)
        user_id = str(user.profile_id)
        if user_id == profile_id:
            db.delete(user)
            db.commit()
            return "Delete User Data"
        else:
            logging.warning("Please Enter profile_id.")
            return {"message":"Please Enter valid profile_id."}

    elif user_info.role == "User":
        user = get_user_info(profile_id, db)
        logging.info(f"Deleted data: {user} from table with user id: {user.profile_id}.")
        db.delete(user)
        db.commit()
        logging.info(f"Delete_user: Success")
        return "Deleted User Data"

@router.get("/get")
async def read_data(token: Annotated[str, Depends(get_current_user)],profile_id: str , db: Session = Depends(get_db)):
    userInfo = token
    try:
        if userInfo.role == "admin":
            user = get_user_info(profile_id,db)
            user_id = str(user.profile_id)
            if user_id == profile_id:
                logging.info(f"get user data for profile_id: {profile_id}")
                user = get_user_info(profile_id,db)
        
                return success_response(user)
        elif userInfo.role == "user":
            logging.info(f"get user data for prfile_id: {profile_id}")
            user_data = token
            return success_response(user_data)
    except Exception as e:
        logging.error(f"Error - id: {e}")
        raise Exception("internal_sever_error")

@router.post("/update/")
async def update_user_profile(token: Annotated[str, Depends(get_current_user)], user_data: UpdateUserProfile, profile_id:str , db: Session = Depends(get_db)):
    userInfo = token
    try:
        if userInfo.role == "Admin":
            user = get_user_info(profile_id,db)
            user_id = str(user.profile_id)
            if user_id == profile_id:
                logging.info(f"update user id: {user_data} with data: {user_data}")
                data = {key: value for key, value in user_data.__dict__.items() if value is not None}
                user = get_update_profile(data, db=db)
                return success_response(UpdateUserProfile(**user.__dict__))
            
            existing_user = get_user(email=user_data.email, db=db)
            if existing_user:
                logging.warning("Email already exists in the database.")
                raise Exception("Email already exists.") 

        elif userInfo.role == "User":
            # for removing all null values
            data = {key: value for key, value in user_data.__dict__.items() if value is not None}
            user = get_update_profile(data, db=db)
            return success_response(UpdateUserProfile(**user.__dict__))


        logging.info(f"Updated user data with user id: {user.profile_id}")
    except ArithmeticError as e:
        logging.error(f"Error - id: {e}")
        raise Exception("Internal_server_error")

# background task for send_email
@router.get("/send_email/")
def index(background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, 'Hello there!' )
    return {'result': 'success'}

# background task for uploadfile 
@router.post("/uploadfile/") 
async def create_upload_file(background_tasks: BackgroundTasks, file: UploadFile): 
    background_tasks.add_task(upload_file, file) 
    return {"message": "File uploaded successfully"}
