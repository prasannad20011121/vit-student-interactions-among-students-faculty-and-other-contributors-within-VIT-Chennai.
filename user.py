from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from database import user_collection
import models
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/register")
async def create_user(user: models.User):
    user.password = pwd_context.hash(user.password)
    await user_collection.insert_one(user.dict())
    return {"msg": "User created successfully"}

@router.get("/users/{username}")
async def read_user(username: str):
    user = await user_collection.find_one({"username": username})
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")
