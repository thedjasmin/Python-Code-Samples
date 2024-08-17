import globalvariables
import chapter1
import chapter4
import gameover

def start_chapter():
    print(f"\nChapter {globalvariables.chapter}: The Escape")
    print("The exit looms ahead, tantalizingly close. The final barrier between you and freedom.")

    print("\nWhat would you like to do?")
    print("1. Confront the Guards")
    print("2. Use the Secret Passage")
    print("3. Distract and Flee")
    print("4. Find an Alternate Route")

    choice = input("Choose an action (1-4): ")

    if choice == "1":
        confront_guards()
    elif choice == "2":
        use_secret_passage()
    elif choice == "3":
        distract_and_flee()
    elif choice == "4":
        find_alternate_route()
    else:
        print("Invalid choice. Try again.")
        start_chapter()

def confront_guards():
    print("You engage in a fierce battle with the guards.")
    outcome = input("Did you win the battle? (yes/no): ")

    if outcome.lower() == "yes":
        print("You defeated the guards and gained your freedom!")
        print("Ending: Freedom")
        exit()
    else:
        print("You were captured in the battle.")
        gameover.trigger_game_over()

def use_secret_passage():
    print("You successfully navigate the passage and reach freedom.")
    print("Ending: Freedom")
    exit()

def distract_and_flee():
    print("You create a diversion and manage to escape through the main gate.")
    print("Ending: Freedom")
    exit()

def find_alternate_route():
    print("You discover a hidden path that bypasses the guards.")
    globalvariables.chapter = 4
    chapter4.start_chapter()
