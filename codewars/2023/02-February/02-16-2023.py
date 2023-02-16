# DESCRIPTION:
# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))
#     1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
#     5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

def add_binary(num1: int, num2: int) -> str:
    return bin(num1 + num2).replace('0b', '')

#==============================================================================================================

# In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213

# It will need 3 entire years.

def nb_year(p0, percent, aug, p, year_count = 0):
    
    while p0 < p:
        p0 += int(p0 * percent/100) + aug
        year_count += 1
    
    return year_count

# OR (with recursion)

def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year((p0 + int(p0 * (percent / 100)) + aug), percent, aug, p, years + 1)
    else:
        return years
    
#==============================================================================================================

# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# Examples:
#     a = "xyaabbbccccdefww"
#     b = "xxxxyyyyabklmopq"
#     longest(a, b) -> "abcdefklmopqwxy"

#     a = "abcdefghijklmnopqrstuvwxyz"
#     longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    return ''.join(sorted(set(a1).union(set(a2))))

# OR

def longest(string1: str, string2: str) -> str:
    return ''.join(sorted(set(string1 + string2)))

# OR

def longest(str1: str, str2: str) -> str:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sorted_str = ''

    for letter in alphabet:
        if letter in (str1 + str2).lower():
            sorted_str += letter
    
    return sorted_str

#==============================================================================================================

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst: list[int]) -> list[int]:
    total_zeroes = lst.count(0)
    
    while 0 in lst:
        lst.remove(0)
            
    return lst + [0] * total_zeroes

#==============================================================================================================

# DESCRIPTION:
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
#     "1234"   -->  true
#     "12345"  -->  false
#     "a234"   -->  false

def validate_pin(pin):
    return all(char.isdigit() for char in pin) and (len(pin) == 4 or len(pin) == 6)

# OR

def validate_pin(pin:str) -> bool:
    return len(pin) in (4, 6) and pin.isdigit()

# OR

from re import fullmatch

def validate_pin(pin):
    return bool(fullmatch('^(\d{4}|\d{6})$', pin))

#==============================================================================================================

# DESCRIPTION:
# Given the triangle of consecutive odd numbers:

#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# ...
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

# 1 -->  1
# 2 --> 3 + 5 = 8

def row_sum_odd_numbers(n):
    return n ** 3

#==============================================================================================================

# DESCRIPTION:
# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

def is_pangram(string: str) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return all(letter in string.lower() for letter in alphabet)