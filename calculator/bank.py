import time

def main():
    # asks user what they would like to do
    print("1 : Add money")
    print("2 : Take money")
    print("3 : View total")
    print("4: reset to 0")
    # Takes input on what the user wants
    row = int(input("what would you like to do: "))
    #gives row to cal
    call(row)



def call(n):
    #checks on what to do with the balance
    if n == 1: 
        Add_money()
    elif n == 2:
        Take_money()
    elif n==3:
        total()
    elif n==4:
        reset()
    else:
        print("retry again")
        return main()
        
        
def Add_money():
    #does the following read money, get the money, change the value
    with open("bank.txt", "r+") as file:
        i = file.read()
        m = int(i)
        total = m + int(input("how much would you like to add: "))
        print(f"Balance: ${total}")
        file.seek(0)
        file.write(str(total))
        file.truncate()
def Take_money():
    #does the following read money, get the money, change the value
    with open("bank.txt", "r+") as file:
        i = file.read()
        m = int(i)
        total = m - int(input("how much would you like to add: "))
        print(f"Balance: ${total}")
        file.seek(0)
        file.write(str(total))
        file.truncate()
    
def total():
    #give the total
    with open("bank.txt", "r+") as file:
        i = file.read()
        total = int(i)
        print(f"Balance: ${total}")
        
def reset():
    warning = input("erasing data, are you sure. enter yes/no: ").strip().lower()
    if warning == "yes":
        print("erasing data")
        time.sleep(2)
        with open("bank.txt", "w") as file:
            file.write(str(0))
            print("Balance = $0")
    else:
        print("not erasing")
        exit
    
    
if __name__ == "__main__":
    main()