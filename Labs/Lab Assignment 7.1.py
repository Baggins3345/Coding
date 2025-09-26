start = int(input("Enter the starting calue in gallons: "))
end = int(input("Enter the ending value in gallons: "))
step = int(input("Enter the step value: "))

def gallons_quarts(gallons):
    return gallons *4
def gallons_pints(gallons):
    return gallons * 8
def gallons_liters(gallons):
    return gallons * 3.785

print(f"{"Gallons":>10} {"Quarts":>10} {"Pints":>10} {"Liters":>10}")
for gallons in range (start, end, -step):
    Quarts = gallons_quarts(gallons)
    Pints = gallons_pints(gallons) 
    Liters = gallons_liters(gallons)
    print(f"{gallons:>10} {Quarts:>10.1f} {Pints:>10.1f} {Liters:>10.1f}")


