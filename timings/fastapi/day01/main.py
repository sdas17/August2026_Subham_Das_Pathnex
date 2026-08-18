from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

todo_list = []


class Updatetodo(BaseModel):
    user_name: str


class Todo(BaseModel):
    id: int
    user_name: str
    daily_active: str
    task: bool


# GET ALL
@app.get("/response")
def get_todo_list():
    return {
        "response": todo_list
    }


# POST
@app.post("/post_todo_list")
def todo_post_list(todo: Todo):
    todo_list.append(todo)

    return {
        "response": todo_list
    }


# FIND TODO BY ID
def todo_list_item(id: int):
    for todo in todo_list:
        if todo.id == id:
            return todo

    return None


# PUT / UPDATE
@app.put("/update_response/{id}")
def update_response(id: int, updateresponse: Updatetodo):

    response = todo_list_item(id)

    # Check first
    if response is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    # Update user_name
    response.user_name = updateresponse.user_name

    return {
        "status": "success",
        "response": response
    }


# DELETE
@app.delete("/delete/{id}")
def delete_id(id: int):

    for index, todo in enumerate(todo_list):

        if todo.id == id:

            todo_list.pop(index)

            return {
                "status": "success",
                "message": "Todo deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )


# GET BY ID
@app.get("/response/{id}")
def todo_list_based_item(id: int):

    response = todo_list_item(id)

    if response is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return {
        "response": response
    }