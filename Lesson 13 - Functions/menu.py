"""
PROGRAM: Menu
This starts with a menu so users can run 1 of 3 different programs:
1.
2.
3.
"""

# INSTRUCTIONS
# TODO Copy over the code from 3 of your other programs into their own function.
# TODO If you have any imports, make sure to move them out of the function to IMPORTS section 
# (everything else can stay in the functions)
# TODO Create a menu program in the main function and call each program function based on user input

#===============================
# IMPORTS
#===============================
import random

#===============================
# FUNCTIONS
#===============================

# Run program 1
def programme_1():

    responses = ["Yes", "No", "Maybe", "Likely", "Unlikely", "No way", "Certainly", "Ask again later"]
    #       8-ball answers (strings). There should be positive answers, negative answers and neutral answers.
    #       Examples: "Yes, definitely!", "Ask again later.", "Outlook not so good."


    # MAIN LOOP
    # TODO Create an infinite loop
    while 1 == 1:
        question = input("Ask a yes/no question to the magic 8 ball. Type exit to leave.").strip().lower()
        # TODO: Ask the user to type in a Yes/No question about their future and save it in a variable.
        #       (Or tell them to type 'quit' to leave).
        if question == "exit":
            break
        
        # Check if the user wants to exit and break from the loop if they do.
            
        # RANDOM REPSONSE
        # TODO: Step A: Calculate the last valid index of your list.
        #       (Remember: If a list has 5 items, the indexes are 0, 1, 2, 3, 4).
        #       Use random.randint() to get a number between 0 and that last index.
        #       Save it in a variable called 'random_index'.
        print(responses[random.randint(0,7)])
    main()

# Run program 2
def programme_2():
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
    main()


# Run program 3
def programme_3():
        # TODO Create a variable for valid input and set it to false
    valid_input = False
    # GET INPUT

    # TODO Start a loop while the input is invalid
    while not valid_input:
        age = input("How old are you?")
        
        # TODO Ask the user for their age and save it
        try:
            age_int = int(age)
            
            if age_int > 18:
                valid_input = True
            elif age_int > 13:
                print("You have partial access")
            else: 
                print("Your are not old enough.")
        except:
            valid_input = False
            print("Access has been denied")
    print("Welcome, you have full access.")
    main()
        #TRY

# Run main code
def main():
    user_input = input("Hi! Here's the menu, we have 1) Magic 8 Ball, 2) Shopping Cart, and 3) Spy Verification. Please choose one using numbers 1-3.").strip().lower()
    user_int = int(user_input)
    if user_int  == 1:
        programme_1()
    elif user_int == 2:
        programme_2()
    else:
        programme_3()


#===============================
# EXECUTION
#===============================

# Execute main code
main()



#===============================
#===============================
# EXTENSION
# TODO Go back to each program you chose and structure them with functions. 
# TODO Then recopy them over as multiple functions (rather than one)
# NOTE The main() function in your programs can be renamed as run_program_name() so it doesn't clash with this program's main()