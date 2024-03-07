from fastapi import APIRouter, HTTPException
from schemas import TodoCreate, TodoInDB, TodoUpdate, serialize_todos, serialize_todo
from database import get_database
from bson import ObjectId


router = APIRouter()

db = get_database()

@router.get("/todos/")
async def read_todos():
    todos = list(db.todos.find())
    return serialize_todos(todos)

@router.post("/todos/", response_model=TodoInDB)
async def create_todo(todo: TodoCreate):
    todo_id = db.todos.insert_one(todo.dict()).inserted_id
    todo = db.todos.find_one({"_id": todo_id})
    return serialize_todo(todo)

@router.put("/todos/{todo_id}")
async def update_todo(todo_id: str, todo: TodoUpdate):
    todo = dict(todo)
    result = db.todos.update_one({"_id": ObjectId(todo_id)}, {"$set": todo})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail=f"Todo with ID {todo_id} not found")
    return {"message": "Todo updated"}

@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    result = db.todos.delete_one({"_id": ObjectId(todo_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail=f"Todo with ID {todo_id} not found")
    return {"message": "Todo deleted"}
