# Python_Games

<B>Escape game <br></B>
flow chart <br>
Start → Door Choice (Left: Normal | Right: Enemy+20HP | Wait: Player-10HP)<br>
     ↓ <br>
Combat Loop (Player Attack → Enemy Counter → Check HP)<br>
     ↓<br>
End (Player ≤0: Defeat | Enemy ≤0: Escape)<br>


haunted house

[START]
   |
[Initialize: location="entrance", inventory=[]]
   |
[Display Welcome]
   |
[Main Loop START]
   | 
[Show Status: desc, exits, items]
   |
[In Bedroom? --> Yes --> Check Key in Inventory? --> Yes --> WIN! --> [END]]
   | No                          | No
   |                             [Need Key Msg] --> Back to Loop
[Get Input]
   |
[Input == "quit"? --> Yes --> [Game Over] --> [END]]
   | No
[Valid Exit? --> Yes --> Move to New Location --> Back to Loop]
   | No
[Invalid Msg] --> Back to Loop
[Main Loop END - theoretical, broken by conditions]


school escape
       [START]
         |
    [Init: room=classroom, inv=[], time=0]
         |
      [Main Loop: time < 10?]
    No --> [Time Up: Lose] --> [END]
    Yes
         |
    [show_status() + pickup?]
         |
    [room == "exit"? --> Yes --> WIN! --> [END]]
         | No
    [Get action input]
         |
[quit? --> Yes --> [END]]
    | No
[Valid exit? --> Yes --> Update room --> Loop]
    | No
["unlock" + key? --> Yes --> Special room --> Loop]
    | No
[puzzle? --> Correct? --> Yes --> Reward/Unlock --> Loop]
              | No --> Wrong msg --> Loop
    [Invalid] --> Loop


space mission 

         [START]
           |
   [Init: planet=earth, inv=[], O2=100]
           |
    [Main Loop: O2 > 0?]
       No ──> [O2 Depleted: FAIL] ──> [END]
       Yes
           |
    [show_status() + pickup?]
           |
[planet=="home"? ── Yes ──> MISSION SUCCESS! ──> [END]]
       No
    [Get action input]
           |
[quit? ── Yes ──> [END]]
    No
[Valid planet? ── Yes ── Warp + O2-=rand(5-15) ──> Loop]
     No
["scan"? ── Yes ── Puzzle? Correct? ──> Yes: Reward ──> Loop]
                │ No: O2-=2 ──> Loop
[Invalid ── O2-=2 ──> Loop]


treasure hunt 

algrithm 
1. Initialize: current_location = "beach", inventory = [], pirate_timer = 8
2. Print "Treasure Hunt: Find map pieces + shovel → dig treasure!"
3. WHILE pirate_timer > 0:
   a. show_status(): Print timer, room desc, items, exits
   b. Handle pickup if items present
   c. IF "treasure" in inventory: WIN! Break
   d. Get player action input
   e. IF action == "quit": Lose, break
   f. ELSE IF action in exits: Move to new location
   g. ELSE IF "dig" AND location=="waterfall" AND shovel AND 2+ map pieces: Get treasure
   h. ELSE IF "riddle"/"solve": Attempt puzzle solution
   i. ELSE: Invalid message
   j. pirate_timer -= 1
4. IF pirate_timer <= 0: Pirates win, game over

flowchart 
         [START]
           |
[Init: beach, inv=[], timer=8]
           |
[Main Loop: timer > 0?]
      No ──> [PIRATES WIN: Lose] ──> [END]
      Yes
           |
    [show_status() + pickup?]
           |
["treasure" in inv? ── Yes ──> TREASURE FOUND! ──> [END]]
           No
    [Get action input]
           |
[quit? ── Yes ──> [END]]
     No
[Valid exit? ── Yes ──> Move location ──> Loop]
     No
["dig" + right items? ── Yes ──> Get treasure ──> Loop]
                No
["riddle"? ── Correct? ── Yes ──> Unlock reward ──> Loop]
                   No ──> Wrong, timer-- ──> Loop
[Invalid ── timer-- ──> Loop]


campus simulator 
BEGIN Campus Simulator
  SET current_location = "hostel"
  SET gpa = 8.5, energy = 100, cash = 200, clock = 8
  
  OUTPUT "SRM Campus Simulator: Survive semester with GPA ≥ 8.0!"
  
  WHILE (energy > 0 AND gpa >= 4.0 AND clock < 22)
    CALL show_status()  // Display time, stats, room desc, exits, actions
    
    INPUT action
    
    IF action == "quit"
      BREAK
    
    ELSE IF action in campus[current_location].exits
      SET current_location = campus[current_location].exits[action]
    
    ELSE IF action matches location-specific action AND requirements met
      UPDATE stats accordingly  // +GPA/-energy, +energy/-cash, etc.
    
    ELSE
      OUTPUT "Invalid! Try location or action."
    
    // Random campus events (30% chance)
    IF random() < 0.3
      event = random.choice(["Prof quiz! GPA -0.1", "Free biryani!", ...])
      APPLY event effects
    
    clock += 2
  END WHILE
  
  IF gpa >= 8.0
    OUTPUT "Semester cleared with First Class!"
  ELSE IF energy <= 0
    OUTPUT "Burnout! Need hostel break."
  ELSE
    OUTPUT "GPA dropped. Summer classes!"
END


flowchart 
         [START]
           |
[Initialize: hostel, gpa=8.5, energy=100, cash=200, clock=8]
           |
[Main Loop: energy>0 ∧ gpa≥4.0 ∧ clock<22?]
       No ──> [END with Results] ──> [END]
       Yes
           |
    [show_status(): Display stats/time/location]
           |
    [Get player action input]
           |
[Valid location move? ── Yes ──> Update location ──> Loop]
     No
[Valid action + requirements? ── Yes ──> Update stats ──> Loop]
                   No ──> "Invalid" ──> Loop
           |
[Random event? (30%) ── Yes ──> Apply effect ──> Loop]
           No ──> 
    [clock += 2] ──> Loop
