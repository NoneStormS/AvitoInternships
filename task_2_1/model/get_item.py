from pydantic import BaseModel

class Statistics(BaseModel):
    contacts: int
    likes: int
    viewCount: int

class GetItem(BaseModel):
    createdAt: str
    id: str
    name: str
    price: int
    sellerId: int
    statistics: Statistics
    
