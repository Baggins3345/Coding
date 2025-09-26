#The {animal} then {verb4} towards the window and attacked my {relative} on its way out. 
# Finally it stoped and my family all decided to {verb5} the {animal} and then we all went to {place}. The end.

print("Answer each prompt to create a silly story.\n")
adjective = input("Adjective: ")
animal = input("Animal: ")
verb1 = input("Verb ending in 'ing': ")
verb2 = input("Verb: ")
verb3 = input("Verb: ")
verb4 = input("Verb, past tense: ")
verb5 = input("Verb: ")
exclamation = input("Eclamation: ")
relative = input("A relative: ")
place = input("A place to go to: ")


print("The story is:\n")
print(f"""The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {verb1} down the hallway. "{exclamation.title()}!" I yelled. But all
I could think to do was to {verb2} over and over. Miraculously,
that caused it to stop, but not before it tried to {verb3}
right in front of my family.The {animal} then {verb4} towards the window and attacked my {relative} on its way out. 
Finally it stoped and my family all decided to {verb5} the {animal} and then we all went to {place}. The end.""")