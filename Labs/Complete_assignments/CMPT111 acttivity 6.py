import random, sys
print("Let's play a little game\n \nRock, Paper, Scissors\n")

wins = 0
losses = 0
ties = 0

while True:
    while True:
        comp = ["ROCK", "PAPER", "SCISSORS"]
        print("{} Wins, {} Losses, {} Ties".format(wins, losses, ties))
        user_input = input("Enter your move: (R)ock (P)aper (S)issors or (Q)uit: ")

        if user_input == "Q":
            print("Thanks for playing!")
            sys.exit()

        if user_input.lower() == "R":
            print("Rock versus...")
            user_input = "ROCK"
        elif user_input.lower() == "P":
            print("Paper versus...")
            user_input = "PAPER"
        elif user_input.lower() == "S":
            print("Scissors versus...")
            user_input = "SCISSORS"
        
        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            computerMove = "ROCK"
        elif randomNumber == 2:
            computerMove = "PAPER"
        elif randomNumber == 3:
            computerMove = "SCISSORS"
        print(computerMove)



        yay = "You Win!"
        boo = "You Lose!"

        if user_input == computerMove:
            print("It\'s a tie!")
            ties += 1
        elif user_input == "ROCK" and computerMove == "SCISSORS":
            print(yay)
            wins += 1
        elif user_input == "PAPER" and computerMove == "ROCK":
            print(yay)
            wins += 1
        elif user_input == "SCISSORS" and computerMove == "PAPER":
            print(yay)
            wins += 1
        elif user_input == "ROCK" and computerMove == "PAPER":
            print(boo)
            losses += 1
        elif user_input == "PAPER" and computerMove == "SCISSORS":
            print(boo)
            losses += 1
        elif user_input == "SCISSORS" and computerMove == "ROCK":
            print(boo)
            losses += 1
        



