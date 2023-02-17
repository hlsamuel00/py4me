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