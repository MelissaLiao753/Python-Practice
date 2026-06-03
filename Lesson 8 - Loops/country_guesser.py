# =====================================================================
# Task: Country Guessing Game
# =====================================================================

# VALUES
# TODO: Create a variable to store the correct country (e.g., "Italy").
country_correct= "italy"
# TODO: Create a variable to keep track of the user's current guess. 
attempts = 0
#       (Hint: Start it as an empty string "" so the loop runs at least once!)


# LOOP
# TODO: Start a 'while' loop. 
guess= input("What country am I thinking of?").lower().strip()
while guess != country_correct:
    print("Wrong. But you can do it!")
    guess=input("Try again.").lower().strip()
    attempts +=1

    
   
print("Correct! I was thinking of", country_correct)
print("You did it! Hurray, it only took you", attempts, "attempts. Congrats")
#       The loop should keep running AS LONG AS the user's guess 
#       is NOT EQUAL to the correct country.
    
    # TODO: Ask the user for their guess and save it to your guess variable.
    #       (Remember: This changes the loop condition so it doesn't run forever!)
    
    # TODO: (Optional) Add an 'if' statement inside the loop.
    #       If they guessed wrong, print an encouraging message or an extra hint.
    #       If they guessed right, the loop will automatically exit on the next check!


# GAME OVER / WINNING MESSAGE
# TODO: Print a congratulatory message celebrating their win!

# ================================================================
# EXTENSION
# TODO: Add an introduction
# TODO: Add a scoring system (starts at 20, lose 1 point for each wrong guess)
# TODO: Add a lose condition (if score reaches 0)

#==================================================================
# EXPERT
# TODO: Make the game unique (use a list of countries and randomly select one)
# TODO: Add a play again option