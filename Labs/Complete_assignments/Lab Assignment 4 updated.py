#this is where the assignment starts
#Benjamin Strong
#153481

kilo = int(input("How many kilograms do you want to convert?: "))
user_input = input("Choose (p)ounds, (g)rams, or (o)unces: ")
if user_input == "p":
    p = kilo * 2.205
    print (f"{kilo} Kilograms is {p:.1f} pounds.")
elif user_input == "g":
    g = kilo * 1000
    print (f"{kilo} Kilograms is {g:.1f} pounds.")
elif user_input == "o":
    o = kilo *35.274
    print (f"{kilo} Kilograms is {o:.1f} pounds.")
else:
    print("There was an error made in this choice.")
