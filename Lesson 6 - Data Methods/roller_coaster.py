# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Get input
height = int(input("How tall are you?".strip()))
age = int(input("How old are you?".strip()))
heart = input("Do you have a heart condition? (Yes or no)".strip().lower())
vip = input("Do you have a vip pass? (Yes or no)".strip().lower())




# Check conditions and output verdicte
if height > 150 and age > 10 and heart == "no" and vip == "yes":
    print("You are allowed entry. Welcome to vip!")

elif height > 150 and age > 10 and heart == "no":
    print("You are allowed entry.")

else: 
    print("Sorry, you can't go on this ride.")
    



# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient