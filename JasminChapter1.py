import globalvariables
import chapter2
import chapter3
import gameover

def start_chapter():
    print(f"\nChapter {globalvariables.chapter}: The Awakening")
    print("It was an ordinary night until the sirens blared and the lights flickered, leaving the corridors in a shadowy gloom.")
    
    print("\nWhat would you like to do?")
    print("1. Explore the Room")
    print("2. Check the Door")
    print("3. Talk to a Fellow Patient")
    print("4. Exit the Room Recklessly")

    choice = input("Choose an action (1-4): ")

    if choice == "1":
        explore_room()
    elif choice == "2":
        check_door()
    elif choice == "3":
        talk_to_patient()
    elif choice == "4":
        reckless_exit()
    else:
        print("Invalid choice. Try again.")
        start_chapter()

def explore_room():
    globalvariables.player.room_explored = True
    globalvariables.player.note_found = True
    print("You find a hidden note with a hint about a secret passage.")
    globalvariables.chapter = 3
    chapter3.start_chapter()

def check_door():
    globalvariables.player.door_checked = True
    print("The door is unlocked, and you cautiously step into the hallway.")
    globalvariables.chapter = 2
    chapter2.start_chapter()

def talk_to_patient():
    globalvariables.player.ally_met = True
    print("You gain valuable information about the hospital's layout and learn about a potential ally in another wing.")
    globalvariables.chapter = 3
    chapter3.start_chapter()

def reckless_exit():
    globalvariables.player.captured = True
    print("You alert the guards and are captured.")
    gameover.trigger_game_over()
