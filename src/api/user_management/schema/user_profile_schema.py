from pydantic import BaseModel
from typing import Optional,Union
from uuid import UUID


class UserProfile(BaseModel):
    profile_img: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None

        
class UserProfileResponse(BaseModel):
    profile_id: UUID
    profile_img: Optional[str]
    first_name: str
    last_name: Optional[str]
    email: str
    phone_number: Optional[str]
    address: Optional[str]
    password: Optional[str] 
    role: Optional[str] 


class UpdateUserProfile(BaseModel):
    profile_id: str
    profile_img: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
    

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    first_name: Union[str, None] = None
