from fastapi import FastAPI 
from .database import engine , get_db
from . import models
from .routers import post,user,auth,vote
from app import database

models.Base.metadata.create_all(bind=engine)

app = FastAPI()    # fastapi instance
# print(database.SQLALCHEMY_DATABASE_URL)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# @app.get("/")
# async def root():
#     return {"message": "Welcome to fastapi project"}

