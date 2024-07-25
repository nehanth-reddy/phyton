import random

userwins = 0
computerwin = 0
options = ["rock", "paper", "scissors"]
while True:
    user_imput = input("type Rock/Paper/Scissors or type end to quit: ").strip().lower()
    if user_imput == "end":
        quit()
    
    elif user_imput not in  options:
        continue
    
    bot_answer = options[random.randint(0,2)]
    print(f"I chose {bot_answer}")
    
    if user_imput == options[2] and bot_answer == options[1]:
        print("you won")
        userwins +=1
        
    elif user_imput == options[0] and bot_answer ==options[2]:
        print("you won")
        userwins +=1
        
    elif user_imput == options[1] and bot_answer == options[0]:
        print("you won")
        userwins +=1  
    elif user_imput == bot_answer:
        print("tie")
    else:
        print("you lost")
        computerwin +=1
        