##num = int(input("Enter five numbers that are divisible by 5: "))
#for i in range (4):
    #if num % 5 == 0:
        #num = int(input("That's right! Enter another number: "))
    #else:
        #print("uh-oh!!")
        #break

num = int(input("Enter five numbers that are divisible by 5: "))

i = 0 

while i<4:
    if num % 5 == 0:
        i = i+1
        num = int(input("That's right! Enter another number: "))
    else:
        print("uh-oh!!")
        break