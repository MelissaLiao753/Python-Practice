# =====================================================================
# PROJECT: Wordle
# Create a program where the user must guess the 5 letter word.
# =====================================================================

# TOOLS
# TODO Import random so you can randomise the word
import random

# VALUES
# TODO Create a list of at least 5 different 5-letter words
words = ["horse", "magic", "ocean", "flute", "apple"]
# TODO Create a variable called play and set it to True
play = True

# INTRODUCTION
# TODO Tell your user how to play wordle (make sure they know they must input 5 letter words)
print("Hi! Let's play wordle. In order to play, you must type in one of these 5 words. These words are : 1) horse 2) magic 3) ocean 4) flute 5) apple")
# MAIN
# TODO Create a while loop that runs if play is true
while play == True:
    # TODO Create word variable and store a random word from your list (using random.choice)
    secret_word = random.choice(words)
    # USER INPUT
    # TODO Get user's first guess and save it into a variable
    user_input = input("What word do you guess?").lower().strip()
    # TODO Create a while loop if the guess is not 5 characters long
    while len(user_input) != 5:
        # TODO Tell them it's not 5 letters and to try again
        print("That's not 5 letters, try again with one of the 6 words I said earlier.")
        user_input = input("What word do you guess?").lower().strip()
    if user_input == secret_word:
        print("You guessed it correctly! It was", secret_word)
        

    # TODO Check if they got it correct and if they did, tell them so and then break the loop
    else:
    # TODO Create a for loop that loops 5 times
        for i in range(5):
            if (user_input[i]) == secret_word[i]:
                print("You got the letter i correct! It's the right letter and it's in the right position.")
            # TODO Check if the current letter of user_input (user_input[i]) is the same as the i letter of the word and if it is tell them they got that letter correct
            elif (user_input[i]) in secret_word:
                print("You got the correct letter, but it's in the wrong position.")
            # TODO Otherwise check if the current letter of user_input is in the word and if it is, tell them that letter is in the wrong position
            else:
                print("You got the letter wrong.")

            # TODO Else tell them that letter is wrong

play_again = input("Do you want to play again? yes/no").strip().lower()
if play_again == "no":
    play = False
# TODO Ask if they want to play again. If they don't, set play to false.


# ==========================================================
# EXTENSION
# Instead of telling the user one by one about their letters, put each correct letter and _ for a wrong letter into a list. 
# Then finally print the list (you can use "".join(list_name) to merge them into a string if you like)

# ==========================================================
# EXPERT
# Following on from the extension, add colour to the letters instead (Don't use _ for incorrect anymore). Green for correct, orange for wrong place, red for incorrect. You'll need to add the colour as you add them to the list

# print("\033[31mThis is Red Text\033[0m")
# print("\033[38;2;255;165;0mThis is Orange Text\033[0m")
# print("\033[32mThis is Green Text\033[0m")

# Further Extension: Structure with user defined functions