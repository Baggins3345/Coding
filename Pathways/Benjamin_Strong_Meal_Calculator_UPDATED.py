# Compute the price of a meal as follows by asking for the price of child and adult meals, the number of each, 
# and then the sales tax rate. Use these values to determine the total price of the meal. 
# Then, ask for the payment amount and compute the amount of change to give back to the customer.

####STUFF I ADDED: I added an if/else statment asking the user if they would like to round up for charity. If y then they would get the amount rounded up using 
####the function math.ceil, then get the payment/change. If no we continue as normal and get the payment/change. 

import math

#Ask for adult# and amount
adult_num = int(input("How many adults are there? "))
adult_meal_price = float(input("What is the price for the adults? "))
#ask for children amount and price
child_num = int(input("How many children are there? "))
child_meal_price = float(input("What is the price for the children? "))

#this is the total amount for the childrens meals together
total_child_price = child_num * child_meal_price

#this is the total amount for the adults meals together
total_adult_price = adult_num * adult_meal_price

#Here is the subtotal and showing it to the user
subtotal_price = total_adult_price + total_child_price
print(f"Subtotal: ${subtotal_price:.2f}")

#Ask for the sales taxs whole number stored as float incase the amount is with a decimal 
sales_tax = float(input("What is the sales tax rate for each? "))

#Calculate the sales tax by addin the adult and child meals then mutiply the sales tax whole number divided by 100
sales_tax_rate = subtotal_price * (sales_tax/100)

#Calculating the total after sales tax and showing it to the user
total = sales_tax_rate + subtotal_price
print(f"Sales tax rate is: ${sales_tax_rate:.2f}")
print(f"The total is ${total:.2f}")
#Ask the user if they want to upcharge for donations
round_up_ask = input("Would you like to round up for charity (y/n)? ")
#The round up number from the total 
round_up = math.ceil(total)
#use an if else statment to see if the user says yes or no
#if yes, then the total is rounded up using the ceil function (use of lower to make sure the user can use Y and y)
if round_up_ask.lower() == "y":
    print(f"Your total is {round_up}")
    payment = float(input("What is the payment amount? "))
    #Now we subtract the payment from the new rounded up number
    change = payment - round_up
    #display the change for the user
    print(f"Change: ${change:.2f}")
#if no, we continue to the total 
elif round_up_ask.lower() == "n":
    payment = float(input("What is the payment amount? "))
    #Calculating the change from the amount paid
    change = payment - total
    print(f"Change: ${change:.2f}")



