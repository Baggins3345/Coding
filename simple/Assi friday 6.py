user_input = int(input("Enter a number between 10 and 50: "))

if user_input <= 10 or user_input >= 50:
    print("Number you entered is not valid.")
elif user_input > 10:
    print("Number you entered is greater than 10")
    if user_input > 20:
        print("It is also greater than 20")
        if user_input > 30:
            print("It is also greater than 30")
            if user_input > 40:
                print("It is also greater than 40")



