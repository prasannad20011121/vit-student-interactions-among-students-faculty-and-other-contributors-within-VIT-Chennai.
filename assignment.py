from fastapi import APIRouter, Depends, HTTPException
from database import assignment_collection
import models

router = APIRouter()

@router.post("/assignments")
async def create_assignment(assignment: models.Assignment):
    await assignment_collection.insert_one(assignment.dict())
    return {"msg": "Assignment created successfully"}

@router.get("/assignments/{assignment_id}")
async def read_assignment(assignment_id: str):
    assignment = await assignment_collection.find_one({"_id": assignment_id})
    if assignment:
        return assignment
    raise HTTPException(status_code=404, detail="Assignment not found")
