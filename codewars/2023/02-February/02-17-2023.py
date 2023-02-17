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

# DESCRIPTION:
# Well met with Fibonacci bigger brother, AKA Tribonacci.

# As the name may already reveal, it works basically like a Fibonacci, but summing the last 3 (instead of 2) numbers of the sequence to generate the next. And, worse part of it, regrettably I won't get to hear non-native Italian speakers trying to pronounce it :(

# So, if we are to start our Tribonacci sequence with [1, 1, 1] as a starting input (AKA signature), we have this sequence:

# [1, 1 ,1, 3, 5, 9, 17, 31, ...]
# But what if we started with [0, 0, 1] as a signature? As starting with [0, 1] instead of [1, 1] basically shifts the common Fibonacci sequence by once place, you may be tempted to think that we would get the same sequence shifted by 2 places, but that is not the case and we would get:

# [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
# Well, you may have guessed it by now, but to be clear: you need to create a fibonacci function that given a signature array/list, returns the first n elements - signature included of the so seeded sequence.

# Signature will always contain 3 numbers; n will always be a non-negative number; if n == 0, then return an empty array (except in C return NULL) and be ready for anything else which is not clearly specified ;)

def tribonacci(signature, n):
    if not n:
        return []
    elif n < len(signature): 
        return signature[:n]
    else:
        trib = signature

        while len(trib) < n:
            trib.append(sum(trib[-3:]))

        return trib
    
# OR

def tribonacci(signature: list[int], n: int):
    trib = signature[:n]
    while len(trib) < n:
        trib.append(sum(trib[-3:]))
    return trib

# OR (remove variable)

def tribonacci(signature: list[int], n: int):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    return signature[:n]

#==============================================================================================================

# DESCRIPTION:
# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits), which is narcissistic:

#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
# and 1652 (4 digits), which isn't:

#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938
# The Challenge:

# Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a Narcissistic number in base 10. This may be True and False in your language, e.g. PHP.

# Error checking for text strings or other invalid inputs is not required, only valid positive non-zero integers will be passed into the function.

def narcissistic(num):
    return sum(int(digit) ** len(str(num)) for digit in str(num)) == num

