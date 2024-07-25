import os
from password_management import hash_password, check_password
from key_management import generate_key_for_user

def register_user(user_id: str, password: str) -> None:
    """Register a new user with a hashed password and a new encryption key."""
    # Hash and save the password
    hashed_password = hash_password(password)
    with open(f"{user_id}_password.hash", "wb") as password_file:
        password_file.write(hashed_password)
    
    # Generate and save the encryption key
    generate_key_for_user(user_id)

def authenticate_user(user_id: str, password: str) -> bool:
    """Authenticate a user by checking the provided password against the stored hash."""
    try:
        with open(f"{user_id}_password.hash", "rb") as password_file:
            stored_hash = password_file.read()
        return check_password(stored_hash, password)
    except FileNotFoundError:
        raise FileNotFoundError(f"Password file for user '{user_id}' not found. Please register first.")
