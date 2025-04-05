from pydantic import BaseModel
from fastapi import Form, File, UploadFile, Request, FastAPI

class MealRequest(BaseModel):
    userId: int
    mealName: str 
    calories: int
    description: str
    mealDate: str