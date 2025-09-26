user_input = int(input("How many times?: "))

for i in range (1, user_input):
    print(i + 1)
    for j in range(user_input):
        print(j, end = "  ")
    print('')