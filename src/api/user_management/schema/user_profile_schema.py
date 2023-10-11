from pydantic import BaseModel, ConfigDict, field_validator, EmailStr
from typing import Optional
from uuid import UUID


class UserProfile(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra='allow')
    profile_img: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: EmailStr
    phone_number: Optional[str] = None  
    address: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None
    

    @field_validator('password')
    @classmethod
    def validate_password(cls, password):
        special_symbols =['$', '@', '#', '%']
        
        if len(password) < 6:
            raise ValueError('Password must have atleast 6 characters.')
        
        if not any(characters.isdigit() for characters in password):
            raise ValueError('Password must have at least one numeric character.')
            
        if not any(characters.isupper() for characters in password):
            raise ValueError('Password must have at least one uppercase character')
            
        if not any(characters.islower() for characters in password):
            raise ValueError('Password must have at least one lowercase character')
            
        if not any(characters in special_symbols for characters in password):
            raise ValueError('Password should have at least one of the symbols $@#%')
            
        return password

    @field_validator('role')
    @classmethod
    def validate_role(cls, role):
        if role not in ["User","Admin"]:
            raise ValueError('Please add Correct role.')
        return role
    
    @field_validator('phone_number')
    @classmethod
    def validate_phone_number(cls, phone_number):
        if len(phone_number)<10 or len(phone_number)>10:
            raise ValueError('Invalide Phone number')
        return phone_number


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
    profile_id: UUID
    profile_img: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    password: Optional[str] = None
    role: Optional[str] = None

    @field_validator('phone_number')
    @classmethod
    def validate_phone_number(cls, phone_number):
        if len(phone_number)<10 or len(phone_number)>10:
            raise ValueError('Invalide Phone number')
        return phone_number

    @field_validator('role')
    @classmethod
    def validate_role(cls, role):
        if role not in ["User","Admin"]:
            raise ValueError('Please add Correct role.')
        return role


class Token(BaseModel):
    access_token: str
    token_type: str


class loginSchema(BaseModel):
    username: str
    password: str
