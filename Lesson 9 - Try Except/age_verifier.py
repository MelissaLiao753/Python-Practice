# =====================================================================
# PROGRAM: Age verification
#           Verify the user's age is over 18 to give access (or deny access)
#           Keep asking for input until they've given a valid age
# =====================================================================

# VARIABLES
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
    #TRY
    # TODO Create a try statement
        # TODO Change the input into an integer and resave it
        # TODO Set the valid input variable to true

    # FAIL TO CONVERT TO INTEGER
    # TODO Add an except statement
    # TODO Tell the user their input was invalid

# Unindented = Loop has finished so the input must be valid now

# CHECK AGE
# TODO Check if they are older than 18 and tell them they have access if they are
# TODO Check if they are older than 13 and tell them they have partial access if they are.
# TODO Otherwise tell them access has been denied


# ===================================================================
# EXTENSION
# Create a avatar creator for them to use if they get access. There should be 2 versions (full and partial)
# Eg. Full can choose: character class (warrior, rogue), hair colour, eye colour; partial just character class (with animal classes?)