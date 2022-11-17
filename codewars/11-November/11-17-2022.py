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

# DESCRIPTION:
# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

# For example:

# summation(2) -> 3
# 1 + 2

# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

def summation(num):
    return sum( [ idx + 1 for idx in range(num) ] )

# OR

def summation(num):
    return sum( range(1,num+1) )

#==============================================================================================================

# DESCRIPTION:
# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

# For example,

# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.

# Hint: Don't forget to check for bad values like null/undefined

def count_sheeps(sheep):
    return sheep.count(True)

#==============================================================================================================

# DESCRIPTION:
# Description:
# Make a simple function called greet that returns the most-famous "hello world!".

# Style Points
# Sure, this is about as easy as it gets. But how clever can you be to create the most creative hello world you can think of? What is a "hello world" solution you would want to show your friends?

def greet():
    return 'hello world!'

#==============================================================================================================

# DESCRIPTION:
# Note: This kata is inspired by Convert a Number to a String!. Try that one too.

# Description
# We need a function that can transform a string into a number. What ways of achieving this do you know?

# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

# Examples
# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7

def string_to_number(string):
    try:
        return int(string)
    except (ValueError):
        return 'Invalid Input!'

#==============================================================================================================