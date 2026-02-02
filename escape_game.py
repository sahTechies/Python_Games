import random

#Global Health
player = 100
enemy = 100

#Combat Functions
def enemyAttack():
    global player
    damage = random.randint(5, 20)
    print("Enemy attacks!")
    print("Attack =", damage, "HP")
    player = player - damage


def conservAttack():
    "Remove health from enemy"
    global enemy
    damage = random.randint(10, 25)
    print("You attack!")
    print("Attack =", damage, "HP")
    enemy = enemy - damage
    print("Enemy Health =", enemy, "HP")


def hardAttack():
    "Remove health from enemy"
    global enemy
    damage = random.randint(10, 25)
    print("You attack!")
    print("Attack =", damage, "HP")
    enemy = enemy - damage
    print("Enemy Health =", enemy, "HP")


#Health Check/Game Over Function
def healthCheck():
    "Checks the player's health to see if the game is over"
    if player <= 0:
        print("You have been defeated! Game Over.")
        exit()  

#Scenario 1
print("You wake up in a dark room ")
print("You don't know where you are or how you got there.")

#Scenario 1 loop
while True:
    print("do you want to go through one of the doors?")
    print("1. Left door")
    print("2. right door")
    print("3. just sit here a minute")
    answer = input()
    if answer == "1":
        print("good choice,but be prepared for a fight!")
        break
    elif answer == "2":
        print("You like taking the hard way, don't you?")
        ememy = enemy + 20
        break
    elif answer == "3":
        print("You are wasting time! You're losing health!")
        player -= 10
        healthCheck()
    else:
        print("That's not an option, try something else.")

#Scenario 2 - Combat
print("You can hear the sound of a monster approaching in the darkness.") 
Print("Prepare to fight!")  

#scenario 2 loop
while enemy > 0:
    print("Do you want to:")
    print("1. Attack Conservatively")
    print("2. Attack Hard")
    choice = input()
    if choice == "1":
        conservAttack()
        if enemy <= 0:
            print("You have defeated the enemy!")
            break
        enemyAttack()
        healthCheck()
    elif choice == "2":
        hardAttack()
        if enemy <= 0:
            print("You have defeated the enemy!")
            break
        enemyAttack()
        healthCheck()
    else:
        print("Invalid choice, try again.")


