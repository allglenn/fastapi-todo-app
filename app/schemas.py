from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoInDB(TodoBase):
    id: str

# Comment: This file defines the models used in the Todo application.

def serialize_todo(todo):
    todo["id"] = str(todo["_id"])
    todo.pop("_id")
    return todo

def serialize_todos(todos):
    return [serialize_todo(todo) for todo in todos]
