import random
user_wins=0
computer_wins=0
tied=0
options=["rock", "paper", "scissors"]
while True:
    user_input=input("Type Rock/Paper/Scissors or Q to quit: ")
    if user_input.lower()=="q":
        break
    if user_input.lower() not in options:
        continue
    random_number=random.randint(0,2)
    #rock=0, paper=1, scissors=2
    computer_pick=options[random_number]
    print("Computer picked", computer_pick + ".")
    if user_input.lower()=="rock" and computer_pick.lower()=="scissors":
        print("You won!")
        user_wins+=1
    if user_input.lower()=="paper" and computer_pick.lower()=="rock":
        print("You won!")
        user_wins+=1
    elif user_input.lower()=="rock" and computer_pick.lower()=="rock":
        print("Tied")
        tied+=1
    elif user_input.lower()=="paper" and computer_pick.lower()=="paper":
        print("Tied")
        tied+=1
    elif user_input.lower()=="scissors" and computer_pick.lower()=="scissors":
        print("Tied")
        tied+=1
    else:
        print("You lost!")
        computer_wins+=1
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Total tied:", tied, "times.")
print("Goodbye!")