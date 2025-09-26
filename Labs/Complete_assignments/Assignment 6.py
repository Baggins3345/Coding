#Benjamin Strong
#153481
#March, 08, 2024

import random

#initialize the counters
prob_done = 0
prob_won = 0

#asking to start the game
user_input = input("Do you want a problem to solve? (y/n): ")
    
while user_input == "y":
    prob_done += 1
    
    #setting the ranges for each value
    w = random.randint(21,30)
    x = random.randint(5,9)
    y = random.randint(17,20)
    z = random.randint(10,15)

    #the actual answer for each equation
    answer = (w + x) * (y - z)

    user_answer = int(input(f"\nWhat is ({w} + {x}) * ({y} - {z})?: "))
    if user_answer == answer:
        print("\nCorrect!\n")
        prob_won += 1
    else:
        print(f"\nSorry the correct answer is {answer}\n")

    #calculating the total wins, problems and percentage of wins
    percent_won = (prob_won / prob_done) * 100
    print(f"Total wins: {prob_won}")
    print(f"Total problems: {prob_done}")
    print(f"Percentage won: {percent_won:.1f}%")

    user_input = input("\nWould you like another probelem to solve? (y/n): ")

print("\nUnderstandable, have a nice day!")
