import random
print("Welcome to the word guessing game!")


play = True

while play:
    word_list = ["nephi", "mosiah", "temple", "dog", "cat", "zion", "book of mormon", "spirit", "game"]
    secret = random.choice(word_list)
    guess_num = 0
    hint_len = len(secret)
    print(f"Your hint is: {"_ " * hint_len} ({len(secret)})")
    guess = ""
    

    while guess != secret:
        guess = input("What is your guess? ")
        guess_num += 1
        hint = ""

        if guess == secret:
            print("Congratulations! You guessed it!")
            print(f"It took you {guess_num} guesses.")
            play = input("Would you like to play again (yes/no)? ")
            if play == "no":
                print("Goodbye!")
                exit()
        elif len(guess) != len(secret):
            print(f"Sorry, the guess must have the same number of letters as the secret word. ({len(secret)})")
            continue
        elif guess != secret:
            for i in range(len(secret)):
                if guess[i] == secret[i]:
                    hint[i] = guess[i].upper() , " "
                elif guess[i] in secret:
                    hint[i] = guess[i].lower() , " "
                else:
                    hint[i] = "_ "
        print(f"Your hint is: {" ".join(hint)} ({len(secret)})")

