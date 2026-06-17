# PROJECT: Pokemon

import random

# Wild Pokemon
# Multidimensional list that holds 4 pokemon names and their max health
wild_pokemon = [
    ["turtwig", 55],
    ["chimchar", 44],
    ["piplup", 53],
    ["pikachu", 35]
    ]
# User Pokemon
# Multidimensional list that holds 4 pokemon attacks and their different damage
pokemon_attacks = [
    ["scratch", 15],
    ["tackle", 25],
    ["pound", 30],
    ["quick attack", 35]
    ]
# RANDOM WILD POKEMON PICK
random_wild_pokemon = random.choice(wild_pokemon)
# MAX HEALTH OF RANDOM POKEMON
current_health = random_wild_pokemon[1]
print(f"Hi! Your battle will be against: {random_wild_pokemon[0]}, It's health is: {current_health}")
# WHILE CURRENT HEALTH OF WILD POKEMON IS ABOVE 0 HP OR EQUAL TO 0 HP
while 0 < current_health:
    user_attack_choice = input("Which attack would you like to use? Type in the number corresponding to the attack. The available attacks are: 1) scratch 2) tackle 3) pound 4) quick attack.")
    try:
        #ATTACK INDEX IS EQUAL TO THE INTEGER VERSION OF USER ATTACK
        attack_index = int(user_attack_choice) - 1
        #IF ATTACK INDEX IS ABOVE OR EQUAL TO 0 AND THE LENGTH OF THE POKEMON-
        if 0<= attack_index < len(pokemon_attacks):
            chosen_attack = pokemon_attacks[attack_index]
            damage = chosen_attack[1]
            print("Attack commensing..")
            current_health = current_health - damage
    except ValueError:
        print("Please enter a valid number corresponding to the attack.")
        continue
   
    # TODO Ask the user which attack they'd like to use (list all 4 options, numbered); save input
    # TODO Use try except to ensure the user has input a number; if they didn't tell them so and then use 'continue' to restart the loop
    # TODO Using the number, get the attack damage value and minus it from current health
print("The pokemon's health is at:", current_health)
# TODO Tell the user they defeated the pokemon

# ====================================================
# EXTENSION
# NOTE: Only do the extension once you have completed the project update (with dictionaries)

# TODO: Give your wild pokemon each an attack value as well, then allow it to attack the user back each turn (You'' need a player health)
# TODO: Change your 'user pokemon' to a list of different pokemon they can choose from. Each pokemon will have their own list of attacks.
# TODO: Give all pokemon a type. Create a new dictionary of types that each has a dictionary of strengths and weaknesses. Use this to change the damage.