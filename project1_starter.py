"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Izeal Mallory]
Date: [10/30/25]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    strength, magic, health = calculate_stats(character_class, level)

    char = {
        "name": name,
        "class": character_class,
        "level": level,
        "strength": strength,
        "magic": magic,
        "health": health,
        "gold": 100
    }
    return char
    # Remember to use calculate_stats() function for stat calculation
    pass

def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
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
        strength = 0
        magic = 0
        health = 0

    return (strength * level, magic * level, health * level)
    # Return a tuple: (strength, magic, health)
    pass

def save_character(character, 'my_character.txt'):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    with open('my_character.txt', 'w') as file:
        file.write(f"Character Name: {character.get('name', '')}\n")
        file.write(f"Class: {character.get('class', '')}\n")
        file.write(f"Level: {character.get('level', '')}\n")
        file.write(f"Strength: {character.get('strength', '')}\n")
        file.write(f"Magic: {character.get('magic', '')}\n")
        file.write(f"Health: {character.get('health', '')}\n")
        file.write(f"Gold: {character.get('gold', '')}\n")
    return True
    # Remember to handle file errors gracefully
    pass

def load_character('my_character.txt'):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    with open('my_character.txt', 'r') as file:
        character_data = {}
        for line in file:
            key, value = line.strip().split(': ', 1)
            if key == 'Character Name':
                character_data['name'] = value
            elif key == 'Class':
                character_data['class'] = value
            elif key == 'Level':
                character_data['level'] = int(value)
            elif key == 'Strength':
                character_data['strength'] = int(value)
            elif key == 'Magic':
                character_data['magic'] = int(value)
            elif key == 'Health':
                character_data['health'] = int(value)
            elif key == 'Gold':
                character_data['gold'] = int(value)
        return character_data
    # Remember to handle file not found errors
    pass

def display_character(char):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    pass

def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    character['level'] += 1
    character['strength'] += 2
    character['magic'] += 3
    character['health'] += 10
    character['gold'] += 50
    # Remember to recalculate stats for the new level
    pass

# Main program area (optional - for testing your functions)
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
