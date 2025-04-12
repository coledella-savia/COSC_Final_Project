# import auth
import queries

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
sessions = {}
thread_local = local()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(meal_router, prefix="/meals", tags=["meals"])
