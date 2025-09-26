def function_a ():
    print("My first name is Benjamin.")
    print("My last name is Strong.")
    print("My faculty is IT.")
    print("My year is Second.")

def function_b ():
    print("This is my first initial")
    print("++++++++++++++++++++++++++++++++++++++++")
    print("+ BBBBBBBBBBBBBBBBB                    +")
    print("+ BBBBBBBBBBBBBBBBBBB                  +")
    print("+ BBBBBB         BBBBBBB               +")
    print("+ BBBBBB           BBBBBBB             +")
    print("+ BBBBBB            BBBBBBBB           +")
    print("+ BBBBBB           BBBBBBBB            +")
    print("+ BBBBBB          BBBBBBB              +")
    print("+ BBBBBB         BBBBB                 +")
    print("+ BBBBBB    BBBBBB                     +")
    print("+ BBBBBBBBBBBBBBB                      +")
    print("+ BBBBBBBBBBBBBBBBB                    +")
    print("+ BBBBBBBBBBBBBBB                      +")
    print("+ BBBBBB      BBBBBBBBB                +")
    print("+ BBBBBB        BBBBBBBBB              +")
    print("+ BBBBBB        BBBBBBBBBB             +")
    print("+ BBBBBB        BBBBBBBB               +")
    print("+ BBBBBB      BBBBBBBB                 +")
    print("+ BBBBBB     BBBBBBBB                  +")
    print("+ BBBBBBBBBBBBBBBBB                    +")
    print("++++++++++++++++++++++++++++++++++++++++")

print("Which function do you want to call?")
print("A. Lab Assignment 1, Program 1\nB. Lab Assignment 2, Program 2")
user_input = input("Enter your choice here: ")

if user_input == "A":
    function_a()
elif user_input == "B":
    function_b()