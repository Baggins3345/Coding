store_capacity = int(input("Enter the store capacity: "))
    
    # Get the number of capacity checks
num_checks = int(input("Enter the number of capacity checks: "))
    
    # Initialize counters
for i in range(10):
    below_capacity = i
    at_capacity = i
    above_capacity = i
    
    # Loop through each capacity check
for _ in range(num_checks):
    people_count = int(input("Enter the number of people in the store: "))
        
    
    # Display the results
print(f"Number of times below capacity: {below_capacity}")
print(f"Number of times at capacity: {at_capacity}")
print(f"Number of times above capacity: {above_capacity}")