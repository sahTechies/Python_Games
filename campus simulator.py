import time
import random

current_location = "hostel"
gpa = 8.5
energy = 100
cash = 200
clock = 8  # 8 AM

campus = {
    "hostel": {
        "desc": "Your messy hostel room. Books everywhere. Class in 30 min.",
        "exits": {"classroom": "classroom", "canteen": "canteen"},
        "action": "sleep (+energy)"
    },
    "classroom": {
        "desc": "AIML class in session. Prof teaching Neural Networks.",
        "exits": {"hostel": "hostel", "library": "library"},
        "action": "attend (+GPA, -energy)"
    },
    "library": {
        "desc": "Silent library. Perfect for DSA practice or project work.",
        "exits": {"classroom": "classroom", "canteen": "canteen"},
        "action": "study (+GPA, -energy)"
    },
    "canteen": {
        "desc": "Busy canteen. Sambar rice or parotta? Mess food special.",
        "exits": {"hostel": "hostel", "sports": "sports"},
        "action": "eat (+energy, -cash)"
    },
    "sports": {
        "desc": "Campus ground. Cricket or volleyball? Relieve exam stress.",
        "exits": {"canteen": "canteen"},
        "action": "play (+energy)"
    }
}

def show_status():
    global clock
    room = campus[current_location]
    print(f"\n⏰ {clock}:00 | GPA: {gpa:.1f} | Energy: {energy} | Cash: ₹{cash}")
    print(room["desc"])
    print(f"Go: {', '.join(room['exits'].keys())} | {room['action']}")

print("SRM Campus Simulator: Survive semester with GPA > 8.0!")
while energy > 0 and gpa >= 4.0 and clock < 22:
    show_status()
    
    action = input("\n> ").lower()
    
    if action == "quit":
        break
    elif action in campus[current_location]["exits"]:
        current_location = campus[current_location]["exits"][action]
    elif "sleep" in action and current_location == "hostel":
        energy = min(100, energy + 30)
    elif "attend" in action and current_location == "classroom":
        gpa += 0.2
        energy -= 15
    elif "study" in action and current_location == "library":
        gpa += 0.3
        energy -= 20
    elif "eat" in action and current_location == "canteen" and cash >= 30:
        energy = min(100, energy + 40)
        cash -= 30
    elif "play" in action and current_location == "sports":
        energy = min(100, energy + 25)
    else:
        print("Invalid! Try location name or action.")
    
    # Random campus events
    if random.random() < 0.3:
        events = ["Prof quiz! GPA -0.1", "Fest prep duty!", "Free biryani!", "Lab crash!"]
        event = random.choice(events)
        print(f"⚡ {event}")
        if "quiz" in event: gpa -= 0.1
        if "biryani" in event: energy += 10
    
    clock += 2  # Time passes
    time.sleep(1)

if gpa >= 8.0:
    print("🎉 Semester cleared with First Class!")
elif energy <= 0:
    print("😴 Burnout! Need hostel break.")
else:
    print("📉 GPA dropped. Summer classes!")


