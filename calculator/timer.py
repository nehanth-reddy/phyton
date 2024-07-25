import time
def main():
    try:
        n = int(input("how many seconds: "))
        while n>0 :   
            print(n)
            n -= 1
            time.sleep(1)
        if n==0:
            print(n)
            print("time over")
            
    except ValueError:
        print("numbers only")
        return main()
        

if __name__ == "__main__":
    main()