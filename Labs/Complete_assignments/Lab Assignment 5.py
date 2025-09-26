start = int(input("Enter the starting calue in kilograms: "))
end = int(input("Enter the ending value in kilograms: "))
step = int(input("Enter the step value: "))

print(f"{"Kilograms":>10} {"Pounds":>10} {"Grams":>10} {"Ounces":>10}")

for kg in range (start, end, step):
    pounds = kg * 2.205
    grams = kg * 1000
    ounces = kg * 35.274
    print(f"{kg:>10} {pounds:>10.1f} {grams:>10.1f} {ounces:>10.1f}")


