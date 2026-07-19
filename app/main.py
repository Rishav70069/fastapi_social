

from random import randrange

from fastapi import FastAPI , Response , status , HTTPException ,Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional,List
import psycopg
from psycopg.rows import dict_row
import time
from . import models
from .database import engine , get_db
from sqlalchemy.orm import Session
from . import models, schemas

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
    

@app.get("/")
async def root():
    return {"message": "Welcome to fastapi project"}

@app.get("/posts",response_model=List[schemas.PostResponse])
def posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts""")  #raw SQL
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()     #sqlalchemy (python query)
    return posts

@app.post("/posts",status_code= status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def create_post(post : schemas.PostCreate,db: Session = Depends(get_db)):
    # cursor.execute("""INSERT INTO posts (title,content,published) VALUES(%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    # new_post = cursor.fetchone()

    # conn.commit()

    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.get("/posts/latest",response_model=schemas.PostResponse)
def get_latest_post(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts ORDER BY id DESC LIMIT 1""")
    # post = cursor.fetchone()
    latest_post = db.query(models.Post).order_by(models.Post.created_at.desc()).first()
    return latest_post


@app.get("/posts/{id}",response_model=schemas.PostResponse)
def get_post(id: int,db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts WHERE id = %s """, (id,))
    # Post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id == id).first()

    if not post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail = f"{id} was not found")
        
    return post

@app.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING * """, (id,))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found")
    
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}",response_model=schemas.PostResponse)
def update_post(id: int, post: schemas.PostCreate,db: Session = Depends(get_db)):
    # cursor.execute("""UPDATE posts SET title = %s ,content = %s , published = %s WHERE id = %s RETURNING * """, (post.title,post.content,post.published,(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    update_post = post_query.first()

    if update_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found")

    post_query.update(post.model_dump(),synchronize_session=False)
    db.commit()
    return post_query.first()

