from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import  Optional

class PostBase(BaseModel):  #schema from pydantic model
    title : str
    content : str
    published : bool = True

class PostCreate(PostBase):
    pass

class UserResponse(BaseModel):
    id : int
    email : EmailStr
    created_at : datetime

    class Config:
        orm_mode = True   
    
class PostResponse(PostBase):
    id : int
    created_at : datetime
    owner_id : int
    owner : UserResponse

    class Config:
        orm_mode = True
        

class UserCreate(BaseModel):
    email : EmailStr
    password : str


class user_login(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token : str
    token_type : str

class Token_data(BaseModel):
    id : Optional[int] = None