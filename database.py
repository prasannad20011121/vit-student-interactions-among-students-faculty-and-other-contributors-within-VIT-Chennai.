from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")
database = client.vit_db
user_collection = database.get_collection("users")
assignment_collection = database.get_collection("assignments")
feedback_collection = database.get_collection("feedbacks")
