from fastapi import FastAPI
from routes import auth, user, assignment, feedback

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/users")
app.include_router(assignment.router, prefix="/assignments")
app.include_router(feedback.router, prefix="/feedback")

@app.get("/")
async def root():
    return {"message": "Welcome to the VIT API"}
