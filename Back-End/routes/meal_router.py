import sqlite3
from fastapi import Form, HTTPException, File, APIRouter, Depends, Request, UploadFile, status
from fastapi.responses import JSONResponse
import queries
from db import get_db
from models.post.mealRequest import MealRequest
from uuid import uuid4
import requests
import json 
import dotenv
import os
from dotenv import load_dotenv, find_dotenv

router = APIRouter()

@ router.get("/")
async def get_players(request: Request):
    query_params = request.query_params
    db = get_db()
    cursor = db.cursor()
    if "fromdate" and "todate" in query_params:
        cursor.execute(queries.get_meal_by_date,
                       (query_params['fromdate'], query_params['todate']))
        items = cursor.fetchall()

    cursor.close()
    return items

@ router.get("/{meal_id}")
async def get_team(meal_id: str):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(queries.get_meal_by_id, (meal_id))
    items = cursor.fetchall()
    cursor.close()

    return items

@ router.post("/")
async def create_player(meal: MealRequest):
    print(meal)
    db = get_db()
    cursor = db.cursor()
    try:
        db.execute('BEGIN')
        data = (meal.userId, meal.mealName,
                meal.calories, meal.description, meal.mealDate)
        print(data)
        db.execute(queries.post_meal, (data))
        db.commit()

    except sqlite3.Error as e:
        db.rollback()
        print("Create match error", e)
        return JSONResponse(content={"message": "Error creating player"}, status_code=500)
    cursor.close()
    return JSONResponse(content="", status_code=200)