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

# DESCRIPTION:
# Nathan loves cycling.

# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

# For example:

# time = 3 ----> litres = 1

# time = 6.7---> litres = 3

# time = 11.8--> litres = 5

def litres(time):
    return int(time * .5)

# OR

def lires(time):
    return time // 2

#==============================================================================================================

# DESCRIPTION:
# Introduction
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in.

# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20

import math
def century(year):
    return math.ceil(year / 100)

# OR

def century(year):
    return -(-year//100)

