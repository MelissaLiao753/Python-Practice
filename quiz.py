score = 0


# Introduction
name = input("What's your name?")
print("Hi", name +"!")
print("You're going to play a quiz. There are 5 random trivia questions to answer, and they get progressively harder. Your score will be shown at the end. Goodluck", name)

# Question 1
print("Question 1:")
answer_1= input("What is the largest ocean on Earth?").lower()
if answer_1 == "pacific" in answer_1:
    print("Correct! The Pacific ocean is approximately 63-64 million square miles.")
    score+=1
else:
    print("No, that's not quite right.")
    score-=-1

# Question 2
print("Question 2:")
answer_2= input("What's the fastest bird?").lower()
if answer_2 == "falcon" in answer_2:
    print("Yes! The Peregrine falcon can fly up to speeds up to 389km/h")
    score+=1
else:
    print("Incorrect.")
    score-=1

#Question 3
print("Question 3:")
answer_3= input("What is the meaning of verisimilitude?")


