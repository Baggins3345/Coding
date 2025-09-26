import random

roll = random.randint(1,6)

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_inx in range(players):
        print(f"\nPlayer {player_inx + 1} turn!\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)?: ")
            if should_roll.lower != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}")

            print(f"Your score is {current_score}")

        player_scores[player_inx] =+ current_score
        print(f"Your total score is {player_scores[player_inx]}")