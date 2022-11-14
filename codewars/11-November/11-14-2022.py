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