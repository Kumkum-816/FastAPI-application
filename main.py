from fastapi import FastAPI, HTTPException
from models import StoreItem
from database import collection

app = FastAPI()

@app.post("/store/{key}")
async def store_value(key: str, item: StoreItem):
    """Stores a key-value pair in MongoDB."""
    if collection.find_one({"key": key}):
        raise HTTPException(status_code=400, detail="Key already exists")
    
    collection.insert_one({"key": key, "value": item.value})
    return {"message": "Stored successfully", "key": key, "value": item.value}

@app.get("/store/{key}")
async def get_value(key: str):
    """Retrieves the value for a given key from MongoDB."""
    result = collection.find_one({"key": key})
    if not result:
        raise HTTPException(status_code=404, detail="Key not found")
    
    return {"key": key, "value": result["value"]}

@app.delete("/store/{key}")
async def delete_value(key: str):
    """Deletes a key-value pair from MongoDB."""
    result = collection.delete_one({"key": key})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Key not found")

    return {"message": "Deleted successfully", "key": key}
