# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

def find_short(string: str) -> str:
    return min(len(word) for word in string.split(' '))

#==============================================================================================================

# DESCRIPTION:
# This time no story, no theory. The examples below show you how to write function accum:

# Examples:
#     accum("abcd") -> "A-Bb-Ccc-Dddd"
#     accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
#     accum("cwAt") -> "C-Ww-Aaa-Tttt"
#     The parameter of accum is a string which includes only letters from a..z and A..Z

def accum(string: str) -> str:
    return '-'.join((letter * idx).capitalize() for idx, letter in enumerate(string, 1))