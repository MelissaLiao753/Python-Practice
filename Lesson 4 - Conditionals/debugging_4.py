
# Variables and constants
steps = input("How many steps did you walk today? ")
steps_int = int(steps)

daily_goal = input("What's your daily goal?")
daily_goal_int = int(daily_goal)


# Step Tracker
print("--- Daily Step Tracker ---")

if steps_int == 0:
    print("Did you forget your phone today? You have 0 steps!")

if 10000 < steps_int :
     print("Amazing! You walked over 10,000 steps! You are a Pro Athlete.")
     
if steps_int < 5000:
    print("Good start, but try to walk a bit more tomorrow!")

if steps_int >= daily_goal_int:
    print("Bullseye! You hit your goal!")

if steps_int == daily_goal_int:
    print("Bullseye! You hit your goal exactly!")



print("Tracker closing...")
