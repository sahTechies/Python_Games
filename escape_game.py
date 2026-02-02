import random

# Global variables
player_health = 100
enemy_health = 100

def enemy_attack(is_hard=False):
    """Enemy attacks player"""
    global player_health
    if is_hard:
        damage = random.randint(8, 25)
    else:
        damage = random.randint(5, 20)
    
    print(f"👹 Enemy attacks for {damage} damage!")
    player_health -= damage
    print(f"Your health: {player_health}/100\n")

def conservative_attack():
    """Safe attack"""
    global enemy_health
    damage = random.randint(10, 25)
    print(f"⚔️  Conservative attack deals {damage} damage!")
    enemy_health -= damage
    print(f"Enemy health: {enemy_health}/100\n")

def hard_attack():
    """Risky attack"""
    global enemy_health
    damage = random.randint(15, 35)
    print(f"💥 Hard attack deals {damage} damage!")
    enemy_health -= damage
    print(f"Enemy health: {enemy_health}/100\n")

def check_health():
    """Check game over conditions"""
    global player_health, enemy_health
    if player_health <= 0:
        print("💀 You have been defeated! Game Over.")
        exit()
    if enemy_health <= 0:
        print("🎉 Victory! You escaped!")
        exit()

# === GAME START ===
print("🕯️  You wake up in a dark room.")
print("Which door will you choose?\n")

# Scenario 1: Door Selection (FIXED)
while True:
    print("1. Left door")
    print("2. Right door") 
    print("3. Wait here")
    choice = input("Choose (1-3): ").strip()
    
    if choice == "1":
        print("✅ Good choice! But danger awaits...\n")
        break
    elif choice == "2":
        enemy_health += 20  # FIXED: No global here (already global scope)
        print("⚠️  Harder path chosen!")
        print(f"Enemy is stronger! ({enemy_health}/100 HP)\n")
        break
    elif choice == "3":
        player_health -= 10
        print("⏳ Time wasted! Lose 10 health.")
        print(f"Your health: {player_health}/100\n")
        check_health()
    else:
        print("❌ Invalid choice. Try 1, 2, or 3.\n")

# Scenario 2: Combat
print("👹 Monster approaches! Fight!\n")

while enemy_health > 0 and player_health > 0:
    print("Choose attack:")
    print("1. Conservative (Safe)")
    print("2. Hard (Risky/Powerful)")
    choice = input("Choose (1-2): ").strip()
    
    if choice == "1":
        conservative_attack()
        check_health()
        enemy_attack()
        check_health()
    elif choice == "2":
        hard_attack()
        check_health()
        enemy_attack(is_hard=True)
        check_health()
    else:
        print("❌ Invalid! Monster attacks!\n")
        enemy_attack()
        check_health()

print("Game Over!")
