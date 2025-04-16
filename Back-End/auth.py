import bcrypt
import secrets
import string
from models import Session


sessions = {}

def hash_password(password):
    salt = bcrypt.gensalt()  # Generate a random salt
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)  # Hash the password
    return salt, hashed


def verify_password(stored_salt, stored_hash, entered_password):
    hashed = bcrypt.hashpw(entered_password.encode(
        "utf-8"), stored_salt.encode("utf-8"))
    return hashed == stored_hash.encode("utf-8")


def generate_session_token():
    characters = string.ascii_letters + string.digits

    # Generate a random session token with the specified length
    session_token = ''.join(secrets.choice(characters) for _ in range(32))

    return session_token


def validate_token(token):
    print(token)
    if token in sessions:
        if not sessions[token].is_expired():
            return sessions[token]
    return None

def get_user_id_from_session(session_token):
    if session_token in sessions:
        return sessions[session_token]["user_id"]
    else:
        return None
    
def get_sessions():
    return sessions
    

"""
session_token=TzoKOZEtjFAQWN01ZuR8b5w0F7lNVqEd; Path=/; Secure; HttpOnly; Expires=Tue, 15 Apr 2025 16:29:52 GMT;

"""