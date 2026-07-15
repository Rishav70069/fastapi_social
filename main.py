

from random import randrange

from fastapi import FastAPI , Response , status , HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

my_posts = [{"title" : "title of post1","content" : "content of post1", "id" : 1},
            {"title" : "title of post2 " , "content" : "content of post2" , "id" : 2}]


app = FastAPI()

class Post(BaseModel):
    title : str
    content : str
    published : bool = True
    rating : Optional[int] = None

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
async def root():
    return {"message": "hello guys"}

@app.get("/posts")
def posts():
    return {"post": my_posts}

@app.post("/posts")
def create_post(post : Post):
    post_dict = post.model_dump();
    post_dict["id"] = randrange(1,1000000)
    my_posts.append(post_dict)
    # print(post)
    # print(post.rating)
    # print(post.model_dump()) # to convert pydantic schema data into dictionary
    return {"data" : post_dict}

@app.get("/posts/latest")
def get_latest_post():
    Post = my_posts[len(my_posts) - 1]
    return {"detail" : Post}


@app.get("/posts/{id}")
def get_post(id: int):
    print(id)
    Post = find_post(id)
    if not Post:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail = f"{id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message" : f"{id} was not found"}
    return {"post detail" : Post}
