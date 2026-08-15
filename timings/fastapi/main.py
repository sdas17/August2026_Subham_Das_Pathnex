from fastapi import FastAPI,Response,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
app=FastAPI()
class UpdatePost(BaseModel):
    title:str
    headline:str

class Post(BaseModel):
    title: str
    headline: str
    Publish:bool =True
    rating: Optional[int] = None

data = [
    {
        "id": 1,
        "title": "Subham",
        "headline": "Learning FastAPI",
        "publish": True,
        "rating": 3
    }
]
def delete_response(id):
    for index, post in enumerate(data):
        if post["id"] == id:
            return index

    return None

def fetch_id(id):
    for i in data:
         if i['id']== id:
            return i
# request method get "/"
# post methos is post 
@app.get("/")
async def get_response():
      return {"status":data}
@app.delete("/delete/{id}")
async def delete_reponse(id:int):
    delete_index=delete_response(id)
    data.pop(delete_index)
    if delete_index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )
    return {
        "status": "success",
        "message": "Post deleted successfully"
    }
@app.put("/post/{id}")
async def update_post(id: int, response: UpdatePost):

    post = fetch_id(id)

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )

    post["title"] = response.title
    post["headline"] = response.headline

    return {
        "status": "success",
        "data": post
    }


@app.get("/getid/{id}")
async def get_response(id: int, response: Response):

    post = fetch_id(id)

    if post is None:
        response.status_code = 404
        return {"status": "Post not found"}

    return {"status": post}

@app.post("/post_reocrd")
async def post_data(response:Post):
    value_respone= response.dict()
    value_respone['id']=randrange(0,10000)
    data.append(value_respone)
    return {"status": data}

    
# @app.post("/post")
# async def post_data(payload:dict=Body(...)):
#     print(payload)
#     return {"status":f"payload response {payload['title'] and payload['headline']}"}