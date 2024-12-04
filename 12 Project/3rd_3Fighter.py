Q1. Create a Normal Project where fight amoung 3 player. 
For Example: - Men, Robot, Water

import random

while True:   
    choices = ["Men", "Robot", "Water"]
             # Rock, Paper, Scissors

    computer = random.choice(choices)
    player = None
    
    while player not in choices:
       
        player = input("[Men, Robot, or Water] Pls Enter Any One:-").title()  # Convert input to title case
    
    if player == computer:
        print("Computer:", computer)
        print("Player:", player)
        print("Tie")
    
    elif player == "Men":           # Men vs Robot
        if computer == "Robot":
            print("Computer:", computer)
            print("Player:", player)
            print("You Lose!!")
        elif computer == "Water": 
            print("Computer:", computer)
            print("Player:", player)
            print("You Win!")
    
    elif player == "Water":         # Water vs Robot 
        if computer == "Men":
            print("Computer:", computer)
            print("Player:", player)
            print("You Lose!!")
        elif computer == "Robot":
            print("Computer:", computer)
            print("Player:", player)
            print("You Win!!")
    
    elif player == "Robot":         # Robot vs Men 
        if computer == "Water":
            print("Computer:", computer)
            print("Player:", player)
            print("You Lose!!")
        elif computer == "Men":
            print("Computer:", computer)
            print("Player:", player)
            print("You Win!!")      

    play_again = input("Play again? (Yes/No): ").lower()
    if play_again != "yes":
        break
print("Bye! Thanks for coming!")
