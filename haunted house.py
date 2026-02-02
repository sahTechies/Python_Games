import time

# Game state
current_location = "entrance"
inventory = []

# Game world: rooms with descriptions, exits, and items
game_world = {
    "entrance": {
        "description": "You stand before a creepy old haunted house. The door creaks open.",
        "exits": {"door": "living_room"},
        "items": []
    },
    "living_room": {
        "description": "Dimly lit living room with dusty furniture. Stairs lead up; door back.",
        "exits": {"door": "entrance", "stairs": "bedroom"},
        "items": ["candle"]
    },
    "bedroom": {
        "description": "Spooky bedroom. A treasure chest hides under the bed.",
        "exits": {"stairs": "living_room"},
        "items": []
    }
}

def show_status():
    print("\n" + game_world[current_location]["description"])
    exits = game_world[current_location]["exits"]
    print("Exits:", ", ".join(exits.keys()))
    
    # Show items
    items = game_world[current_location]["items"]
    if items:
        print("You see:", ", ".join(items))
        if input("Pick up an item? (yes/no): ").lower() == "yes":
            item = input("Which? ").lower()
            if item in [i.lower() for i in items]:
                inventory.append(item)
                game_world[current_location]["items"].remove(next(i for i in items if i.lower() == item))
                print(f"You picked up {item}.")

def bedroom_special():
    print("Treasure chest under the bed!")
    if "key" in [i.lower() for i in inventory]:
        print("You unlock it with the key! You find a silver crown. You win!")
        print("Inventory:", inventory)
        return True
    else:
        print("It's locked. Need a key.")
    return False

# Main game loop
print("Welcome to Haunted House! Type 'quit' to exit.")
while True:
    show_status()
    
    if current_location == "bedroom":
        if bedroom_special():
            break
    
    user_input = input(">> ").lower()
    
    if user_input == "quit":
        print("Game over. Thanks for playing!")
        break
    elif user_input in game_world[current_location]["exits"]:
        current_location = game_world[current_location]["exits"][user_input]
        time.sleep(1)
    else:
        print("Invalid move. Try again.")[web:2][page:1][page:2]
