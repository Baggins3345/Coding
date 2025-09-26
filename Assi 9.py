print("This program asks user to enter 5 numbers and calculates the sum for them")
total = 0

for i in range(5):
    num = eval(input("Please enter a number: "))
    total = total + num

print("The sum of the 5 numbers is", total)
print("The average of 5 numbers is", total/5)