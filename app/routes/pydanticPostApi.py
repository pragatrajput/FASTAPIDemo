from fastapi import APIRouter
from pydantic import BaseModel

userData = APIRouter(prefix="/userData")

class Address(BaseModel):
    address: str
    
class User(BaseModel):
    name: str
    age: int 
    address: Address
    


@userData.post("/")
async def create_userData(user: User):
    return {"message": "data created",
            "data": user}

