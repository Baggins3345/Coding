# I had ChatGPT help me to figure out how to have the text relay like a video game one letter at a time — pretty cool.
# I also added an end game state where you can end the game at any time by typing LEAVE, which will cause the elif statement to happen.
# Then if you input a choice that the program didn't account for, it just says to restart... Which is a bit rudimentary, but I really don't want to mess with 
# loops and what not right now, just want to focus on if/else statments and other concepts we have just learned.
# I guess I went a little overboard with the choices, this was just so fun and I tried my best to keep to stuff I know, ChatGPT helped me a little
# But only with the text printing, I liked it so I kept it. I have 3 diffrent endings, and that can be up to you to find out if you'd like. 
# Other than that I added inputs, if, elif, else statments, even used for loops from ChatGPT, I had to add those where I wanted to so I implemented them myself
# I play tested this on my brother and my wife, my wife helped me find flaws in my code and my brother helped me find spelling errors

import time

text = """Welcome to your adventure! 
Will you survive or will your story be one of dread and despair?
You decide! All choices will be CAPITALIZED,
and at any time you can type LEAVE to exit the game. Let's begin!
"""
#This line of code is for the text to print in a cool letter by letter fashion, I have set the speed as really fast for test play purposes
for letter in text:
    print(letter, end='', flush=True)
    time.sleep(0.005)

story_intro = ("""\nYour story starts as you enter the forest in your small town.
You have heard of many ghost stories and kids getting lost
in this forest. Your friends have dared you to go alone. You're no pansy, so you go.
As you enter, you hear strange noises and rustling of leaves.
""")
for letter in story_intro:
    print(letter, end='', flush=True)
    time.sleep(0.005)

# User lower to make sure the user input is valid even with mixed caps, and strip to make sure the user input is valid even with spaces
choice1 = input("\nThe noises frighten you, do you RUN AWAY or KEEP WALKING? ").strip().lower()
if choice1 == "run away":
    print("\nYou stumble as you try to run out of the forest but make it out with your life, and a bruised ego. THE END")
    exit()
elif choice1 == "keep walking":
    print("\nYou trudge forward, not fearing what lies ahead...")
elif choice1 == "leave":
    print("\nYou don't make a choice in time and the birds and animals of the forest scare you into running away. THE END")
    exit()
else:
    print("That wasn't a valid choice. Try restarting the game and picking carefully next time.")

# Continuing the story
con1 = """\nAs you walk, you notice the forest starts to take on a cool tone of colors. The greens melt away into blues, and the sounds become more muffled as if 
underwater. You keep walking and stop near a tree that seems normal — until you look up and see that the top has transformed into seaweed and is flowing as if in water.
At the base of the tree, there is a hole. You believe you can enter this hole.
"""
for letter in con1:
    print(letter, end='', flush=True)
    time.sleep(0.005)

choice2 = input("\nDo you ENTER or KEEP WALKING? ").strip().lower()

if choice2 == "enter":
    print("\nYou enter through the tree...")
    result = """\nYou come out on the other side and enter another world. A world underwater, but you can breathe. There are fishes and other critters flying — or swimming — above you.
You walk further, gawking at the sights until you come across a fountain of water... 
"""
    for letter in result:
            print(letter, end='', flush=True)
            time.sleep(0.005)

    choice2_5 = input("\nDo you DRINK or WALK BACK OUT? ").strip().lower()
    if choice2_5 == "drink":
        result = """You cup your hands into the cool water, bringing it to your mouth, and question everything you have done up until this point.
As you drink, the liquid slithers down your throat and reaches the depths of your belly... Something comes alive inside you. You are shot back into darkness and see a vision.
In this vision, you see yourself flying high above the clouds as if swimming. You glide, and as you do so, you are pulled in a certain direction — and you realize it is towards your home...
Next thing you know, you wake up in your bed at home, no longer in a vision. Was it all a dream? you think, as suddenly you fall a half foot to your bed... Maybe it wasn't a dream after all.
                                                                  THE END.
"""
        for letter in result:
            print(letter, end='', flush=True)
            time.sleep(0.005)
        exit()
    elif choice2_5 == "walk back out":
        print("You walk back out of the tree and instead go around it...")
    else:
        print("That wasn't a valid choice. Try restarting the game and picking carefully next time.")
        exit()

elif choice2 == "keep walking":
    print("\nYou walk around the tree...")
elif choice2 == "leave":
    print("\nYou don't make a choice in time and the birds and animals of the forest scare you into running away. THE END")
    exit()
else:
    print("That wasn't a valid choice. Try restarting the game and picking carefully next time.")
    exit()

cont2 = """\nAs you walk around the tree, you come to see a big cabin... Was this here before? You see no lights on and nothing around, but something tells you
you should go to the cabin...
"""
for letter in cont2:
    print(letter, end='', flush=True)
    time.sleep(0.005)

choice3 = input("\nDo you WALK IN or GO HOME or go to the TREE? ").strip().lower()

if choice3 == "walk in":
    result = """As you walk into the cabin, the door opens with a creak... Silence. Darkness... Was this a good idea? You fumble around for a light switch until the lights 
attack you and you are blinded for a moment — until vision rushes back and you hear a loud 'SURPRISE' as you finally can see all around you are your friends — the ones who dared you.
Your heart settles as your birthday party begins. There was nothing weird about this forest after all... or was there?
                                                        THE END.
"""
    for letter in result:
        print(letter, end='', flush=True)
        time.sleep(0.005)
    exit()

elif choice3 == "tree":
    result = """You come out on the other side and enter another world. A world underwater, but you can breathe. There are fishes and other critters flying — or swimming — above you.
You walk further, gawking at the sights until you come across a fountain of water... 
"""
    for letter in result:
        print(letter, end='', flush=True)
        time.sleep(0.005)
    choice3_5 = input("\nDo you DRINK or WALK BACK OUT? ").strip().lower()
    if choice3_5 == "drink":
        result = """You cup your hands into the cool water, bringing it to your mouth, and question everything you have done up until this point.
As you drink, the liquid slithers down your throat and reaches the depths of your belly... Something comes alive inside you. You are shot back into darkness and see a vision.
In this vision, you see yourself flying high above the clouds as if swimming. You glide, and as you do so, you are pulled in a certain direction — and you realize it is towards your home...
Next thing you know, you wake up in your bed at home, no longer in a vision. Was it all a dream? you think, as suddenly you fall a half foot to your bed... Maybe it wasn't a dream after all.
                                                                  THE END.
"""
        for letter in result:
            print(letter, end='', flush=True)
            time.sleep(0.005)
        exit()
    elif choice3_5 == "walk back out":
        print("You walk back out of the tree and go home... ya pansy.")
        exit()
    else:
        print("That wasn't a valid choice. Try restarting the game and picking carefully next time.")
        exit()

elif choice3 == "leave":
    print("\nYou don't make a choice in time and the birds and animals of the forest scare you into running away. THE END")
    exit()
else:
    print("That wasn't a valid choice. Try restarting the game and picking carefully next time.")
    exit()