from cryptography.fernet import Fernet
import os
import time
from key_management import load_key  # Import load_key from key_management

def encrypt_data(cipher_suite: Fernet, data: str) -> bytes:
    """Encrypt data using the provided cipher suite."""
    return cipher_suite.encrypt(data.encode())

def decrypt_data(cipher_suite: Fernet, encrypted_data: bytes) -> str:
    """Decrypt data using the provided cipher suite."""
    return cipher_suite.decrypt(encrypted_data).decode()

def ensure_file_exists(user_id: str) -> None:
    """Ensure the bank file exists; if not, create it with an initial balance of 0."""
    if not os.path.exists(f"{user_id}_bank.txt"):
        with open(f"{user_id}_bank.txt", "wb") as file:
            encrypted_zero = encrypt_data(load_key(user_id), "0")
            file.write(encrypted_zero)

def Add_money(user_id: str, cipher_suite: Fernet) -> None:
    """Add money to the user's bank file."""
    ensure_file_exists(user_id)
    with open(f"{user_id}_bank.txt", "rb+") as file:
        encrypted_data = file.read()
        decrypted_data = decrypt_data(cipher_suite, encrypted_data)
        m = int(decrypted_data)
        amount = int(input("How much would you like to add: "))
        total = m + amount
        print(f"Balance: ${total}")
        file.seek(0)
        encrypted_total = encrypt_data(cipher_suite, str(total))
        file.write(encrypted_total)
        file.truncate()

def Take_money(user_id: str, cipher_suite: Fernet) -> None:
    """Take money from the user's bank file."""
    ensure_file_exists(user_id)
    with open(f"{user_id}_bank.txt", "rb+") as file:
        encrypted_data = file.read()
        decrypted_data = decrypt_data(cipher_suite, encrypted_data)
        m = int(decrypted_data)
        amount = int(input("How much would you like to take: "))
        total = m - amount
        print(f"Balance: ${total}")
        file.seek(0)
        encrypted_total = encrypt_data(cipher_suite, str(total))
        file.write(encrypted_total)
        file.truncate()

def total(user_id: str, cipher_suite: Fernet) -> None:
    """Display the total balance."""
    ensure_file_exists(user_id)
    with open(f"{user_id}_bank.txt", "rb") as file:
        encrypted_data = file.read()
        decrypted_data = decrypt_data(cipher_suite, encrypted_data)
        total = int(decrypted_data)
        print(f"Balance: ${total}")

def reset(user_id: str, cipher_suite: Fernet) -> None:
    """Reset the bank file to an initial balance of 0."""
    warning = input("Erasing data, are you sure? Enter yes/no: ").strip().lower()
    if warning == "yes":
        print("Erasing data")
        time.sleep(2)
        ensure_file_exists(user_id)
        with open(f"{user_id}_bank.txt", "wb") as file:
            encrypted_zero = encrypt_data(cipher_suite, "0")
            file.write(encrypted_zero)
            print("Balance = $0")
    else:
        print("Not erasing")
        exit()
