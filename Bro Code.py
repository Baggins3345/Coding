# Shopping Cart

foods = []
prices = []
total = 0 

while True:
    food = input("Enter the food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("-"*5, "YOUR CART", "-"*5)

for item in range(len(foods)):
    food_item = foods[item]
    price_item = prices[item]

    print(f"{food_item} - ${price_item}")

for price in prices:
    total += price

print(f"Your total is ${total:.2f}")