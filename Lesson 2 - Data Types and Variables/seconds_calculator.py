# Create a calculator that asks the user for a number (of days)
# and outputs how many seconds in that number of days

# Values - start by writing constants to hold:
# The number of seconds in a minute
SECS_IN_MINUTE= 60
# The number of minutes in an hour
MINS_IN_HOUR= 60
# The number of hours in a day
HOURS_IN_DAY= 24

# Get input from the user and save it in a variable
days_input = input("How many days until the weekend?")

# Change the value into an integer and resave in the variable
days = int(days_input)

# Calculate the number of seconds using * with the input and your constants.
total_seconds = days * HOURS_IN_DAY * MINS_IN_HOUR * SECS_IN_MINUTE
# Save it in a new variable.
secs= int(total_seconds)
# Output the answer
print("So, there are", secs,  "seconds away from the weekend.")
# ---------------------------------

# EXTENSION
# Also output how many total hours and how many total minutes in the days
total_hours = days * HOURS_IN_DAY
hours = int(total_hours)

total_mins = days* HOURS_IN_DAY * MINS_IN_HOUR
mins = int(total_mins)

print("Which means that there are", mins, "minutes away from the weekend, and", hours, "hours away. That's a long time, goodluck!")
# Create another calculator that does the opposite (input is seconds, output is days)

# ---------------------------------

# EXPERT (for those who already know some Python)
# Create the calculator above, but...
#   allow your user to choose the input and output type (seconds, minutes, hours, days)
#   Loop the calculator so they can do it again with having to reopen the program.