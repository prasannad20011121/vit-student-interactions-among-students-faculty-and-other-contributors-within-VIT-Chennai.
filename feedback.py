from fastapi import APIRouter, HTTPException
from database import feedback_collection
import models

router = APIRouter()

@router.post("/feedback")
async def create_feedback(feedback: models.Feedback):
    await feedback_collection.insert_one(feedback.dict())
    return {"msg": "Feedback submitted successfully"}

@router.get("/feedback/{assignment_id}")
async def read_feedback(assignment_id: str):
    feedbacks = await feedback_collection.find({"assignment_id": assignment_id}).to_list(100)
    if feedbacks:
        return feedbacks
    raise HTTPException(status_code=404, detail="Feedback not found")
