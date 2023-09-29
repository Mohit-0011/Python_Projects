import random

#Take Input for Snake Water Gun from user
user = int(input("Snake = 0\nWater = 1\nGun   = 2\nEnter Your Choice : "))

#Randomly select Snake Water Gun as Computer
comp = random.randint(0,2)
print("Computer Choose", comp)
#Evaluate Result and Print Score

Score = 0

#Creating a Function to Check Results

def result(user, comp):
    if user==comp:
        return 0 
    elif user==1 and comp==0 or user==2 and comp==1 or user==0 and comp==2:
        return -1
    else:
        return 1
    

Score = result(user,comp)
if (Score==0):
    print("It is a tie ,\nScore" ,Score ,"\nTry Again")

if (Score==1):
    print("You Won\n Score" , Score ,"\nTry Again")

if (Score==-1):
    print("You Loose!\nScore" , Score, "\nTry Again")