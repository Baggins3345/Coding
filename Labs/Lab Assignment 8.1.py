num_prec = int(input("How many precipitations will be entered?: "))

all_prec = []
less_prec = []
above_prec = []
max_ml = 4


for i in range(num_prec):
    prec = int(input(f"Enter precipitations {i+1}: "))
    all_prec.append(prec)
    if prec < max_ml:
        less_prec.append(prec)
    else:
        above_prec.append(prec)

print(f"\nThe precipitations are {all_prec}")
print(f"\nPrecipitations below 4 mm: {less_prec}")
print(f"Lowest precipitation: {min(less_prec)}")

print(f"\nPrecipitations at least 4 mm: {above_prec}")
print(f"Highest precipitation: {max(above_prec)}")
