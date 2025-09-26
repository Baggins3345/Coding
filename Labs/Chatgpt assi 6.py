import random

def main():
    # Initialize variables
    problems_won = 0
    problems_done = 0

    play_again = 'y'

    while play_again.lower() == 'y':
        problems_done += 1

        # Generate random values
        w = random.randint(21, 30)
        x = random.randint(5, 9)
        y = random.randint(17, 20)
        z = random.randint(10, 15)

        # Display the expression
        print(f"Solve the expression: ({w} + {x}) * ({y} - {z})")

        # Calculate the correct answer
        correct_answer = (w + x) * (y - z)

        # Get user's answer
        user_answer = int(input("Your answer: "))

        # Check user's answer
        if user_answer == correct_answer:
            print("Correct!")
            problems_won += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

        # Show stats
        print(f"Problems won: {problems_won}/{problems_done}")
        percentage_won = (problems_won / problems_done) * 100 if problems_done > 0 else 0
        print(f"Percentage of problems won: {percentage_won:.1f}%")

        play_again = input("Do you want to solve another problem? (y/n): ")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()




else:
        print("\nSorry wrong input, try again\n")