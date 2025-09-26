store_cap = 200
num_checks = int(input("How many times is a store checked for capacity?: "))

#adding space between lines
print("   ")

below_capacity = 0
at_capacity = 0
above_capacity = 0

#making a range starting at 1 and incresing up to the users input plus 1 to be within the range
for i in range(1, num_checks + 1):
        people = int(input(f"How many people are in a store at inspection {i}?: "))
        
        if people < store_cap:
            below_capacity += 1
        elif people == store_cap:
            at_capacity += 1
        else:
            above_capacity += 1

#adding space between lines
print("    ")

print(f"Total checks with a store under capacity: {below_capacity}")
print(f"Total checks with a store at capacity: {at_capacity}")
print(f"Total checks with a store over capacity: {above_capacity}")


