

from logging import raiseExceptions
from random import randrange
from warnings import deprecated

from fastapi import FastAPI , Response , status , HTTPException ,Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional,List
import psycopg
from psycopg.rows import dict_row
import time
from .database import engine , get_db
from sqlalchemy.orm import Session
from . import models, schemas ,utility
from .routers import post,user,auth

models.Base.metadata.create_all(bind=engine)

# my_posts = [{"title" : "title of post1","content" : "content of post1", "id" : 1},
#             {"title" : "title of post2 " , "content" : "content of post2" , "id" : 2}]


app = FastAPI()    # fastapi instance


# while True:
try:
    conn = psycopg.connect(host = 'localhost' , dbname = 'fastapi' , user = 'postgres' , password = '@Rishav123', row_factory = dict_row)
    cursor = conn.cursor()
    print("Database connection was sucessfull")
    
except Exception as error:
    print("Connection to Database failed")
    print("Error: ",error)
    time.sleep(3)


# def find_post(id):
#     for p in my_posts:
#         if p["id"] == id:
#             return p
        
# def find_index_post(id):
#     for i,p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
    
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

# @app.get("/")
# async def root():
#     return {"message": "Welcome to fastapi project"}

