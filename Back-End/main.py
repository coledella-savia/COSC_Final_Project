# import auth
import queries
import auth
from auth import get_sessions
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from db import get_db
#from models import Credentials
from fastapi import FastAPI, Depends, HTTPException, Request
from threading import current_thread, local

# Routes
from routes.users_router import router as user_router
from routes.meal_router import router as meal_router


app = FastAPI()
thread_local = local()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Or whatever your Vue dev server URL is
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@ app.get("/sessions")
async def get_connected_sessions():
    return get_sessions()

@ app.post("/refresh")
async def check_for_session_token(request: Request):
    # Check if user is already authorized
    session_info = validate_token(request)
    if (session_info is not None):
        return JSONResponse(status_code=200, content={"User": session_info.username})

    return JSONResponse(status_code=400, content={"message": "No session token"})

def validate_token(request: Request):
    if (request.cookies.get("session_token")):
        return auth.validate_token(auth.sessions, request.cookies.get("session_token"))
    return None


def remove_token(request: Request):
    return auth.sessions.pop(request.cookies.get("session_token"))


def get_user_id_from_session(session_token):
    if session_token in auth.sessions:
        return auth.sessions[session_token]["user_id"]
    else:
        return None

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(meal_router, prefix="/meals", tags=["meals"])


