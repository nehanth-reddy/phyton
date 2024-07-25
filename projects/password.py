from cryptography.fernet import Fernet

def load_key():
    with open("key.key", 'rb') as file:
        key = file.read()
        return key

master_pwd = input("What's the master password? ")
key = load_key()
fer = Fernet(key)

def add():
    name = input("Account name: ")
    pwd = input("Password: ")
    with open("passwords.txt", 'a') as file:
        file.write(f"{name} | {fer.encrypt(pwd.encode()).decode()}\n")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user, passw = data.split(" | ")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

while True:
    mode = input("Would you like to add a new password or view existing passwords (view/add) or type q to quit: ").strip().lower()
    
    if mode == "q":
        break
    elif mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print("Invalid mode.")
