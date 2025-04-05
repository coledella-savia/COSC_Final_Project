import bcrypt
import secrets
import string
# from models import Session


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


def validate_token(sessions: dict[str, Session.Session], token):
    if token in sessions:
        if not sessions[token].is_expired():
            return sessions[token]
    return None