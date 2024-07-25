def main():
    try:
        tip(float(input('how many $:')))
    except ValueError:
        print("numbers only")
        return main()
def tip(money):
    percentage = float(input("percentage: "))
    converter = percentage/100
    tipvalue = money*converter
    print(f"tip: ${tipvalue}")
    print(f"total: ${tipvalue+money}")
    
    
    
if __name__ == "__main__":
    main()