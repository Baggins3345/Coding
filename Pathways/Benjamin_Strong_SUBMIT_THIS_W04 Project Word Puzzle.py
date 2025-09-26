# Boy this one took me a while! So I got ChatGPT to write out a random list of words for me to randomly choose from so its more fun. I could've wrote them
# Myself, but I am too smart to do that haha. Then added the random.choice to the hidden_word variable. Also added the length of the hidden word right after the hint
# I also added a while loop to ask the user if they want to play again. Added a simple print statment for when the user gets the hidden word in 1 try.

import random
print("Welcome to the word guessing game!")
play = "yes"
word_list = [
    "nephi", "lamoni", "ablish", "samuel", "zion", "gospel",
    "temple", "sabbath", "israel", "prophet", "prayer", "planet", "beacon",
    "hammer", "jungle", "pickle", "camera", "button", "mirror", "dollar",
    "laptop", "orange", "monkey", "cipher", "jaguar", "gimmic", "knaves",
    "quiver", "murmur", "baffle", "rhythm", "magma", "wreath"
]

while play == "yes":
    
    hidden_word = random.choice(word_list)
    guess_amount = 0
    hint = "_ " * len(hidden_word)
    user_guess = ""
    # I add the hidden word for playtest purposes, I would take this out 
    # in normal game play
    print(f"Your hint is: {hint} ({len(hidden_word)}) ({hidden_word})")
    while user_guess != hidden_word:
        user_guess = input("\nWhat is your guess? ")
        guess_amount += 1
        if user_guess == hidden_word:
            print("Congratulations! You guessed it!")
            if guess_amount == 1:
                print(f"You got it in 1 try!")
            else:
                print(f"It took you {guess_amount} tries.")
            play = input("Would you like to play again? (yes/no): ")
            if play == "no":
                print("Thank you for playing!")
                break
            else:
                play = "yes"
        elif len(user_guess) != len(hidden_word):
            print("Sorry, the guess must have the same number of letters as the secret word.")
            print("Try again")
        else:
            print("Try again")

    # This whole section with the for loops messed me up! I tried my best to get it myself but I used chatGPT to help walk me through it. I didn't just get it to 
    # write the code for me, but it helped me understand what I was doing wrong and how to make it better. I wasn't addind to hint, just changing it each time,
    # I wasn't using elif, just if (go me), and I had hidden_index = hidden_word[index] in a seperate line completley, I was just confusing myself. 
            # Reset hint variable for each new guess so we don't croud the hints
            hint = ""
            # Go into a for loop to iterare through the letters in the guess
            for index in range(len(user_guess)):
                # Have each letter in the guess word and the secret word have an index number
                user_index = user_guess[index]
                hidden_index = hidden_word[index]
                # If that idex number of the guess word matches with the same one in the secret word
                # Then hint gets updated with the letter uppercase
                if user_index == hidden_index:
                    hint += hidden_index.upper() + " "
                # If letter index is in the word, then lowercase
                elif user_index in hidden_word:
                    hint += user_index.lower() + " "
                # Otherwise, just do a "_ "
                else:
                    hint += "_ "
            print(f"Your hint is: {hint} ({len(hidden_word)})")
            print()