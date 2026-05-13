### Secret Agent Login
# Create a login process for a secret agent

# Ask for the user's name and save it in a variable
name = input("What's your name?")
# Ask for the password and save it in a variable
password = input("What's the password?")
# Check if the password == 'Falcon'
if password == "Falcon":
    print("Access has been granted. Welcome,", name,".")
    age = input("How old are you?")
    age_int = int(age)
    if age_int <= 13 :
        print("You're a spy in training.")
    
    if 13 < age_int < 18:
        print("You're a junior spy.")
    
    if age_int >= 18 :
        print("You're a field agent.")
    
    print("Goodbye")
else:
    print("Unauthorized access. Try again.")
    # Ouput that access has been granted and welcome user using their name

    # Ask for the user's age and save it in a variable

    # Change the age into an integer

    # If the user's age is under 13, tell them they are a spy in training

    # If their age is under 18, tell them they are a junior spy

    # If their age is 18 or over, tell them they are a Field Agent

# Output a goodbye

# ___________________________

# EXTENSION

# Ask more questions to give your spy more information
# Look up how to use 'and' and 'or' to force more conditions (eg. they must be one of 3 users AND get the password correct)

# ___________________________

# EXPERT (For those who already know python)

# Create a SPY ID GENERATOR
# Your user must login using the correct password to access the generator
# Use a bunch of questions to generate an id. Eg. If their name has 4 or fewer letters, their ID is a random fruit plus other logic...