from art import art
import random

print("welcome to rock paper scissor game\n good luck")
while(True):
    user_picked = input("rock,paper or scissor?\n>")
    pc_picked = random.randint(0, 2)
    if(user_picked == "rock"):
        user_picked = 1
    elif(user_picked == "paper"):
        user_picked = 2
    elif(user_picked == "scissor"):
        user_picked = 3
    user_picked = int(user_picked)-1
    print(f"you picked \n{art[user_picked]}  \n")
    print(f"bot picks \n {art[pc_picked]}  \n")
    if(user_picked == 2 and pc_picked == 0):
        print("you lose")
    elif(pc_picked == 2 and user_picked == 0):
        print("you win")
    elif(pc_picked < user_picked):
        print("you win")
    elif(pc_picked == user_picked):
        print("draw")
    else:
        print("you lose")
