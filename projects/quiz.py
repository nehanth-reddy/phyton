print('welcome to the quiz game')
playing=input('do you want to play: ').strip().lower()

if playing != 'yes':
    quit()
    
print("okay! let's play :)")

def cpu():
    answer = input("what does cpu stand for ").strip().lower()
    if answer == "central processing unit":
        print("Correct")
    else:
        print('Incorrect')
        return cpu()
    
cpu()