
def main() :
    table = input(str("what table would you like to print: "))
    i=1
    try:
        while i != 11:
            print(f"{table} times {i} is {float(table)*i}")
            i = i+1
    except :
        ValueError
        print("please enter numbers only")
        return main()

