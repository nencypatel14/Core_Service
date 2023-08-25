from pydantic import BaseModel
from typing import Optional


class UserProfile(BaseModel):
    profile_img: Optional[str]
    first_name: str
    last_name: Optional[str]
    email: str
    phone_number: Optional[str]
    address: Optional[str]


class UserProfileResponse(BaseModel):
    profile_img: Optional[str]
    first_name: str
    last_name: Optional[str]
    email: str
    phone_number: Optional[str]
    address: Optional[str]
    