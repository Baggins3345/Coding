import random 
options = ["paper", "rock", "scissors"]

user = input("Rock, Paper, Scissors?: ").lower()

comp_choice = random.randint(1,3)

if user == comp_choice:
    print("Tie")
else:
    print("cont.")