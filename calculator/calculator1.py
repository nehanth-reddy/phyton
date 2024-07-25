def calculator(number, a, b):
    if number == 1:
        multiplication(a, b)
    elif number == 2:
        division(a, b)
    elif number == 3:
        addition(a, b)
    elif number == 4:
        subtraction(a, b)
    elif number == 5:
        square(a)
    else:
        print("Please try again, only numbers 1 through 5")
        main()

def values():
    a = int(input("Enter the first value: "))
    b = int(input("Enter the second value: "))
    return a, b

def multiplication(c, d):
    print(f"{c} times {d} is: {c * d}")

def division(c, d):
    try:
        print(f"{c} divided by {d} is: {c / d}")
    except ZeroDivisionError:
        print("Cannot divide by zero. Please try again.")
        main()

def addition(c, d):
    print(f"{c} plus {d} is: {c + d}")

def subtraction(c, d):
    print(f"{c} minus {d} is: {c - d}")

def square(a):
    print(f"The square of {a} is: {a * a}")

def main():
    try:
        print("1 = multiply")
        print("2 = divide")
        print("3 = add")
        print("4 = subtract")
        print("5 = square")
        number = int(input("Which type of calculation: "))
        
        # For square, only one input is needed
        if number == 5:
            a = int(input("Enter the value to square: "))
        else:
            a, b = values()
        
        calculator(number, a, b)
    except ValueError:
        print("Numbers only. Please try again.")
        main()

if __name__ == "__main__":
    main()
