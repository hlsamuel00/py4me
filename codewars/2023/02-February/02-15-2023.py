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

# DESCRIPTION:
# Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a: int, b: int, c: int) -> bool:
    return a + b > c and a + c > b and b + c > a

# OR

def is_triangle(a: int, b: int, c: int) -> bool:
    a, b, c = sorted((a, b, c))
    return a + b > c

#==============================================================================================================

# DESCRIPTION:
# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples
#     "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
#     "4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
#     ""  -->  ""

from re import findall
def order(sentence: str) -> str:
    if not sentence: return ''

    word_list = sentence.split(' ')
    
    sorted_sentence = [''] * len(word_list)
    
    for word in word_list:
        idx = int(findall('\d', word)[0]) - 1
        sorted_sentence[idx] = word
    
    return ' '.join(sorted_sentence)

# OR

def order(sentence: str) -> str:
    return ' '.join(sorted(sentence.split(' '), key = lambda word: sorted(word)))

# OR

def find_digit(word: str) -> int:
  for char in word:
      if char.isdigit():
          return int(char)

def order(sentence: str) -> str:
    return ' '.join(sorted(sentence.split(), key=find_digit))