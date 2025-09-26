# fruits = ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]


# for items in groceries:
#     for item in items:
#         print(item)


# num_pad = ((1, 2, 3),
#            (4, 5, 6),
#            (7, 8, 9),
#            ("*", 0, "#"))

# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()



# Python quiz game

# Tuple of questions for the quiz
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in the Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet is the hottest?: ")

# 2D Tuple of multiple-choice options for each question
options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
           ("A. 206", "B. 207", "C. 208", "D. 209"),
           ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# Tuple of correct answers corresponding to each question
answers = ("C", "D", "A", "A", "B")

# List to store the user's guesses
guesses = []

# Initialize the user's score
score = 0 

# Index to track the current question number
question_num = 0

# Loop through each question in the questions tuple
for question in questions:
    print("-"*20)  # Print a separator
    print(question)  # Display the question

    # Display the answer choices for the current question
    for option in options[question_num]:
        print(option)

    # Get the user's guess and convert it to uppercase
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)  # Store the guess in the guesses list

    # Check if the guess is correct
    if guess == answers[question_num]:
        score += 1  # Add one point to the score
        print("-"*20)
        print("CORRECT!")  # Feedback for correct answer
    else:
        print("-"*20)
        print("INCORRECT!")  # Feedback for wrong answer
        print(f"{answers[question_num]} is the correct answer")  # Show correct answer

    question_num += 1  # Move to the next question

# Quiz is over, now show results
print("-"*20)
print("     RESULTS")
print("-"*20)

# Display correct answers
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

# Display user's guesses
print("Guess: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Calculate the final score as a percentage
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")  # Display the score
