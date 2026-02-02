import time
import random

current_location = "beach"
inventory = []
pirate_timer = 8

island = {
    "beach": {
        "desc": "Sandy beach with palm trees. Jungle path north, cave east.",
        "exits": {"north": "jungle", "east": "cave"},
        "items": ["shovel"],
        "puzzle": None
    },
    "jungle": {
        "desc": "Dense jungle. Find first map piece under vines.",
        "exits": {"south": "beach", "west": "waterfall"},
        "items": ["map_piece1"],
        "puzzle": "First mate's birthday? (April 1st)"
    },
    "cave": {
        "desc": "Dark cave with pirate markings. Riddle on wall.",
        "exits": {"west": "beach"},
        "items": [],
        "puzzle": "Blackbeard's ship name (Queen Anne's Revenge)"
    },
    "waterfall": {
        "desc": "Hidden waterfall cave. Treasure map needs 2 pieces + shovel.",
        "exits": {"east": "jungle"},
        "items": [] if len([i for i in inventory if "map_piece" in i]) < 2 or "shovel" not in inventory else ["treasure"],
        "puzzle": None
    }
}

def show_status():
    global pirate_timer
    room = island[current_location]
    print(f"\n--- Pirates arrive in {pirate_timer} turns ---")
    print(room["desc"])
    if room["items"]: print("Found:", ", ".join(room["items"]))
    if room["exits"]: print("Paths:", ", ".join(room["exits"].keys()))

    # Pickup logic
    if room["items"] and input("Grab? (y/n): ").lower() == 'y':
        item = input("Which? ").strip()
        if item in room["items"]:
            inventory.append(item)
            room["items"].remove(item)
            print(f"Got {item}!")

def solve_riddle():
    room = island[current_location]
    if room["puzzle"]:
        ans = input(f"Riddle: {room['puzzle']} ").strip().lower()
        if "april 1" in ans or "1st" in ans:
            print("Correct! Map piece1 appears!")
            room["items"].append("map_piece1")
            return True
        elif "queen anne" in ans:
            print("X marks spot revealed!")
            island["jungle"]["exits"]["hidden"] = "waterfall"
            return True
        print("Wrong! Pirates get closer...")
        return False
    return True

print("Treasure Hunt: Find map pieces, get shovel, dig treasure!")
while pirate_timer > 0:
    show_status()
    
    if "treasure" in inventory:
        print("🏴‍☠️ TREASURE FOUND! YOU WIN! 🏴‍☠️")
        break
    
    action = input("\n> ").lower()
    
    if action == "quit":
        print("Pirates take everything...")
        break
    elif action in island[current_location]["exits"]:
        current_location = island[current_location]["exits"][action]
    elif "dig" in action and current_location == "waterfall" and "shovel" in inventory:
        if len([i for i in inventory if "map_piece" in i]) >= 2:
            inventory.append("treasure")
            print("SHOVEL STRIKES GOLD!")
        else:
            print("Digging blindly... nothing.")
    elif "riddle" in action or "solve" in action:
        solve_riddle()
    else:
        print("Try direction, 'grab', 'dig', or 'riddle'.")
    
    pirate_timer -= 1
    time.sleep(1)

if pirate_timer <= 0:
    print("Pirates arrived! Lost treasure forever.")