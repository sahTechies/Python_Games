import random


Your_health = 100
Zombies_count = 7

def zombie_attack():
    """Zombies attack the player"""
    global Your_health
    damage = random.randint(10, 40)
    print(f"🧟‍♂️ Zombies attack for {damage} damage!")
    Your_health -= damage
    print(f"Your health: {Your_health}/10\n")

def attack():
    """Safe attack on zombies"""
    global Zombies_count
    damage = random.randint(1, 3)
    print(f"⚔️   attack kills {damage} zombies!")
    Zombies_count -= damage
    if Zombies_count < 0:
        Zombies_count = 0
    print(f"Zombies remaining: {Zombies_count}\n")



# Check game over conditions
def check_health():
    """Check game over conditions"""
    global Your_health, Zombies_count
    if Your_health <= 0:
        print("💀 You have been overwhelmed by zombies! Game Over.")
        exit()
    if Zombies_count <= 0:
        print("🎉 You have defeated all zombies and survived!")
        exit()    

print("🕯️  You wake up in a post-apocalyptic world overrun by zombies.")
print("You must escape the house in search of safety.\n")
print("Zombies surrounded your house!\n")

# Scenario: Zombie Survival
//check status where you are
while True:
    print("1. Barrucade the doors")
    print("2. Fight the zombies")
    print("3. Hide under bed")
    print("4. Escape through the window")
    choice = input("Choose (1-4): ").strip()

    if choice == "1":
        print("✅ You barricaded the doors, but zombies are still attacking!\n")
        zombie_attack()
        check_health()

    elif choice == "2":
        attack()
        check_health()    
