#count = 0
#for number in range(1,10):
    #if number % 2== 0:
        #count += 1
        #print(number)
#print(f"We have {count} even numbers")

weight = int(input("Weight: "))
user_input = input("(K)g or (L)bs: ")
if user_input == "K":
    print(f"Weight in Kg: {weight/0.45:.1f}")
if user_input == "L":
    print(f"Weight in Lbs: {weight*0.45:.1f}")
