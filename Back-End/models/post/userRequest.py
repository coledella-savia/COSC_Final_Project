from pydantic import BaseModel

class UserRequest(BaseModel):
    name: str 
    password: str
    height: float
    age: int
    gender: str
    WeightGoal: float
    DailyCalorie: float

class LoginRequest(BaseModel):
    name: str
    password: str