import random

user_wins=0
computer_wins=0

options=["rock","paper","scissor"]

while True:
    #Take then user input and convert the input into lower case
    user_input=input("Choose between Rock/Paper/Scissor or q for quit").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue

     #0:Rock,1:Paper,2:Scissor
    random_num=random.randint(0,2)
    computer_picks=options[random_num]
    print("Computer Picked",computer_picks)

    if user_input=="paper" and computer_picks =="rock":
        print("You Won")
        user_wins+=1
    elif user_input=="scissor" and computer_picks =="paper":
        print("You Won")
        user_wins+=1
    elif user_input=="rock" and computer_picks =="scissor":
        print("You Won")
        user_wins+=1
    else:
        print("You lost")
        computer_wins+=1
print("You Wins",user_wins,"times.")
print("Computer Wins",computer_wins,"times.")
print("Thankyou")
