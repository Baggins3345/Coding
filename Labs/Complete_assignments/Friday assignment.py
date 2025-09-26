#num = eval(input("Enter a number"))
#if num < 100:
    #print (f"{num} you enter is less than 100")
#elif num > 100:
    #print(f"{num} you enter is greater than 100")
#else: 
    #print (f"{num} is 100")


import random
num1 = random.randint(1,50)
num2 = random.randint(1,50)
num3 = random.randint(1,50)
num4 = random.randint(1,50)
num5 = random.randint(1,50)
largest = max(num1, num2, num3, num4, num5)
smallest = min(num1, num2, num3, num4, num5)

choice = int(input("Enter 1 to spin the wheel for a prize"))

if choice == 1:

    if num1 == largest:
        print(f"You win ${largest}")
    if num2 == largest:
        print(f"You win ${smallest}")
    if num3 == largest:
        print(f"You win ${largest - smallest}")
    if num4 == largest:
        print("You win $5 CAD")
    if num5 == largest:
        print("You win $1 CAD")
else: 
    print("Wrong input, please try again.")