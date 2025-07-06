from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# Create FastAPI app instance
app = FastAPI(
    title="Python FastAPI UV Application",
    description="A FastAPI application built with UV package manager",
    version="0.1.0"
)

# Pydantic models for data validation
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    is_available: Optional[bool] = None

# In-memory storage (in a real app, you'd use a database)
items_db = []
item_id_counter = 1

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "Hello from Python FastAPI UV!",
        "docs": "/docs",
        "redoc": "/redoc"
    }

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "fastapi-uv"}

# Get all items
@app.get("/items", response_model=List[Item])
async def get_items():
    return items_db

# Get a specific item by ID
@app.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# Create a new item
@app.post("/items", response_model=Item)
async def create_item(item: Item):
    global item_id_counter
    new_item = item.model_copy()
    new_item.id = item_id_counter
    item_id_counter += 1
    items_db.append(new_item)
    return new_item

# Update an item
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item_update: ItemUpdate):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            update_data = item_update.model_dump(exclude_unset=True)
            updated_item = item.model_copy(update=update_data)
            items_db[i] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# Delete an item
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for i, item in enumerate(items_db):
        if item.id == item_id:
            deleted_item = items_db.pop(i)
            return {"message": f"Item {deleted_item.name} deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

# Search items by name
@app.get("/items/search/{name}")
async def search_items(name: str):
    matching_items = [item for item in items_db if name.lower() in item.name.lower()]
    return matching_items

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
