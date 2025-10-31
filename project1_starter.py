"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Izeal Mallory]
Date: [10/30/25]

AI Usage: AI helped me identify and correct a critical logical flaw in the level_up 
function, ensuring that character stats are correctly recalculated (using calculate_stats) 
based on the new level, rather than incorrectly stacking fixed increments. AI also helped 
me fix the logic in my save_character function. I used AI to help me debug and explain to meme
how to correctly write the required format to the file.
"""

 #Creates a new character dictionary with initial stats
 def create_character(name, character_class):
    level = 1
    #Calculate the base stats for level 1 characters of this class
    strength, magic, health = calculate_stats(character_class, level)
    #list of recognized character classes
    valid_classes = ["Warrior", "Mage", "Rogue", "Cleric"]
    #Checks if the provided class name is in the list of valid classes
    if character_class not in valid_classes:
        return None
    
    #Assembles all attributes into the final character dictionary
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }
    return character

#Calculates the total strength, magic, and health based on the class and level
def calculate_stats(character_class, level):
    #Determines base stats (Level 1 values) based on class
    if character_class == "Warrior":
        strength = 10
        magic = 2
        health = 100
    elif character_class == "Mage":
        strength = 5
        magic = 15
        health = 80
    elif character_class == "Rogue":
        strength = 8
        magic = 8
        health = 70
    elif character_class == "Cleric":
        strength = 7
        magic = 12
        health = 90
    else:
        print("Invalid character")
        return calculate_stats("Mage", level)
    return strength * level, magic * level, health * level

#Saves character to a text file in the required descriptive format
#Includes basic checks for valid data/filename
def save_character(character, filename):
    import os
    #Checks if inputs are valid dictionary and filename
    if not isinstance(character, dict) or not filename:
        return False
    #Checks if the directory exists
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        return False
    #Use 'with open' to ensure the file is closed automatically
    with open(filename, 'w') as file:
        #Writes each attribute line in the exact required format
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
    return True

import os
def load_character(filename):
    #Checks if the file exist
    if not os.path.exists(filename):
        return None
    #Opens the file and reads the line
    with open(filename) as file:
        lines = file.readlines()
        character_data = {}
        for line in lines:
            key, value = line.strip().split(': ', 1)
            if key == 'Character Name':
                character_data['name'] = value
                print(character_data['name'])
            elif key == 'Class':
                character_data['class'] = value
                print(character_data['class'])
            elif key == 'Level':
                character_data['level'] = int(value)
                print(character_data['level'])
            elif key == 'Strength':
                character_data['strength'] = int(value)
                print(character_data['strength'])
            elif key == 'Magic':
                character_data['magic'] = int(value)
                print(character_data['magic'])
            elif key == 'Health':
                character_data['health'] = int(value)
                print(character_data['health'])
            elif key == 'Gold':
                character_data['gold'] = int(value)
                print(character_data['gold'])
        return character_data

#Prints a formatted character sheet to the console
def display_character(character):
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print("=" * 20)

#Increases character level and recalculates all core stats
#Modifies the character dictionary directly
def level_up(character):
    character['level'] += 1
    #Recalculates stats based on NEW level
    strength, magic, health = calculate_stats(character['class'], character['level'])
    #Applies new calculated stats (replaces new values with new total)
    character['strength'] = strength
    character['magic'] = magic
    character['health'] = health
    character['gold'] += 50
    print(f"{character['name']} has level up!")

#A main program area to test application logic
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Create your own character!")
    #Gets user's input for creation
    user_name = input("What is your name? ")
    player_class = input("What class will you make? (Warrior, Mage, Rogue, or Cleric): ")

    char = create_character(user_name, player_class)
    if char is not None:
        display_character(char)
        level_up(char)
        save_character(char, "my_character.txt")
        loaded = load_character("my_character.txt")
        print("Character loaded from file: ")
        display_character(loaded)
    else:
        print("Invalid class type! Please pick Warrior, Mage, Rogue, or Cleric.")   
