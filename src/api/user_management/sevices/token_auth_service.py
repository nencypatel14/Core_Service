from fastapi.security import OAuth2PasswordBearer 
from datetime import timedelta, datetime
from datetime import timedelta
from typing import Union
from jose import jwt    
from pydantic import ValidationError
from typing_extensions import Annotated
from fastapi import status, Depends, HTTPException

from config.config import settings
from sqlalchemy.orm import Session
from database.db import get_db
from src.api.user_management.schema.user_profile_schema import UserProfile
from src.api.user_management.repository.user_profile_repository import get_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user-management/user/token")

ALGORITHM="HS256"

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=ALGORITHM)
        token_data = UserProfile(**payload)

    except(jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user= get_user(token_data.email, db)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not find user",
        )
    return UserProfile(**user.__dict__)
