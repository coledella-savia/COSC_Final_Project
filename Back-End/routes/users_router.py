from fastapi import APIRouter, Depends, HTTPException, Request
from pydantic import BaseModel
from sqlite3 import Connection
from fastapi.responses import JSONResponse
from db import get_db
from auth import hash_password, verify_password, generate_session_token, sessions, validate_token
from queries import register_user, get_user_by_name
from models.post.userRequest import UserRequest, LoginRequest

# Models
from models.Session import Session

router = APIRouter()

def get_cookie_validation(request: Request):
    if (request.cookies.get("session_token")):
        return validate_token(request.cookies.get("session_token"))
    return None

@router.post("/register")
def register_user_endpoint(user: UserRequest, db: Connection = Depends(get_db)):
    existing = db.execute(get_user_by_name, (user.name,)).fetchone()
    if existing:
        raise HTTPException(status_code=400, detail="Username already taken.")

    salt, hashed_password = hash_password(user.password)
    db.execute(register_user, (
        user.name,
        hashed_password.decode("utf-8"),
        user.height,
        user.age,
        user.gender,
        user.WeightGoal,
        user.DailyCalorie
    ))
    db.commit()

    return {"message": "User registered successfully."}


@router.post("/login")
async def login_user(request: Request):

    session_info = get_cookie_validation(request)
    print(session_info)
    if (session_info is not None):
        sessions.pop(request.cookies.get("session_token"))
    
    json_body = await request.json()
    creds = LoginRequest(name=json_body['name'], password=json_body['password'])

    db = get_db()
    cursor = db.cursor()
    user = db.execute(get_user_by_name, (creds.name,)).fetchone()
    cursor.close()

    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password.")

    user_id, stored_hash = user
    stored_salt = stored_hash[:29]

    if not verify_password(stored_salt, stored_hash, creds.password):
        raise HTTPException(status_code=401, detail="Invalid username or password.")

    token = generate_session_token()
    session_info = Session(creds.name)
    sessions[token] = session_info
    response = JSONResponse(content={
                            "User": user_id, "Token": token}, status_code=200)
    response.set_cookie(key="session_token", value=token,
                        expires=session_info.expiration_time, httponly=True, samesite="none", secure=True)
    print(response)
    return response

