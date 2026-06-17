# =====================================================================
# PROJECT: Wordle
# Create a program where the user must guess the 5 letter word.
# =====================================================================

#IMPORT RANDOM
import random

# VALUES
#LIST OF 5 FIVE-LETTER-WORDS
words = ["horse", "magic", "ocean", "flute", "apple"]

#PLAY
play = True

# INTRODUCTION
print("Hi! Let's play wordle. In order to play, you must type in one of these 5 words. These words are : 1) horse 2) magic 3) ocean 4) flute 5) apple")
# MAIN
#WHILE LOOPS THAT RUNS IF PLAY == TRUE
while play == True:
    #CHOOSING RANDOM SECRET WORD FROM THE LIST
    secret_word = random.choice(words)
    #USER INPUTS FIRST GUESS
    user_input = input("What word do you guess?").lower().strip()

    #WHILE LOOP IF USER INPUT WASN'T A FIVE LETTER WORD
    while 5!= len(user_input) :
        #TELLING USER THEIR GUESS WAS NOT A FIVE LETTER WORD
        print("That's not 5 letters, try again with one of the 5 words I said earlier.")
        #ASKING FOR THE USER'S GUESS FOR THE SECRET WORD AGAIN
        user_input = input("What word do you guess?").lower().strip()
    #IF USER INPUT GUESSED THE CORRECT WORD
    if user_input == secret_word:
        print("You guessed it correctly! It was", secret_word)
        break
        
    else:
        #LOOPS 5 TIMES
        for i in range(5):
            #IF THE LETTER AND POSITION IN THE CORRECT PLACE (INDEX)
            if (user_input[i]) == secret_word[i]:
                print("You got the letter correct! It's the right letter and it's in the right position.")

            #IF THEY GOT THE LETTER CORRECT BUT NOT THE POSITION
            elif (user_input[i]) in secret_word:
                print("You got the correct letter, but it's in the wrong position.")

            #WRONG LETTER AND POSITION
            else:
                print("You got the letter wrong.")

                
    #OPTION TO PLAY AGAIN
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