from cryptography.fernet import Fernet

def generate_key_for_user(user_id: str) -> None:
    """Generate a new encryption key for a user and save it to a file."""
    key = Fernet.generate_key()
    with open(f"{user_id}_key.key", "wb") as key_file:
        key_file.write(key)
    print(f"Key for user '{user_id}' generated and saved as '{user_id}_key.key'.")

def load_key(user_id: str) -> Fernet:
    """Load the encryption key from the file for a given user."""
    key_path = f"{user_id}_key.key"
    try:
        with open(key_path, "rb") as key_file:
            key = key_file.read()
        return Fernet(key)
    except FileNotFoundError:
        raise FileNotFoundError(f"Key file '{key_path}' not found. Please generate the key first.")
