# DESCRIPTION:
# Welcome.

# In this kata you are required to, given a string, replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.

# Example
#     alphabet_position("The sunset sets at twelve o' clock.")
#     Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

def alphabet_position(text: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ' '.join(str(alphabet.index(char) + 1) for char in text.lower() if char in alphabet)
    
#==============================================================================================================

# DESCRIPTION:
# You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

def is_valid_walk(walk):
    return walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w') and len(walk) == 10

# OR

def is_valid_walk(walk: list[str]) -> bool:
    if len(walk) != 10: return False

    x,y = 0,0
    
    for block in walk:
        if block == 'n':
            y += 1
        elif block == 's':
            y -= 1
        elif block == 'e':
            x += 1
        else:
            x -= 1
        
    return not x and not y