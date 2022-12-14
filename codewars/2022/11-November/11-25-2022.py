# Write a function which converts the input string to uppercase.

def make_upper_case(s:str):
    return s.upper()

#==============================================================================================================

# DESCRIPTION:
# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

def count_positives_sum_negatives(nums):
    if not nums: return []
    count = 0
    sum = 0
    for num in nums:
        if num < 0:
            sum += num
        if num > 0:
            count += 1
    return [count, sum]

#==============================================================================================================

# DESCRIPTION:
# Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

# Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

# Example:
# n= 5, m=5: 25
# n=-5, m=5:  0
# Waiting for translations and Feedback! Thanks!

def paperwork(classmates, pages):
    if classmates < 1 or pages < 1:
        return 0
    return classmates * pages

# OR

def paperwork(classmates, pages):
    return max(classmates, 0) * max(pages, 0)

#==============================================================================================================

# DESCRIPTION:
# Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each. If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.

# Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.

def lovefunc( flower1:int, flower2:int ):
    return (flower1 % 2) != (flower2 % 2)

#==============================================================================================================

# DESCRIPTION:
# Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

# Input: []
# Output: 0

# Input: [-2.398]
# Output: -2.398

# Assumptions
# You can assume that you are only given numbers.
# You cannot assume the size of the array.
# You can assume that you do get an array and if the array is empty, return 0.
# What We're Testing
# We're testing basic loops and math operations. This is for beginners who are just learning loops and math operations.
# Advanced users may find this extremely easy and can easily write this in one line.

def sum_array(a:list):
    return sum(a)

#==============================================================================================================

# DESCRIPTION:
# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []
# You can assume that all values are integers. Do not mutate the input array/list.

def invert(nums):
    return [-num for num in nums]