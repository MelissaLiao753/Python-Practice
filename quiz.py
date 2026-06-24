
""" 
#ORIGINAL
def main():
    # Variables & Constants
    score = 0

    ART_CORRECT = "( '◡' )"
    ART_INCORRECT = "( ˘︹˘ )"

    answer_1 = "yes"
    answer_2 = "no"
    answer_3 = "no"
    answer_4 = "yes"
    answer_5 = "yes"
    play = True
        # Introduction

    while play == True:
        name = input("What's your name?")
        print(f"Hi {name}!")
        print("You're going to play a quiz. There are 5 random trivia questions to answer, and they get progressively harder. Your score will be shown at the end. You can only answer with yes or no. Goodluck", name)

        # Question 1 : Pacific Ocean 
        print("Question 1:")
        response= input("Is the pacific ocean the largest ocean in the world?").lower().strip()
        if answer_1 in response:
            print("Correct! The Pacific ocean is approximately 63-64 million square miles.")
            print(f"{ART_CORRECT}")
            score+=1

        elif response != "yes" or "no":
            print("Your input is not valid. Please try again.")
            response= input("Is the pacific ocean the largest ocean in the world?").lower().strip()

        else:
            print("No, that's not quite right. The Pacific ocean is the largest ocean in the world.")
            score-=1
            print(f"{ART_INCORRECT}")

        # Question 2 : Fastest Animal 
        print("Question 2:")
        response= input("Is the fastest animal is the golden eagle?").lower().strip()
        if answer_2 in response:
            print("Correct! The Peregrine falcon is the fastest bird and can fly up to speeds up to 389km/h")
            score+=1
            print(f"{ART_CORRECT}")

        elif response != "yes" or "no":
            print("Your input is not valid. Please try again.")
            response= input("Is the fastest animal is the golden eagle?").lower().strip()

        else:
            print("Incorrect. The Peregrine falcon is the fastest bird on earth.")
            score-=1
            print(f"{ART_INCORRECT}")

        #Question 3 : First Iphone
        print("Question 3:")
        response= input("Was the first iphone created in 2009?").lower().strip()
        if answer_3 in response:
            print("Yes that's correct! The first iphone was actually created in 2007.")
            score+=1
            print(f"{ART_CORRECT}")

        elif response != "yes" or "no":
            print("Your input is not valid. Please try again.")
            response= input("Was the first iphone created in 2009?").lower().strip()

        else:
            print("Incorrect. The first iphone was created in 2007.")
            score-=1
            print(f"{ART_INCORRECT}")

        #Question 4 : Rarest Spice
        print("Question 4:")
        response= input("Is saffron the most rarest and most expensive spice in the world by weight?").lower().strip()
        if answer_4 in response:
            print("Yes that's correct! Saffron costs anywhere between $5,000 to over $10,000 USD per kilogram due to required intense labor to extract the spice.")
            score+=1
            print(f"{ART_CORRECT}")

        elif response != "yes" or "no":
            print("Your input is not valid. Please try again.")
            response= input("Is saffron the most rarest and most expensive spice in the world by weight?").lower().strip()

        else:
            print("Incorrect. Saffron is the most expensive spice. Costing around $5,000 to over $10,000 USD per kilogram.")
            score-=1
            print(f"{ART_INCORRECT}")

        #Question 5 : Egyptian Goddess
        print("Question 5:")
        response= input("Which Egyptian goddess has the head of a hippopotamus? A) Renenutet B) Taurt C) Hatmehit (Enter the corresponding letter)").lower().strip()
        if answer_5  in response:
            print("Yes that's correct! Taurt is known for protecting against evil spirits and being a gentle guardian looking after children and pregnant women. Renenutet was a cobra goddess known for harvest and fertility and Hatmehit was a fish goddess.")
            score+=1
            print(f"{ART_CORRECT}")

        elif response != "yes" or "no":
            print("Your input is not valid. Please try again.")
            response= input("Which Egyptian goddess has the head of a hippopotamus? A) Renenutet B) Taurt C) Hatmehit (Enter the corresponding letter)").lower().strip()

        else:
            print("Taurt is known for protecting against evil spirits and being a gentle guardian looking after children and pregnant women. Renenutet was a cobra goddess known for harvest and fertility and Hatmehit was a fish goddess.")
            score-=1
            print(f"{ART_INCORRECT}")


        # Conclusion
        print("You finished the quiz!. You scored", score, "points.")

        #Responses in terminal based on score
        if score == 5:
            print("Wow! You got them all correct! Goodjob.")
            print("(o゜▽゜)o☆")

        elif score > 0 and score < 2:
            print("You did average. Try again?")
            print("(￣_￣|||)")

        elif score > 1 and score < 5:
            print("You did pretty good!")
            print("ƪ(˘⌣˘)ʃ")

        elif score > -4 and score < 0:
            print("You did pretty bad. You should try again.")
            print("╮（╯＿╰）╭")

        elif score < -3:
            print("General trivia isn't your thing.")
            print("（；´д｀）ゞ")

main()
"""
#----------------------------------------------------------------------#

ART_CORRECT = "( '◡' )"
ART_INCORRECT = "( ˘︹˘ )"
answers = ["b","c","d","a","b"]
score = 0

play = True
def intro():
    name = input("What's your name?")
    print(f"Hi {name}!")
    print(f"You're going to play a quiz. There are 5 random trivia questions to answer, and they get progressively harder. Your score will be shown at the end. You can only answer with a, b, c, or d. Goodluck {name}")

def invalid_input(response):
    if response not in ["a", "b", "c", "d"]:
        return True
    else:
        return False
    
    
def total_score(actual_score):
        if score == 5:
            print("Wow! You got them all correct! Goodjob.")
            print("(o゜▽゜)o☆")

        elif score == 3:
            print("You did average. Try again?")
            print("(￣_￣|||)")

        elif score == 4:
            print("You did pretty good!")
            print("ƪ(˘⌣˘)ʃ")

        elif score == 2 or score == 1:
            print("You did pretty bad. You should try again.")
            print("╮（╯＿╰）╭")

        elif score == 0:
            print("General trivia isn't your thing.")
            print("（；´д｀）ゞ")


questions = [ 
    
    ["What is the largest ocean in the world?", "a) Indian Ocean, b) Pacific Ocean, c) Atlantic Ocean, d) Antarctic Ocean"] , 

    ["What is the fastest animal?", "a) Golden Eagle, b) Cheetah, c) Peregrine Falcon, d) Black Marlin"],

    ["When was the first iphone created?", "a) 2009, b) 2005, c) 2012, d) 2007"],

    ["What is the rarest and most expensive spice in the world by weight?", "a) Saffron, b) Oregano, c) Paprika, d) Cinnamon"],

    ["Which Egyptian goddess has the head of a hippopotamus? a) Renenutet b) Taurt c) Hatmehit d) None"]
]
response = "none"
intro()

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
            score = max(0, score - 1)
            break
        
    
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
            score = max(0, score - 1)
            print(f"{ART_INCORRECT}")
            break

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
            score = max(0, score - 1)
            print(f"{ART_INCORRECT}")
            break

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
            score = max(0, score - 1)
            print(f"{ART_INCORRECT}")
            break

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
            score = max(0, score - 1)
            print(f"{ART_INCORRECT}")
            break

total_score()

