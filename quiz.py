# Variables & Constants
score = 0
ART_CORRECT = "(●'◡'●)"
ART_INCORRECT = "( ˘︹˘ )"
answer_1 = "yes"
answer_2 = "no"
answer_3 = "no"
answer_4 = "yes"
answer_5 = "b"

# Introduction
name = input("What's your name?")
print("Hi", name + "!")
print("You're going to play a quiz. There are 5 random trivia questions to answer, and they get progressively harder. Your score will be shown at the end. You can only answer with yes or no. Goodluck", name)

# Question 1 : Pacific Ocean 
print("Question 1:")
response= input("Is the pacific ocean the largest ocean in the world?").lower().strip()
if answer_1 in response:
    print("Correct! The Pacific ocean is approximately 63-64 million square miles.")
    print(f"{ART_CORRECT}")
    score+=1
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



