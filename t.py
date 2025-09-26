start = float(input("Enter the start value for kilograms: "))
end = float(input("Enter the end value for kilograms: "))
step = float(input("Enter the step value for kilograms: "))

    # Print the table header
print(f"{'Kilograms':>10} {'Pounds':>10} {'Grams':>10} {'Ounces':>10}")
print("=" * 50)

    # Iterate over the range of kilograms
for kg in range(start, end, step):
    pounds = kg * 2.205
    grams = kg * 1000
    ounces = kg * 35.274

        # Print values in right-aligned format with one decimal place each
print(f"{kg:>10.1f} {pounds:>10.1f} {grams:>10.1f} {ounces:>10.1f}")

def range(start, stop, step):
    # Custom range function that supports floating-point step values
    while start < stop:
        yield start
        start += step