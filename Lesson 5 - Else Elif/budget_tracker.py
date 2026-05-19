### Budget Tracker ###
# Create a budget tracker that gives financial recommendation around an item

#CONSTANTS
BUDGET = 100
SAVINGS_GOAL = 100

#VARIABLES
name = input("What is your name?")
cost = input("What is the cost?")
cost_int = int(cost)
item_type = input("Is it a food item? (yes/no)").lower()
percentage = ((cost_int/BUDGET) * 100)

#INTRO
print(name,"the percentage of money taken away from your budget is", percentage)


#ANSWER TO FOOD QUESTION: NO
if item_type == "no":
    if percentage == 0:
        print("It's free! Go ahead and buy it")
    # Check if percentage is 0 and say it's free if it is
    elif percentage < 10:
        print("It's a small treat so enjoy")
    # Check if the percentage is less then 10 and say it's a small treat so enjoy
    elif percentage < 50:
        print("It's a major spend. You should sleep on it.")
    # Check if it is less than 50 percent and if it is tell them it's a major spend and should sleep on it
    elif percentage > 100:
        print("You can't afford this. You don't have enough money.")
    # Check if it's over 100 and if it is tell them they don't have enough money
    else:
        print("It costs way too much and just isn't worth it.")
# Otherwise, tell them it costs way too much and isn't worth it
#ANSWER TO FOOD QUESTION : YES
if item_type == "yes":
    if percentage == 0:
        print("It's free! Go ahead and buy it")
    
    elif percentage < 10:
        print("It's a small treat so enjoy")
    
    elif percentage < 50:
        print("That's quite expensive for food. You should try find some alternatives.")

    elif percentage > 100:
        print("You can't afford this. You don't have enough money.")

    else:
        print("It costs way too much and just isn't worth it.")



# _______________________

# EXTENSION
# Include an item type question and change answers based on this. 
# Eg. food shouldn't cost as much as a bill so if it's a food, 
# tell them to not buy it at a lower percentage


# _______________________

# EXPERT
# Try to create a budget tracker that saves data in a file 
# so the remaining_budget can be updated every time the program is used
# You will need to create a save.txt file to go with this (keep it in the same folder)
# If you're not sure how to do this check here: https://www.w3schools.com/python/python_file_write.asp 