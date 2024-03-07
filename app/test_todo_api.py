from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_read_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert response.json() == []
    assert response.headers["content-type"] == "application/json"
    assert isinstance(response.json(), list)

def test_create_todo():
    response = client.post(
        "/todos/",
        json={"title": "Test Todo", "description": "This is a test"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "title": "Test Todo",
        "description": "This is a test",
        "completed": False,
        "id": response.json()["id"],
    }
    assert response.headers["content-type"] == "application/json"

def test_update_todo():
    response = client.post(
        "/todos/",
        json={"title": "Test Todo", "description": "This is a test"},
    )
    todo_id = response.json()["id"]
    response = client.put(
        f"/todos/{todo_id}",
        json={"title": "Updated Todo", "description": "This is an updated test"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Todo updated"}
    assert response.headers["content-type"] == "application/json"

def test_delete_todo():
    response = client.post(
        "/todos/",
        json={"id": "Test Todo", "description": "This is a test"},
    )
    todo_id = response.json()["id"]
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted"}
    assert response.headers["content-type"] == "application/json"