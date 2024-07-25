def calculator(number):
    if number == 1:
        multiplication()
    elif number == 2:
        division()
    elif number == 3:
        addition()
    elif number == 4:
        subtraction()
    elif number == 5:
        square()
    else:
        print()
        print(f"please try again, only numbers 1 through 5")
        main()

def multiplication():
    try:
        a = int(input("what's the first number: "))
        b = int(input("what's the second number: "))
        print(f" {a} times {b} is: {a*b}")
    except:
       ValueError
       print("numbers only, retry again")
       return multiplication()
        
def division():
    try:
        a = int(input("what's the first number: "))
        b = int(input("what's the second number: "))
        print(f" {a} divided by {b} is: {a/b}")
    except:
       ValueError
       print("numbers only, retry again")
       return division()
    
def addition():
    try:
        a = int(input("what's the first number: "))
        b = int(input("what's the second number: "))
        print(f" {a} + {b} is: {a+b}")
    except:
       ValueError
       print("numbers only, retry again")
       return addition()

def subtraction():
    try:
        a = int(input("what's the first number: "))
        b = int(input("what's the second number: "))
        print(f" {a} minus {b} is: {a-b}")
    except:
       ValueError
       print("numbers only, retry again")
       return subtraction()

def square():
    try:
        a = int(input("what's the first number: "))
        print(f"{a} square is: {a*a}")
    except:
       ValueError
       print("numbers only, retry again")
       return square()

def main():
    try:
        print("1 = multiply")
        print("2 = divide")
        print("3 = add")
        print("4 = subtract")
        print("5 = square")
        calculator(int(input( "which type of calculation: ")))
    except ValueError:
        print("numbers only")
        main()      
if __name__ == "__main__":
    main()