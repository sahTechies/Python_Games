import random

rooms = ["Entrance", "Hallway", "Chamber", "Tunnel", "Gate"]
room_types = ["safe", "enemy", "trap", "treasure", "mystery"]

enemies = ["Goblin", "Skeleton", "Dark Rat"]
loot = ["potion", "bomb", "gold"]

position = 0
health = 100
inventory = []
key_found = False

print("\n=== DUNGEON ESCAPE ===")
print("Survive. Find the key. Escape.\n")

while True:

    current_room = rooms[position]
    room_event = random.choice(room_types)

    print("\nYou enter:", current_room)
    print("Health:", health)

    action = input("move / search / inventory / quit: ").lower()

    if action == "move":
        if position < len(rooms) - 1:
            position += 1
        else:
            print("A locked gate blocks your path.")

    elif action == "search":

        if room_event == "safe":
            print("Nothing here. Too quiet.")

        elif room_event == "trap":
            dmg = random.randint(10, 25)
            health -= dmg
            print("TRAP! You lose", dmg, "HP.")

        elif room_event == "enemy":
            enemy = random.choice(enemies)
            print("A", enemy, "appears!")

            choice = input("fight or run: ")

            if choice == "fight":
                dmg = random.randint(5, 20)
                health -= dmg
                print("You defeated it but lost", dmg, "HP.")
            else:
                escape = random.randint(0, 1)
                if escape == 0:
                    dmg = random.randint(10, 20)
                    health -= dmg
                    print("Couldn't escape! Lost", dmg, "HP.")
                else:
                    print("You escaped safely.")

        elif room_event == "treasure":
            item = random.choice(loot)
            inventory.append(item)
            print("You found:", item)

            if item == "potion":
                print("Use potion automatically.")
                health += 20

        elif room_event == "mystery":
            event = random.randint(1, 5)

            if event == 1:
                health += 15
                print("A warm light heals you (+15).")

            elif event == 2:
                health -= 15
                print("Poison gas! (-15)")

            elif event == 3:
                inventory.append("key")
                key_found = True
                print("You found the EXIT KEY.")

            elif event == 4:
                position = random.randint(0, len(rooms)-1)
                print("A portal warps you elsewhere!")

            else:
                print("Nothing happens. Suspicious.")

    elif action == "inventory":
        print("Inventory:", inventory)

    elif action == "quit":
        print("You gave up.")
        break

    else:
        print("Invalid choice.")

    if position == len(rooms) - 1 and key_found:
        print("\nThe gate opens slowly...")
        print("You escaped the dungeon.")
        break

    if health <= 0:
        print("\nYour vision fades.")
        print("You died in the dungeon.")
        break