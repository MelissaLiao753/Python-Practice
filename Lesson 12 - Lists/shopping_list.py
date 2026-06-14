# =====================================================================
# PROJECT: Shopping List & Budget Tracker
# GOAL: Practice adding items to lists and calculating data from them.
# =====================================================================

# INITIALIZE YOUR LISTS
# TODO: Create an empty list called 'shopping_cart' to hold item names.
shopping_cart = []
# TODO: Create an empty list called 'price_list' to hold item prices.
price_list = []


# MAIN
# TODO Create an infinite while loop
while True:
    print("Hi! I'm your shopping list and budget tracker. I'll help you keep track of all of your items and the prices for them.")
    print("Shopping list : 0 items ")
    print("Current prices: Bananas ($4.99),  Milk ($5.99), Cinnamon Rolls ($7.50), Sushi ($12.99)")
    print("Your options are: 1. Add item to cart, 2. Remove item from cart, 3. Clear cart and restart, 4.View total and checkout")
    user_input = input("Which option do you choose? (1-4)")

    # Info for user
    # TODO Output info for user:
    # Current cart/shopping list
    # Current prices

    # TODO Output Options for user: 1. Add item to cart, 2. Remove item from cart, 3. Clear cart and restart, 4. View total and checkout
    # TODO Get user input (1-4) and save in variable

    # -----------------------------------------------------------------
    # OPTION 1: ADD ITEM 
    # -----------------------------------------------------------------
    # TODO Check if option 1
    if user_input == "1":
        item = input("What is the name of the item would you like to add to your cart?").strip().lower()
        shopping_cart.append(item)
        # TODO Ask user for the name of the item
        # TODO Add it to shopping list
        # TODO Add user for price of item
        item_price = input("What is the price of the item would you like to add to your cart?").strip().lower()
        price_list = float(item_price)
        shopping_cart.append(float(item_price))
        # TODO Change price into a float
        # TODO Add price to price list

    # -----------------------------------------------------------------
    # OPTION 2: REMOVE ITEM 
    # -----------------------------------------------------------------
    # TODO Else check if option 2
    elif user_input == "2":
        item = input("What is the name of the item would you like to remove from your cart?").strip().lower()
        index_num = shopping_cart.index(item)
        # TODO Ask user for the name of the item they want to remove
        # TODO Use .index() to get the index of the item and save in variable
        shopping_cart.pop(index_num)
        shopping_cart.remove(item)
        # TODO Remove the item from cart
        # TODO Remove the price (using its index) from the price list


    # -----------------------------------------------------------------
    # OPTION 3: CLEAR CART (Practice clearing a list)
    # -----------------------------------------------------------------
    # TODO Else check if option 3
    elif user_input == "3" and item in shopping_cart:
        shopping_cart.clear()
        price_list.clear()
        print("Your cart is now empty.")
        # TODO: Use the .clear() method on both lists to empty them out.
        # TODO Tell them their cart is empty.


    # -----------------------------------------------------------------
    # OPTION 4: CHECKOUT
    # -----------------------------------------------------------------
    # TODO Else check if option 4
    elif user_input == "4":
        total_cost = sum([price_list])
        print("RECEIPT:")
        print(shopping_cart)
        break
        # TODO Display the results
        # TODO Exit the loop (to exit the program)

    # -----------------------------------------------------------------
    # NO OPTION
    # -----------------------------------------------------------------
    # TODO Otherwise
    else:
        print("Your option isn't valid, please try again using a number (1-4).")
        # TODO Tell them that option isn't valid

# ====================================================================
# EXTENSION
# Add a budget to the list
# TODO Tell them if their cart is over budget
# TODO Recommend items to remove based on their price.

# =====================================================================
# EXPERT
# Change your program to use dictionaries so prices are connected to shopping items
# Display the cart in alphabetical order
# Add an option to display the cart in order of price.