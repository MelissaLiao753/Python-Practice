# =====================================================================
# PROJECT: Pokemon
# Create a battle program where you battle a random pokemon
# =====================================================================

# TODO Import random module
import random

# Wild Pokemon
# TODO Create a multidimensional list that holds 4 pokemon names and their max health (you choose)
wild_pokemon = [
    ["turtwig", 55],
    ["chimchar", 44],
    ["piplup", 53],
    ["pikachu", 35]
    ]
# User Pokemon
# TODO Create a multidimensional list that holds 4 pokemon attacks and their different damage
pokemon_attacks = [
    ["scratch", 20],
    ["tackle", 30],
    ["pound", 40],
    ["quick attack", 40]
    ]

random_pokemon = random.choice(wild_pokemon)
# TODO Create a variable to hold a randomised wild pokemon
# TODO Create a current_health variable and set it to the max health of the random pokemon
current_health = random_pokemon[1]
# TODO Tell the user what pokemon they're facing
print("Hi! Your battle will be against:",random_pokemon)
# TODO Create a while loop that continues until current health <= 
while current_health > 0:
    user_attack = input("Which attack would you like to use? Type in the number corresponding to the attack. The available attacks are: 1) scratch 2) tackle 3) pound 4) quick attack.")
    attack_int = int(user_attack)
    try:
        if attack_int == int(user_attack):
            print("Attack commensing..")
            break
    except ValueError:
        print("Please enter a valid number corresponding to the attack.")
        continue
   
    # TODO Ask the user which attack they'd like to use (list all 4 options, numbered); save input
    # TODO Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
    # TODO Using the number, get the attack damage value and minus it from current health
print("The pokemon's health is at:", current_health - attack_int)
# TODO Tell the user they defeated the pokemon

# ====================================================
# EXTENSION
# NOTE: Only do the extension once you have completed the project update (with dictionaries)

# TODO: Give your wild pokemon each an attack value as well, then allow it to attack the user back each turn (You'' need a player health)
# TODO: Change your 'user pokemon' to a list of different pokemon they can choose from. Each pokemon will have their own list of attacks.
# TODO: Give all pokemon a type. Create a new dictionary of types that each has a dictionary of strengths and weaknesses. Use this to change the damage.