# DESCRIPTION:
# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.

def remove_char(s):
    return s[1:-1]


#==============================================================================================================


# Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.


def find_smallest_int(arr):
    smallest = arr[0]
    for num in arr:
        if smallest > num:
            smallest = num
    return smallest

# OR

def find_smallest_int(arr):
    return min(arr)


#==============================================================================================================


# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

def square_sum(numbers):
    return sum( number ** 2 for number in numbers )


#==============================================================================================================

# DESCRIPTION:
# Simple, remove the spaces from the string, then return the resultant string.

def no_space(string):
    return string.replace(' ','')

#==============================================================================================================
