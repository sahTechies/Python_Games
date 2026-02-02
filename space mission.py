import time
import random

current_planet = "earth"
inventory = []
oxygen = 100

solar_system = {
    "earth": {
        "desc": "Earth launchpad. Spaceship ready. Mars or Moon available.",
        "exits": {"mars": "mars", "moon": "moon"},
        "items": ["laser"],
        "puzzle": None
    },
    "moon": {
        "desc": "Lunar base. Rocky surface, find fuel tank.",
        "exits": {"back": "earth"},
        "items": ["fuel"],
        "puzzle": "Moon gravity: what's half of 9.8? (4.9)"
    },
    "mars": {
        "desc": "Mars rover site. Alien artifact needs laser.",
        "exits": {"back": "earth", "asteroids": "asteroids"},
        "items": [] if "laser" not in inventory else ["artifact"],
        "puzzle": None
    },
    "asteroids": {
        "desc": "Asteroid field. Dodge or solve path: prime numbers sum to 17? (2+3+5+7)",
        "exits": {"safe": "home"},
        "items": [],
        "puzzle": "2357"
    },
    "home": {
        "desc": "Mission control! You returned with artifact. Victory!",
        "exits": {},
        "items": [],
        "puzzle": None
    }
}

def show_status():
    global oxygen
    room = solar_system[current_planet]
    print(f"\n--- Oxygen: {oxygen}% ---")
    print(room["desc"])
    if room["items"]:
        print("Found:", ", ".join(room["items"]))
    print("Warp to:", ", ".join(room["exits"]))

    # Pickup
    if room["items"] and input("Grab item? (y/n): ").lower() == 'y':
        item = input("Which? ").strip()
        if item in room["items"]:
            inventory.append(item)
            room["items"].remove(item)
            print(f"Acquired {item}!")

def solve_puzzle():
    room = solar_system[current_planet]
    if room["puzzle"]:
        ans = input(f"Captain's log: {room['puzzle']} ").strip().lower()
        if "4.9" in ans or "4.9" in ans.replace('.', ''):
            print("Correct! Fuel unlocked.")
            room["items"].append("fuel")
            return True
        elif "2357" in ans:
            print("Primes aligned! Safe path open.")
            return True
        else:
            print("Failed. Oxygen leak!")
            return False
    return True

print("Space Mission: Collect artifact, return home!")
while oxygen > 0:
    show_status()
    
    if current_planet == "home":
        print("MISSION SUCCESS! 🪐")
        print("Inventory:", inventory)
        break
    
    action = input("\n> ").lower()
    
    if action == "quit":
        print("Mission aborted...")
        break
    elif action in solar_system[current_planet]["exits"]:
        current_planet = solar_system[current_planet]["exits"][action]
        oxygen -= random.randint(5, 15)
    elif "scan" in action:
        solve_puzzle()
    else:
        print("Invalid command. Try planet name.")
        oxygen -= 2
    
    time.sleep(1)

if oxygen <= 0:
    print("Oxygen depleted. Game over.")