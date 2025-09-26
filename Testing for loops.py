



print("Welcome to the word guessing game!")
guess = ""
guess_count = 0
word = "mosiah"

while guess != word:
    for i in word:
        hint = "_"*(len(word))
    print("Your hint is:", hint)
    guess = input("What is your guess? ")
    guess_count += 1
    if (len(guess)) != (len(word)):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    elif guess != word:
        print("Your guess was not correct.")
    else:
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")