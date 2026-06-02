#Create a program to battle a boss.
#The battle should take place over 2+ rounds.
#The user should be able to make a decision. Eg:
#Attack with sword
#Attack with bow
#Heal
#Etc.
#Let the user know the result of each round.
#If you already know how to use loops, use them to make this much better!
import random
attack= 10
specialtymove= 0
specialtydamage= -25
boss_health= 100
your_health=75
dragon="""   
             /|                                                              
        //^^^  ~~~~^^^^---___                   ^\            /|         
     /c~~`'     ____          ^^^^             /| \\        /_ _\     
     ~^^--; _\\\    ~~~---___     ~~~~        / '|  \\       | |           
       /_/                 --        ~~~__/ ,  |   \\       \ \        
      " ~                      -        |\--;' |  |    ;;      | |           
                               |          \   |    |    /     /  / 
                              |__ \  \     ~--|/~~\/~~|/     /  /       
                         /---_.     \  \         |    /      |  |            
                        ;-/   ~\-----   ;         |           |  |           
                         '--\_,--------'           |          |   |        
                           / ____    _^^^_..        |        -    |           
                          |       /^       ..       |       _    |           
               /           | ---- |      .           |      _    |            
          6  /__           `     `.      |           |    -    -              
         0+}/ ;~            ` .--  `      |           -__-    -     q\       
        =( __ /               / ` -_.     /                   -     /`'>      
        /|  |>          _-__ ---^^     /          _---_____--      /^^\     
      -------          ///  ///__ -__  / -____--~                 / || \ """
user_name = input("What is your username?")
print("BOSS BATTLE COMMENSING....")
print(dragon)

#ACTION 1
print("ROUND 1:", user_name, "VS THE DRAGON")
action = input("What will you choose to do? a) Attack b) Dodge c) Heal d) Specialty Move" ).lower().strip()
if action == "d" and specialtymove < 3:
    specialtymove +=1
    print("You can't use your specialty move now. You've lost your time to strike first. Please wait until after the 3rd turn.")
elif action == "a":
    print("ATTACKING...")
    print("BOSS HEALTH:", boss_health - attack)
    print("YOUR HEALTH:", your_health)
elif action == "b":
    print("DODGING...")
    print("You successfully avoided the attack")
    print("YOUR HEALTH:", your_health)
elif action == "c":
    print("HEALING...")
    print("You are already fully healed. You just wasted some of your bandages.")
    print("YOUR HEALTH:", your_health)
else:
    print("You indecision has lost you the time to make a move.")

if action != "b":
    print("The dragon swipes at you with it's massive claws, and it's talons scrape against your side. You don't manage to dodge in time.")
    print("YOUR HEALTH:", your_health - 10)


#ACTION 2

action_2 = input("What will you choose to do? a) Attack b) Dodge c) Heal d) Specialty Move" ).lower().strip()
if action == "d" and specialtymove < 3:
    specialtymove +=1
    print("You can't use your specialty move now. You've lost your time to strike first. Please wait until after the 3rd turn.")

elif action_2 == "a":
    print("ATTACKING...")
    print("BOSS HEALTH:", boss_health - attack)
    print("YOUR HEALTH:", your_health)

elif action_2 == "b":
    print("DODGING...")
    print("You successfully avoided the attack")
    print("YOUR HEALTH:", your_health)
elif action_2 == "c":
    print("HEALING...")
    print("You heal yourself.")
    print("YOUR HEALTH:", your_health + 5)
else:
    print("You indecision has lost you the time to make a move.")

if action_2 != "b":
    print("The dragon unleashes a breath of fire, singing the skin on your arms.")
    print("YOUR HEALTH:", your_health - 15)

print("RANDOM: You see that there's some treasure in the dragons nest. The dragon is fiercely protecting it, and if you get close, it's very easy for it to attack you in a vulnerable position.")
answer=input("But inside the nest might be a useful item to fight the dragon. Do you risk getting closer? Yes/No").strip().lower()
if answer =="yes":
    result=random.choice(["succeeded","failed"])
    print("You", result)
    if result == "succeeded":
        print("You successfuly grabbed a rusty looking sword from the nest that was poking from the edge while avoiding the dragons vicious attacks.")
        attack=+5
