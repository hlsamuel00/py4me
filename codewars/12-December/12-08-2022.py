# DESCRIPTION:
# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    result = 1
    for num in arr:
        result *= num
    return result

# OR

from math import prod
def grow(arr):
    return prod(arr)