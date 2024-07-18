from cryptography.fernet import Fernet
import pickle
import os

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.passwords = {}
        self.key = self.load_or_generate_key()
        self.fernet = Fernet(self.key)

    def load_or_generate_key(self):
        key_file = "secret.key"
        if os.path.exists(key_file):
            with open(key_file, "rb") as f:
                key = f.read()
        else:
            key = Fernet.generate_key()
            with open(key_file, "wb") as f:
                f.write(key)
        return key

    def encrypt_password(self, password):
        return self.fernet.encrypt(password.encode())

    def decrypt_password(self, encrypted_password):
        return self.fernet.decrypt(encrypted_password).decode()

    def save_password(self, account_name, password):
        encrypted_password = self.encrypt_password(password)
        self.passwords[account_name] = encrypted_password
        self.save_to_file()

    def get_password(self, account_name):
        if account_name in self.passwords:
            encrypted_password = self.passwords[account_name]
            return self.decrypt_password(encrypted_password)
        else:
            return None

    def save_to_file(self):
        with open("passwords.pkl", "wb") as f:
            pickle.dump(self.passwords, f)

    def load_from_file(self):
        if os.path.exists("passwords.pkl"):
            with open("passwords.pkl", "rb") as f:
                self.passwords = pickle.load(f)

    def validate_master_password(self, input_password):
        return input_password == self.master_password

def main():
    input_password = input("Enter master password: ")
    password_manager = PasswordManager("1234")

    # Validate master password
    if not password_manager.validate_master_password(input_password):
        print("Invalid master password. Access denied.")
        return

    # Load existing passwords from file if available
    password_manager.load_from_file()

    while True:
        print("\nOptions:")
        print("1. Add/Update Password")
        print("2. Retrieve Password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account_name = input("Enter account name: ")
            account_password = input("Enter account password: ")
            password_manager.save_password(account_name, account_password)
            print("Password saved successfully!")

        elif choice == "2":
            account_name = input("Enter account name: ")
            password = password_manager.get_password(account_name)
            if password:
                print(f"Password for {account_name}: {password}")
            else:
                print(f"No password found for {account_name}")

        elif choice == "3":
            password_manager.save_to_file()
            print("Exiting password manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()