import random
top_of_range = input("please type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print('please type a number greater than zero')
        quit()
else:
    print('not a valid number. try again!!!')
    quit()
    
    
random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number:')
        continue
    
    if user_guess == random_number:
        print("correct")
        print("you got it in", guesses, "guesses")
        break
    
    elif user_guess > random_number:
        print("you were above the number!")
    else:
        print("you were below the number")