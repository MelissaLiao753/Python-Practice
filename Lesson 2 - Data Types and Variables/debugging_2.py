# 3 Question Quiz - Debug all the errors, including any semantic errors.
multiply_1 = input("Pick a random number")
multiply_2= 6
INSTRUCTIONS = "This is a quick 3 part quiz. A question will be asked, and then you answer it"
name=input("What's your name?")


print("Hello", name,"!")

print(INSTRUCTIONS)
print("First question:")
aswr_1=input("How many millimetres in a centimetre?")
print("The answer is 10!")

print("Next Question:")
answr2=input("What is the capital of New Zealand?")
print("The answer is Wellington. That was easy, wasn't it?")

print("Final Question!")
answr_3=input(f"What is {multiply_1} x {multiply_2}?")
print("The answer is", int(multiply_1) * multiply_2)