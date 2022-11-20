# DESCRIPTION:
# Code as fast as you can! You need to double the integer and return it.

def double_integer(i):
    return i * 2

#==============================================================================================================

# DESCRIPTION:
# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

def digitize(n):
    digits = [ int(digit) for digit in f'{n}']
    digits.reverse()
    return digits

# OR

def digitize(n):
    return [ int(digit) for digit in f'{n}' ][::-1]
