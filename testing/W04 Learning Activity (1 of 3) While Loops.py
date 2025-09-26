# number = -1

# while number < 0:
#     number = int(input("Please type a positive number: "))
#     if number < 0:
#         print("Sorry, that is a negative number. Please try again.")
#     else:
#         print(f"The number is: {number}")


# number = 0

# while number <= 0:
#     number = int(input("Please type a positive number: "))
#     if number < 0:
#         print("Sorry, that is a negative number. Please try again.")

# print(f"The number is: {number}")


# answer = False

# while answer == False:
#     answer = input("May I have a piece of candy? ").lower()
#     if answer == "yes":
#         answer = True
#     else:
#         answer = False
# print("Thank you.")


# answer = False

# while answer == False:
#     answer = input("May I have a piece of candy? ").lower()
#     if answer == "yes":
#         print("Thank you.")
#         answer = False
#     elif answer == "STOP".lower():
#         answer = True
#     else:
#         answer = False
# print("ok... sorry")




payment = float(input("What is the payment amount? "))


while payment < 0:
    print("Sorry the payment can't be negative.")

    payment = float(input("What is the payment amount? "))

print(f"The amount is ${payment}")
