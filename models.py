from pydantic import BaseModel

class StoreItem(BaseModel):
    value: str
