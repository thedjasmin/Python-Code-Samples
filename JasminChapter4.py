import globalvariables
import chapter3
import chapter5
import gameover

def start_chapter():
    print(f"\nChapter {globalvariables.chapter}: The Laboratory")
    print("The sterile, cold atmosphere of the laboratory contrasts sharply with the chaos outside.")
    print("The air is thick with chemical fumes.")

    print("\nWhat would you like to do?")
    print("1. Search for Documents")
    print("2. Disable Security Systems")
    print("3. Confront the Professor")
    print("4. Unlock the Main Door")

    choice = input("Choose an action (1-4): ")

    if choice == "1":
        search_for_documents()
    elif choice == "2":
        disable_security_systems()
    elif choice == "3":
        confront_professor()
    elif choice == "4":
        unlock_main_door()
    else:
        print("Invalid choice. Try again.")
        start_chapter()

def search_for_documents():
    print("You uncover evidence of illegal experiments, finding a clue to escape.")
    globalvariables.chapter = 5
    chapter5.start_chapter()

def disable_security_systems():
    print("You open the main exit, triggering an alarm in the process.")
    globalvariables.chapter = 3
    chapter3.start_chapter()

def confront_professor():
    print("You find the professor’s body, but guards arrive, leading to your capture.")
    gameover.trigger_game_over()

def unlock_main_door():
    print("You successfully unlock the door without triggering alarms.")
    globalvariables.chapter = 5
    chapter5.start_chapter()
