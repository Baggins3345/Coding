
capacity = 200  # Capacity of the store
num_checks = int(input("Enter how many capacity checks there are: "))

below_capacity = 0
at_capacity = 0
above_capacity = 0

for _ in range(num_checks):
        num_people = int(input("Enter the number of people in the store at a given time: "))

        if num_people < capacity:
            below_capacity += 1
        elif num_people == capacity:
            at_capacity += 1
        else:
            above_capacity += 1

print("Number of times below capacity:", below_capacity)
print("Number of times at capacity:", at_capacity)
print("Number of times above capacity:", above_capacity)