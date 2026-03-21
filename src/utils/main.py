# frontend-app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.requests import Request
import uvicorn

app = FastAPI(title="Frontend App", description="API for frontend application", version="1.0.0")

class User(BaseModel):
    id: int
    name: str
    email: str

class Item(BaseModel):
    id: int
    name: str
    price: float
    is_active: bool
    owner_id: Optional[int]

@app.get("/users/")
async def read_users():
    return [{"id": 1, "name": "John Doe", "email": "john@example.com"}, {"id": 2, "name": "Jane Doe", "email": "jane@example.com"}]

@app.get("/items/")
async def read_items():
    return [{"id": 1, "name": "Item 1", "price": 10.99, "is_active": True, "owner_id": 1}, {"id": 2, "name": "Item 2", "price": 9.99, "is_active": False, "owner_id": 2}]

@app.post("/users/")
async def create_user(user: User):
    return user

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return item

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return JSONResponse(content={"message": f"Item {item_id} deleted"}, status_code=200)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)