import bcrypt

def hash_password(password: str) -> bytes:
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(stored_hash: bytes, password: str) -> bool:
    """Check if a password matches the stored hash."""
    return bcrypt.checkpw(password.encode(), stored_hash)
