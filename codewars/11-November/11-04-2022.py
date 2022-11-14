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

