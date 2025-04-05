import sqlite3
from threading import current_thread, local

thread_local = local()

def get_db():
    if not hasattr(thread_local, "db"):
        thread_local.db = sqlite3.connect("Database/Calorie.db")
        thread_local.db.row_factory = sqlite3.Row
        print(f"connected to db on thread {current_thread()}")
    return thread_local.db