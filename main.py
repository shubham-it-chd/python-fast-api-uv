from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os
import subprocess
import sys

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

def generate_ssl_certificates():
    """Generate self-signed SSL certificates for development"""
    try:
        # Check if OpenSSL is available
        subprocess.run(["openssl", "version"], check=True, capture_output=True)
        
        # Create certificates directory if it doesn't exist
        certs_dir = "certs"
        os.makedirs(certs_dir, exist_ok=True)
        
        keyfile = os.path.join(certs_dir, "key.pem")
        certfile = os.path.join(certs_dir, "cert.pem")
        
        # Generate private key
        subprocess.run([
            "openssl", "genrsa", "-out", keyfile, "2048"
        ], check=True, capture_output=True)
        
        # Generate certificate
        subprocess.run([
            "openssl", "req", "-new", "-x509", "-key", keyfile, 
            "-out", certfile, "-days", "365", "-subj", 
            "/C=US/ST=State/L=City/O=Organization/CN=localhost"
        ], check=True, capture_output=True)
        
        print(f"SSL certificates generated successfully!")
        print(f"Key file: {keyfile}")
        print(f"Cert file: {certfile}")
        
        return keyfile, certfile
        
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("OpenSSL not found. Please install OpenSSL to generate self-signed certificates.")
        print("Alternatively, you can provide your own certificates via environment variables.")
        return None, None

if __name__ == "__main__":
    import os
    
    # Check for command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == "--generate-ssl":
        generate_ssl_certificates()
        sys.exit(0)
    
    # SSL configuration
    ssl_keyfile = os.getenv("SSL_KEYFILE", None)
    ssl_certfile = os.getenv("SSL_CERTFILE", None)
    
    # If no SSL certificates provided, try to generate them
    if not ssl_keyfile and not ssl_certfile:
        print("No SSL certificates found. Attempting to generate self-signed certificates...")
        ssl_keyfile, ssl_certfile = generate_ssl_certificates()
    
    # Check if SSL certificates are available
    if ssl_keyfile and ssl_certfile and os.path.exists(ssl_keyfile) and os.path.exists(ssl_certfile):
        print("Starting server with HTTPS...")
        print(f"Access your API at: https://localhost:8443")
        print(f"API Documentation at: https://localhost:8443/docs")
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8443,  # Standard HTTPS port
            reload=True,
            log_level="info",
            ssl_keyfile=ssl_keyfile,
            ssl_certfile=ssl_certfile
        )
    else:
        print("Starting server with HTTP...")
        print("To enable HTTPS:")
        print("1. Run: python main.py --generate-ssl")
        print("2. Or set SSL_KEYFILE and SSL_CERTFILE environment variables")
        print(f"Access your API at: http://localhost:8000")
        print(f"API Documentation at: http://localhost:8000/docs")
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )
