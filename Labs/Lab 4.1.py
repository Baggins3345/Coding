#Benjamin Strong
#153481
#Feb. 16. 2024

hour = int(input("Enter the hour the call was made (o - 23): "))
min = int(input("Enter the number of minutes spent on the phone: "))
#If our variable "hour" is less than or equal to 0, and less than 10, then the rate is $0.05
if hour >=0 < 10:
    rate = 0.05
    #If our variable "hour" is less than or equal to 10, and less than 19, then the rate is $0.10
if hour >= 10 < 19:
    rate = 0.10
    #If our variable "hour" is less than or equal to 19, and less than 24, then the rate is $0.20
if hour >=19 <24:
    rate = 0.20
#if the hour is greater than 23, then print the following
if hour > 23: 
    print("Invalid calling hour.")
#if it is less than 23, then print the following
else:
    print(f"Length of call:  {min} minutes.")
    print(f"Rate charged:  ${rate:.2f}")
    print(f"Total charge:  ${min*rate:.2f}")

