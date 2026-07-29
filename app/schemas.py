from pydantic import BaseModel, EmailStr, ConfigDict, conint
from datetime import datetime
from typing import  Optional,Literal

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

    model_config = ConfigDict(from_attributes=True)  
    
class PostResponse(PostBase):
    id : int
    created_at : datetime
    owner_id : int
    owner : UserResponse

    model_config = ConfigDict(from_attributes=True)

class PostOut(BaseModel):
    Post : PostResponse
    vote : int

    model_config = ConfigDict(from_attributes=True)


class Vote(BaseModel):
    post_id : int
    dir : Literal[0,1]
        

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