#Introduction
print("Hi! This programme is meant to help you pack the most suitable items for your travel to ensure you have an amazing and comfortable time. Let's get started!")


# Q1 : Temperature
temperature = input("What's the temperature in the place you're traveling to?")
temp = int(temperature)
if temp < 15:
    print("Chilly. Make sure to pack a jacket or some warm clothes so you don't get catch a cold.")

if temp > 15:
    print("It could get quite hot. Make sure to pack some sunscreen so you can enjoy the weather.")


# Q2 : Destination
destination = input("Where are you going to? The beach or the mountains?").lower()

if destination == "beach":
    print("You should pack a towel if you're planning to swim or sunbathe on the beach.")

if destination == "mountains":
    print("You should bring some hiking boots so you have proper gear and less trouble with climbing.")


# Q2 : Flying?

flight = input("Are you flying to your destination? (yes/no)").lower()

if flight == "yes":
    flight_hours = input("How long is your flight in hours?")
    flight_int = int(flight_hours)
    if flight_int >= 4:
        print("You should consider bringing a neck pillow for comfort during the flight.")
    if flight_int < 4:
        print("Have you considered bringing a few games or things to entertain you during the flight? Shorter flights typically don't have entertainment provided.")

if flight == "no":
    print("Alright. Sounds very closeby. Have fun!")


# EXPERT (for those who already know Python)

# Create a packing checklist (start with something similar to the main program) then 
# display all items to pack with a X or O for packed or not. 
# Allow the user to select an item to change its status.