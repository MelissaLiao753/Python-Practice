### WHAT ANIMAL ARE YOU QUIZ ###

# FIRST, create a basic Flowchart using the FLowchart Shapes to plan the flow of your 'what animal are you' quiz. 
# __________________________

# Write a 'what animal are you' quiz. 
# You can base this on the picture from last lesson, but make it simpler - 
# 3 questions and 4 animals.


# Ask your user a question about themselves, giving them 2 options
Q1 = input("Are you a day or night person?(morning/night)").lower()
# Check if they picked the first option
if Q1 == "morning":
    Q1_part_2 = input("Do you prefer being hot or cold?(hot/cold)").lower()
    if Q1_part_2 == "hot":
        print("You are a Meerkat! Highly sociable and observant.")
    else:
        print("You are a Snowy Owl! Solitary and patient.")
    # Ask the next question

else:
    time_spend = input("Do you prefer being busy or having more free time?(busy/free)").lower()
    if time_spend == "busy":
        print("You are a beaver. Hyper-focused and detail oriented.")
    # Check if they picked the first option
    else:
        print("You are a cat. Independent and self-sufficient.")

        # Tell them they're animal 1

    # Otherwise

        # Tell them they're animal 2

# Otherwise

    # Ask the next question

    # Check if they picked the first option

        # Tell them they're animal 3

    # Otherwise

        # Tell them they're animal 4 

# __________________________

# EXTENSION
# Extend the quiz so there are 8 possible animals
# Create a Flowchart using the FLowchart Shapes to 

# __________________________

# EXTENSION 2
# Create a 'Which ??? are you?' Quiz
# This time allow all questions to have 4 possible answers (a,b,c and d) 
# and tally how many times they choose each
# Determine what they are at the end using the letter with the highest tally.
# Eg. If they picked mostly As, maybe they are Pikachu.