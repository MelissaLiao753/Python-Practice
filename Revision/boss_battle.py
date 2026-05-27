#Create a program to battle a boss.
#The battle should take place over 2+ rounds.
#The user should be able to make a decision. Eg:
#Attack with sword
#Attack with bow
#Heal
#Etc.
#Let the user know the result of each round.
#If you already know how to use loops, use them to make this much better!
attack= 10
specialtymove= 0
specialtydamage= -25
boss_health= 100
your_health=75
user_name = input("What is your username?")
print("BOSS BATTLE COMMENSING....")
print("             /|                                             "                  
    "   //^^^  ~~~~^^^^---___                   ^\            /|       "      
    "/c~~`'     ____          ^^^^             /| \\        /_ _\  "           
    "~^^--; _\\\    ~~~---___     ~~~~        / '|  \\       | |      "       
    "  /_/                 --        ~~~__/ ,  |   \\       \ \    "        
      " ~                      -        |\--;' |  |    ;;      | | "          
"                              |          \   |    |    /     /  / "
                              |__ \  \     ~--|/~~\/~~|/     /  /             
                         /---_.     \  \         |    /      |  |             
                        ;-/   ~\-----   ;         |           |  |            
                         '--\_,--------'           |          |   |           
                           / ____    _^^^_..        |        -                
                          |       /^       ..       |       _    |            
              /           | ---- |      .           |      _    |             
          6  /__           `     `.      |           |    -    -              
         0+}/ ;~            ` .--  `      |           -__-    -     q\        
       =( __ /               / ` -_.     /                   -     /`'>       
        /|  |>          _-__ ---^^     /          _---_____--      /^^\       
      -------          ///  ///__ -__  / -____--~                 / || \ ")
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
action = input("What will you choose to do? a) Attack b) Dodge c) Heal d) Specialty Move" ).lower().strip()