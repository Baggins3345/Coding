# This project was a lot of fun! I wanted to make it my own and got it to work pretty good with some added touches. First I added a while loop inside adding an item
# so the user can just keep adding items till they don't want to. I added the remove option in the shopping cart area for ease of use, might as well ask while there.
# I also added some formating with ("-"*20) just to seperate some stuff. Also some simple stuff like "There is nothing here, try adding some items." while looking at
# the cart with no items in it. I did not need ChatGPT for much, just for waling me through some errors, but eveything was me, ChatGPT can be real dumb sometimes so
# I take eveything it says with a drop of silicon. The most I do is ask it what I am doing wrong and don't give me the answer just walk me through it and I figure it 
# out as it does.


print("Welcome to the Shopping Cart Program!")
shopping_list = []
prices = []
quit_ = False

while not quit_:
    user_choice = (input("""Please select one of the following:
1. Add a new item
2. Shopping cart
3. Remove an item  
4. Total
5. Quit                      
Please enter an action: """))
    if user_choice == "5":
        print("-"*20)
        print("Thank you. Goodbye.")
        print("-"*20)
        quit_ = True
        break
    elif user_choice == "1":
        new_item = ""
        while new_item != "done":
            print("-"*20)
            new_item = input("What is the new item? 'done' to go back: ")
            if new_item == "done":
                print("-"*20)
                continue
            item_price = float(input(f"What is the price of '{new_item}'? "))
            if new_item != "done":
                shopping_list.append(new_item)
                prices.append(item_price)
                print(f"'{new_item}' has been added to the cart.")
    elif user_choice == "2":
        print("-"*20)
        print("The contents of the shopping cart are:")
        if len(shopping_list) < 1:
            print("There is nothing here, try adding some items.\n")
            continue
        for i in range(len(shopping_list)):
            items = shopping_list[i]
            price = prices[i]
            print(f"{i + 1}. {items} - ${price:.2f}".upper())
        print("-"*20)
        user_choice = input("Would you like to remove an item (yes/no)? ")
        if user_choice == "yes":
            remove_item = int(input("Which item would you like to remove? "))-1
            if 0 <= remove_item < len(shopping_list):
                shopping_list.pop(remove_item)
                prices.pop(remove_item)
        else:
            print("Invalid item number.")
        print("-"*20)
    elif user_choice == "3":
        print("-"*20)
        print("The contents of the shopping cart are:")
        if len(shopping_list) < 1:
            print("There is nothing here, try adding some items.\n")
            continue
        for i in range(len(shopping_list)):
            items = shopping_list[i]
            price = prices[i]
            print(f"{i + 1}. {items} - ${price:.2f}".upper())
        print("-"*20)
        remove_item = int(input("Which item would you like to remove? "))-1
        if 0 <= remove_item < len(shopping_list):
            shopping_list.pop(remove_item)
            prices.pop(remove_item)
        else:
            print("Invalid item number.")
    elif user_choice == "4":
        print("-"*20)
        print(f"The total price of the items in the shopping cart is ${sum(prices):.2f}")
        print("-"*20)
    else:
        print("-"*20)
        print("That input is not supported please try again")
        print("-"*20)


