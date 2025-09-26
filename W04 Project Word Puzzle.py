print("Welcome to the word guessing game!")
guess = ""
guess_count = 0
word = "dog"

while guess != word:
    guess = input("What is your guess? ")
    guess_count += 1

    hint = "_"*len(word)
    for i in range(len(word)):
        if guess[i] == word[i]:
            hint += guess[i]
        else:
            hint += "_"
    print(f"Your hint is: {hint} ({len(word)})")
    
    if (len(guess)) != (len(word)):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    elif guess != word:
        print("Your guess was not correct.")
    else:
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")