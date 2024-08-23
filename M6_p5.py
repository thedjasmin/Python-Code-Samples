# Jasmin Duishebaeva
# 08.22.2024
# Write a function that checks whether your game character has picked up all the items needed to perform certain tasks and checks against any status debuffs. Confirm checks with print statements.

# Game Character has the following item list: [pan, paper, idea, rope, groceries]
# Game Character has the following status debuffs: [slow]

# Task 1: Climb a mountain – needs rope, coat, and first aid kit, cannot have slow

# Task 2: Cook a meal – needs pan, groceries, cannot have small

# Task 3: Write a book – needs pen, paper, idea, cannot have confusion


# Given character class and instance
class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

player1 = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])

# Function to check tasks
def check_tasks(character):
    # Task 1: Climb a mountain
    if 'rope' in character.weapons and 'coat' in character.weapons and 'first aid kit' in character.weapons and 'slow' not in character.weaknesses:
        print("Task 1: Climb a mountain - Requirements met.")
    else:
        print("Task 1: Climb a mountain - Requirements not met.")

    # Task 2: Cook a meal
    if 'pan' in character.weapons and 'groceries' in character.weapons and 'small' not in character.weaknesses:
        print("Task 2: Cook a meal - Requirements met.")
    else:
        print("Task 2: Cook a meal - Requirements not met.")

    # Task 3: Write a book
    if 'pen' in character.weapons and 'paper' in character.weapons and 'idea' in character.weapons and 'confusion' not in character.weaknesses:
        print("Task 3: Write a book - Requirements met.")
    else:
        print("Task 3: Write a book - Requirements not met.")

# Check tasks for player1
check_tasks(player1)
