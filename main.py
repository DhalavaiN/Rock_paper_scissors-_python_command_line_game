import random


#Choice function returns the choice for rock paper scissor

def choice():
    #Ask player choice as input
    player_choice=input("Enter your choice(rock,paper, scissors)=")
    possible_choices=["rock","paper","scissors"]
    #Randomly Genetrate the computer choice using random function
    computer_choice=random.choice(possible_choices)
    choice={"player":player_choice,"computer":computer_choice}

    return choice

#The win function checks for the winning choice

def win(player,computer):
    if(player==computer):
        return "It's a Tie, Better Luck Next Time"
    else:
        if(computer=="rock"):
            if(player=="paper"):
                return "Paper Covers Rock, You win!"
            else:
                return "Rock Crushes Scissor, You Lose *_* "
        if(computer=="paper"):
            if(player=="scissors"):
                return "Scissor Cuts Paper, You win!"
            else:
                return "Paper Covers Rock, You Lose *_* "
        if(computer=="scissors"):
            if(player=="rock"):
                return "Rock Crushes Scissor, You win!"
            else:
                return "Scissor Cuts Paper, You Lose *_* "

#Function calling and Execution
result=choice()
print(win(result["player"],result["computer"]))
