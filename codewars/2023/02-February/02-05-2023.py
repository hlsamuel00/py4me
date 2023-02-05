# DESCRIPTION:
# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:
#     XO("ooxx") => true
#     XO("xooxx") => false
#     XO("ooxXm") => true
#     XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
#     XO("zzoo") => false

def xo(string):
    string = string.lower()
    return string.count('x') == string.count('o')


# OR

def xo(string: str) -> bool:
    exes = 0
    ohs = 0

    for char in string.lower():
        if char == 'x': exes += 1
        if char == 'o': ohs += 1

    return exes == ohs

# OR

from collections import Counter

def xo(string: str) -> bool:
    count = Counter(string.lower())
    return count.get('x', 0) == count.get('o', 0)