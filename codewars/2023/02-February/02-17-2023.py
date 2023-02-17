# DESCRIPTION:
# You might know some pretty large perfect squares. But what about the NEXT one?

# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

# If the parameter is itself not a perfect square then -1 should be returned. You may assume the parameter is non-negative.

# Examples:(Input --> Output)
#     121 --> 144
#     625 --> 676
#     114 --> -1 since 114 is not a perfect square

def find_next_square(num):
    sqr_root = int(num ** (1/2))
    
    if sqr_root ** 2 != num:
        return -1
    else:
        return (sqr_root + 1) ** 2
    

# OR 

def find_next_square(num: int) -> int:
    root = num ** .5
    return (root + 1) ** 2 if root.is_integer() else -1

#==============================================================================================================

# DESCRIPTION:
# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

# Examples
#     pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#     pig_it('Hello world !')     # elloHay orldway !

def pig_it(text: str) -> str:
    return ' '.join(f'{word[1:]}{word[0]}ay' if word.isalpha() else word for word in text.split(' '))

# OR

from re import sub

def pig_it(text: str) -> str:
    return sub(r'(\w)(\w*)', r'\2\1ay', text)

#==============================================================================================================

# DESCRIPTION:
# The Western Suburbs Croquet Club has two categories of membership, Senior and Open. They would like your help with an application form that will tell prospective members which category they will be placed.

# To be a senior, a member must be at least 55 years old and have a handicap greater than 7. In this croquet club, handicaps range from -2 to +26; the better the player the lower the handicap.

# Input
# Input will consist of a list of pairs. Each pair contains information for a single potential member. Information consists of an integer for the person's age and an integer for the person's handicap.

# Output
# Output will consist of a list of string values (in Haskell and C: Open or Senior) stating whether the respective member is to be placed in the senior or open category.

# Example
# input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
# output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]

def open_or_senior(data):
    return ['Senior' if age >= 55 and handicap > 7 else 'Open' for age, handicap in data]


#==============================================================================================================

