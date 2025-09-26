#Benjamin Strong 153481
#March 20, 2024

#Asking for input form the user as starting values
start_kg = int(input("Enter the starting value in kilograms: "))
end_kg = int(input("Enter the ending value in kilograms: "))
step = int(input("Enter the step value: "))

print(f"\n{'Kilograms':>10} {'Pounds':>10} {'Grams':>10} {'Ounces':>10}")

#This loop if for the values counting down and not up
while start_kg >= end_kg:
    pounds = start_kg *2.205
    grams = start_kg * 1000
    ounces = start_kg * 35.274

    print(f"{start_kg:>10} {pounds:>10.1f} {grams:>10.1f} {ounces:>10.1f}")
    #This will allow the count down and not up
    start_kg -= step

