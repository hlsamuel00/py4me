# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example (Input --> Output):
#     39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
#     999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
#     4 --> 0 (because 4 is already a one-digit number)

def persistence(n):
    loops = 0
    
    while n > 9:
        product = 1
        
        for digit in str(n):
            product *= int(digit)
        
        n = product
        loops += 1
    
    return loops

# OR

def persistence(n, loops = 0):
    if n < 10:
         return loops
    else:
        product = 1
        for digit in str(n):
            product *= int(digit)

        return persistence(product, loops + 1)

#==============================================================================================================

# DESCRIPTION:
# Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all but the last four characters into '#'.

# Examples
#     "4556364607935616" --> "############5616"
#         "64607935616" -->      "#######5616"
#                 "1" -->                "1"
#                     "" -->                 ""

# // "What was the name of your first pet?"

#     "Skippy" --> "##ippy"

#     "Nananananananananananananananana Batman!" --> "####################################man!"

def maskify(cc: str) -> str:
    return cc[-4:].rjust(len(cc), '#')

#==============================================================================================================

# DESCRIPTION:
# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

# For example:
#     unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#     unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#     unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
#     unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

def unique_in_order(sequence: str) -> list:
    order_list = []
    if len(sequence) < 1: return order_list 

    order_list.append(sequence[0])
    for idx in range(1, len(sequence)):
        if sequence[idx - 1] == sequence[idx]:
            continue
        else:
            order_list.append(sequence[idx])
    
    return order_list

# OR
        
def unique_in_order(sequence: str) -> list[str]:
    order_list = []
    if len(sequence) < 1: return order_list

    for idx in range(len(sequence)):
        if not idx or sequence[idx - 1] != sequence[idx]:
            order_list.append(sequence[idx])
    
    return order_list

#==============================================================================================================

# DESCRIPTION:
# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:
#     solution('abc', 'bc') # returns true
#     solution('abc', 'd') # returns false

def solution(text: str, ending: str) -> bool:
    return text.endswith(ending)

#==============================================================================================================

# DESCRIPTION:
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

from re import split
def to_camel_case(text: str) -> str:
    camelCase = ''

    for idx, word in enumerate(split('[^a-zA-Z]', text)):
        if not idx:
            camelCase += word
        else:
            camelCase += word.capitalize()
    
    return camelCase

# OR

from re import split
def to_camel_case(text: str) -> str:
    wordList = split('[^a-zA-Z]',text)
    return wordList[0] + ''.join(word.capitalize() for word in wordList[1:])

#==============================================================================================================

# DESCRIPTION:
# Make a program that filters a list of strings and returns a list with only your friends name in it.

# If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

# i.e.

# friend ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]
# Note: keep the original order of the names in the output.

def friend(friend_list: list[str]) -> list[str]:
    return [friend for friend in friend_list if len(friend) == 4]

#==============================================================================================================

