# DESCRIPTION:
# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

# Examples (Input -> Output):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "
# Good Luck!

def double_char(s):
    new_string = ''
    for char in s:
        new_string += char * 2
    return new_string

# OR

def double_char(string):
    return ''.join(char * 2 for char in string)