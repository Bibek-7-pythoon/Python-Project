print("Welcome to my Computer Quiz game 🙌")
print("You can only advance to next round if you answer questions correctly.")
rules=input("Enter ok if you accept the game rules: ")
if rules.lower()=="ok":
    print("Fairplay")
else:
    quit()
playing=input("Do you want to play? ")
if playing.lower() =="yes":
    print("Okay! Let's play the game 🤗")
else:
    quit()
score=0
answer=input("What does CPU stands for? ")
if answer.lower()=="central processing unit":
    print("Correct 👏")
    score+=1
else:
    print("Incorrect")
    quit()

answer=input("What does OOP stands for? ")
if answer.lower()=="object oriented programming":
    print("Correct 👏")
    score+=1
else:
    print("Incorrect")
    quit()

answer=input("What does RAM stands for? ")
if answer.lower()=="random access memory":
    print("Correct 👏")
    score+=1
else:
    print("Incorrect")
    quit()

answer=input("What does VScode stands for? ")
if answer.lower()=="visual studio code":
    print("Correct 👏")
    score+=1
else:
    print("Incorrect")
    quit()

answer=input("What does GPU stands for? ")
if answer.lower()=="graphics processing unit":
    print("Correct 👏")
    score+=1
else:
    print("Incorrect")
    quit()
print("You got " + str(score) + " questions correct!")
print("You got " + str(score/5*100) + " questions correct!")