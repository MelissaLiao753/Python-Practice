

#----------------------------------------------------------------------#

def main():
    # CONSTANTS
    ART_CORRECT = "( '◡' )"
    ART_INCORRECT = "( ˘︹˘ )"

    # VARIABLES
    answers = ["b","c","d","a","b"] # correct answers to check for each question
    score = 0 
    play = True

    # QUIZ INTRODUCTION 

    def intro():
        name = input("What's your name?")
        print(f"Hi {name}!")
        print(f"You're going to play a quiz. There are 5 random trivia questions to answer, and they get progressively harder. Your score will be shown at the end. You can only answer with a, b, c, or d. Goodluck {name}")

    # INVALID INPUT (Assigning a value  to use if their answer is valid (FALSE) or invalid (TRUE).)

    def invalid_input(response):
        if response not in ["a", "b", "c", "d"]: 
            return True
        else:
            return False
        
    # SCORE OUTCOME (Outputting a message based on their how many questions they got correct out of 5.)

    def total_score(score):
            if score == 5:
                print("Wow! You got them all correct! Goodjob.")
                print("(o゜▽゜)o☆")

            elif score == 4:
                print("You did pretty good!")
                print("ƪ(˘⌣˘)ʃ")

            elif score == 3:
                print("You did average. Try again?")
                print("(￣_￣|||)")

            elif score == 2 or score == 1:
                print("You did pretty bad. You should try again.")
                print("╮（╯＿╰）╭")

            elif score == 0:
                print("General trivia isn't your thing.")
                print("（；´д｀）ゞ")


                
    # COLLECTION (Listing all of the quiz questions and their answers to list by index later)
    
    questions = [ 
        
        ["What is the largest ocean in the world?", "a) Indian Ocean, b) Pacific Ocean, c) Atlantic Ocean, d) Antarctic Ocean"] , 

        ["What is the fastest animal?", "a) Golden Eagle, b) Cheetah, c) Peregrine Falcon, d) Black Marlin"],

        ["When was the first iphone created?", "a) 2009, b) 2005, c) 2012, d) 2007"],

        ["What is the rarest and most expensive spice in the world by weight?", "a) Saffron, b) Oregano, c) Paprika, d) Cinnamon"],

        ["Which Egyptian goddess has the head of a hippopotamus?", "a) Renenutet b) Taurt c) Hatmehit d) None"]
    ]

    intro()

    # ACTUAL QUIZ (Listing questions by index and checking if it's correct, incorrect, or an invalid input. If it's invalid the question repeats.)
    while play == True:

        # QUESTION 1 : WHAT'S THE LARGEST OCEAN?
        while True:
            print(questions[0][0])
            response = input(questions[0][1]).strip().lower()

            if response == answers[0]:
                print("Correct! The Pacific ocean is approximately 63-64 million square miles.")
                print(f"{ART_CORRECT}")
                score = max(0, score + 1)
                break

            elif invalid_input(response):
                print("That's an invalid input. Type in one of the valid options, a, b, c, or d.")
                    

            else:
                print("No, that's not quite right. The Pacific ocean is the largest ocean in the world.")
                print(ART_INCORRECT)
                break
                
        # QUESTION 2 : WHAT'S THE FASTEST ANIMAL?
        while True:
            print(questions[1][0])
            response = input(questions[1][1]).strip().lower()

            if response == answers[1]:
                print("Correct! The Peregrine falcon is the fastest bird and can fly up to speeds up to 389km/h")
                print(ART_CORRECT)
                score = max(0, score + 1)
                break
            elif invalid_input(response):
                print("That's an invalid input. Type in one of the valid options, a, b, c, or d.")

            else:
                print("Incorrect. The Peregrine falcon is the fastest bird on earth.")
                print(f"{ART_INCORRECT}")
                break
        
        #QUESTION 3 : WHEN WAS THE FIRST IPHONE MADE?
        while True:
            print(questions[2][0])
            response = input(questions[2][1]).strip().lower()

            if response == answers[2]:
                print("Yes that's correct! The first iphone was actually created in 2007.")
                score = max(0, score + 1)
                print(f"{ART_CORRECT}")
                break
            elif invalid_input(response):
                print("That's an invalid input. Type in one of the valid options, a, b, c, or d.")

            else:
                print("Incorrect. The first iphone was created in 2007.")
                print(f"{ART_INCORRECT}")
                break

        # QUESTION 4 : WHAT'S THE MOST EXPENSIVE SPICE?
        while True:
            print(questions[3][0])
            response = input(questions[3][1]).strip().lower()

            if response == answers[3]:
                print("Yes that's correct! Saffron costs anywhere between $5,000 to over $10,000 USD per kilogram due to required intense labor to extract the spice.")
                score = max(0, score + 1)
                print(f"{ART_CORRECT}")
                break

            elif invalid_input(response):
                print("That's an invalid input. Type in one of the valid options, a, b, c, or d.")

            else:
                print("Incorrect. Saffron is the most expensive spice. Costing around $5,000 to over $10,000 USD per kilogram.")
                print(f"{ART_INCORRECT}")
                break

        # QUESTION 5 : WHAT GODDESS HAS THE HEAD OF A HIPPO?
        while True:

            print(questions[4][0])
            response = input(questions[4][1]).strip().lower()

            if response == answers[4]:
                print("Yes that's correct! Taurt is known for protecting against evil spirits and being a gentle guardian looking after children and pregnant women. Renenutet was a cobra goddess known for harvest and fertility and Hatmehit was a fish goddess.")
                score = max(0, score + 1)
                print(f"{ART_CORRECT}")
                break

            elif invalid_input(response):
                print("That's an invalid input. Type in one of the valid options, a, b, c, or d.")

            else:
                print("Incorrect. Taurt is the goddess with a hippopotamus head.")
                print(f"{ART_INCORRECT}")
                break

        # DISPLAY SCORE (Telling the user how many questions they answered correctly)

        print("You got", score, "out of 5 correct!")
        total_score(score) 

        # PLAY AGAIN? (Asking the user if they want to play again. If it's an invalid input, they're forced to answer again.)

        user_choice = input("Would you like to play again? yes/no").strip().lower()
        if user_choice in "yes":
            continue

        elif user_choice in "no":
            break
        
        else:
            while user_choice not in ["yes", "no"]:
                print("Invalid input. Please type yes/no.")
                user_choice = input("Would you like to play again? yes/no").strip().lower()
            
main()


