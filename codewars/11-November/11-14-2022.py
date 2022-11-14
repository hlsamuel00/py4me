# This code does not execute properly. Try to figure out why.

# Code Provided:
def multiply(a, b):
    a * b

# Updated Code:
def multiply(a,b):
    return a * b

# My code:
def multiply(a, b):
    try:
        int(a)
        int(b)
        return a * b
    except:
        print('Please enter a numerical value')
        quit()

#==============================================================================================================

# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    if number % 2:
        return 'Odd'
    else :
        return 'Even'

# OR

def even_or_odd(number): 
    return "Even" if not(number % 2) else "Odd"

# OR

def even_or_odd(number):
    return 'Odd' if number & 1 else 'Even'

#==============================================================================================================

# DESCRIPTION:
# Very simple, given an integer or a floating-point number, find its opposite.

# Examples:

# 1: -1
# 14: -14
# -34: 34

def opposite(number):
    try:
        return -number
    except:
        print('Please enter valid numerical value.')
        quit()

#==============================================================================================================

# DESCRIPTION:
# We need a function that can transform a number (integer) into a string.

# What ways of achieving this do you know?

# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"

def number_to_string(num):
    return str(num)