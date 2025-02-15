from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    username: str
    email: str
    password: str
    role: str  # 'Student', 'Faculty', 'Contributor'

class Assignment(BaseModel):
    title: str
    description: str
    file_url: str
    submitted_by: str

class Feedback(BaseModel):
    assignment_id: str
    feedback: str
    reviewed_by: str
