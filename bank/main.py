from key_management import load_key
from user_management import authenticate_user
from bank_operations import Add_money, Take_money, total, reset

def main():
    user_id = input("Enter user ID: ").strip()
    password = input("Enter password: ").strip()

    try:
        if authenticate_user(user_id, password):
            cipher_suite = load_key(user_id)
        else:
            print("Invalid credentials.")
            return
    except FileNotFoundError as e:
        print(e)
        return
    
    print("1 : Add money")
    print("2 : Take money")
    print("3 : View total")
    print("4 : Reset to 0")
    row = int(input("What would you like to do: "))
    call(row, user_id, cipher_suite)

def call(n, user_id, cipher_suite):
    if n == 1:
        Add_money(user_id, cipher_suite)
    elif n == 2:
        Take_money(user_id, cipher_suite)
    elif n == 3:
        total(user_id, cipher_suite)
    elif n == 4:
        reset(user_id, cipher_suite)
    else:
        print("Retry again")
        return main()

if __name__ == "__main__":
    main()
