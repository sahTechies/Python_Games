import time
import random

current_room = "classroom"
inventory = []
game_time = 0  # Simple timer

rooms = {
    "classroom": {
        "desc": "You're locked in your empty classroom after hours. Desk, blackboard, door (locked).",
        "exits": {},
        "items": ["math_notebook"],
        "puzzle": None
    },
    "hallway": {
        "desc": "Dark school hallway. Classrooms left/right, principal office ahead, exit far end.",
        "exits": {"left": "lab", "right": "library", "ahead": "office"},
        "items": [],
        "puzzle": "What is 2+2*3? (answer: 8)"
    },
    "lab": {
        "desc": "Computer lab. Find hall_key on keyboard table.",
        "exits": {"back": "hallway"},
        "items": ["hall_key"],
        "puzzle": None
    },
    "library": {
        "desc": "Library with books. Riddle: 'I speak without mouth, hear without ears. What am I?' (echo)",
        "exits": {"back": "hallway"},
        "items": [],
        "puzzle": "echo"
    },
    "office": {
        "desc": "Principal's office. Safe needs code from notebook.",
        "exits": {"back": "hallway"},
        "items": ["exit_key"] if "math_notebook" in inventory else [],
        "puzzle": "Safe code is 314 (pi)"
    },
    "exit": {
        "desc": "School gate! You escaped!",
        "exits": {},
        "items": [],
        "puzzle": None
    }
}

def show_status():
    global game_time
    room = rooms[current_room]
    print(f"\n--- Turn {game_time} ---")
    print(room["desc"])
    if room["items"]:
        print("Items: " + ", ".join(room["items"]))
    print("Exits: " + ", ".join(room["exits"]) if room["exits"] else "No exits.")
    
    # Pick up
    if room["items"]:
        if input("Take item? (y/n): ").lower() == 'y':
            item = input("Which? ").strip()
            if item in room["items"]:
                inventory.append(item)
                room["items"].remove(item)
                print(f"Got {item}!")

def solve_puzzle():
    room = rooms[current_room]
    if room["puzzle"]:
        ans = input(f"Puzzle: {room['puzzle']} ").strip().lower()
        if "2+2*3" in room["puzzle"] and ans == "8":
            print("Correct! Door unlocked.")
            return True
        elif room["puzzle"] == "echo" and "echo" in ans:
            print("Echo reveals hidden door!")
            rooms["hallway"]["exits"]["hidden"] = "office"
            return True
        elif "pi" in room["puzzle"] and ans == "314":
            print("Safe opens! Got exit_key.")
            room["items"].append("exit_key")
            return True
        else:
            print("Wrong! Watchman alert rises...")
            return False
    return True

print("School Escape: Find keys, solve puzzles, escape before time runs out!")
while game_time < 10:  # 10-turn limit
    show_status()
    
    if current_room == "exit":
        print("YOU ESCAPED! 🎉")
        break
    
    action = input("\n> ").lower()
    
    if action == "quit":
        print("Trapped forever...")
        break
    elif action in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][action]
    elif "unlock" in action and "hall_key" in inventory and current_room == "classroom":
        current_room = "hallway"
        print("Unlocked with hall_key!")
    elif "exit" in action and "exit_key" in inventory and current_room == "hallway":
        current_room = "exit"
    else:
        print("Invalid. Try direction or 'take'.")
        solve_puzzle()  # Check puzzles
    
    game_time += 1
    time.sleep(1)

if game_time >= 10:
    print("Watchman caught you! Game over.")
