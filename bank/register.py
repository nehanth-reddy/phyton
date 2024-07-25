import os
from user_management import register_user

def register():
    user_id = input("Enter user ID: ").strip()
    password = input("Enter password: ").strip()

    if os.path.exists(f"{user_id}_password.hash") or os.path.exists(f"{user_id}_key.key"):
        print("User already exists. Please choose a different user ID.")
        return

    # Register the user
    register_user(user_id, password)
    print(f"User '{user_id}' registered successfully.")

if __name__ == "__main__":
    register()
