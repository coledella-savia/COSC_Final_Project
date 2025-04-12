from fastapi import APIRouter, HTTPException, status, Request, Depends
from fastapi.responses import JSONResponse
from models.post.userRequest import UserRequest
from db import get_db
from auth import hash_password, verify_password, generate_session_token
import queries
from uuid import uuid4

# Assuming you store sessions globally like in main.py
from main import sessions

router = APIRouter()

@router.post("/register")
async def register_user(user: UserRequest):
    db = get_db()
    cursor = db.cursor()

    # Check if user already exists
    cursor.execute(queries.get_user_by_name, (user.name,))
    if cursor.fetchone():
        cursor.close()
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash password and store salt + hash
    salt, hashed = hash_password(user.password)

    try:
        db.execute('BEGIN')
        cursor.execute(
            queries.create_user,
            (user.name, salt.decode(), hashed.decode(), user.WeightGoal, user.DailyCalorie)
        )
        db.commit()
    except Exception as e:
        db.rollback()
        cursor.close()
        raise HTTPException(status_code=500, detail="Error registering user")

    cursor.close()
    return JSONResponse(content={"message": "User registered successfully"}, status_code=201)

@router.post("/login")
async def login_user(user: UserRequest):
    db = get_db()
    cursor = db.cursor()

    cursor.execute(queries.get_user_credentials, (user.name,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    stored_salt, stored_hash = row[0], row[1]
    if not verify_password(stored_salt, stored_hash, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create a session token
    token = generate_session_token()
    sessions[token] = Session.Session(user.name)  # Assuming Session takes username
    return {"message": "Login successful", "token": token}
