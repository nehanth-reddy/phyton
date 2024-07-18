from sys import argv
def main() :
    table = argv[1]
    i=1
    try:
        while i != 11:
            print(f"{table} times {i} is {float(table)*i}")
            i = i+1
    except :
        ValueError
        print("please enter numbers only")
        return main()
    
main()

