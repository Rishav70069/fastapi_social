from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):  #schema from pydantic model
    title : str
    content : str
    published : bool = True

class PostCreate(PostBase):
    pass
    
class PostResponse(PostBase):
    id : int
    created_at : datetime

    class Config:
        orm_mode = True
        