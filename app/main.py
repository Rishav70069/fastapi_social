from fastapi import FastAPI 
from .database import engine , get_db
from . import models
from .routers import post,user,auth,vote
from app import database

from fastapi.middleware.cors import CORSMiddleware



# models.Base.metadata.create_all(bind=engine) // since we are using alembic now , we do not need use this to create tables.

app = FastAPI()    # fastapi instance
# print(database.SQLALCHEMY_DATABASE_URL)



# origins = [
#     "https://www.google.com",
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {"message": "Welcome to fastapi project"}

