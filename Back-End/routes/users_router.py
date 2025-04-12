from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlite3 import Connection
from db import get_db
from auth import hash_password, verify_password, generate_session_token
from main import sessions
from queries import register_user, get_user_by_name
from models.post.userRequest import UserRequest, LoginRequest

router = APIRouter()


@router.post("/register")
def register_user_endpoint(user: UserRequest, db: Connection = Depends(get_db)):
    existing = db.execute(get_user_by_name, (user.name,)).fetchone()
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken.")

    salt, hashed_password = hash_password(user.password)
    db.execute(register_user, (
        user.name,
        hashed_password.decode("utf-8"),
        user.WeightGoal,
        user.DailyCalorie
    ))
    db.commit()

    return {"message": "User registered successfully."}


@router.post("/login")
def login_user(login: LoginRequest, db: Connection = Depends(get_db)):
    user = db.execute(get_user_by_name, (login.name,)).fetchone()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password.")

    user_id, stored_hash = user
    stored_salt = stored_hash[:29]

    if not verify_password(stored_salt, stored_hash, login.password):
        raise HTTPException(status_code=401, detail="Invalid username or password.")

    token = generate_session_token()
    sessions[token] = {
        "user_id": user_id,
        "name": login.name
    }

    return {"token": token, "message": "Login successful"}

