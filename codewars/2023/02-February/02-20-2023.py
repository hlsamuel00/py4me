# Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1

# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

# we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
# In other words:

# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

# If it is the case we will return k, if not return -1.

# Note: n and p will always be given as strictly positive integers.
#     dig_pow(89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
#     dig_pow(92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
#     dig_pow(695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
#     dig_pow(46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

def dig_pow(num: int, power: int) -> int:
    total = 0
    for idx in range(len(str(num))):
        total += int(str(num)[idx])**(idx + power)
        
    total /= num
    return total if total.is_integer() else -1

# OR

def dig_pow(num: int, power: int) -> int:
    total = sum(int(str(num)[idx]) ** (idx + power) for idx in range(len(str(num)))) / num
    return total if total.is_integer() else -1


#==============================================================================================================

# Task
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array: list[int]) -> list[int]:
    odds = sorted([num for num in source_array if num % 2])
    return [odds.pop(0) if num % 2 else num for num in source_array]

#==============================================================================================================


# DESCRIPTION:
# You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.

# The returned value must be a string, and have "***" between each of its letters.

# You should not remove or add elements from/to the array.

def two_sort(array):
    return '***'.join(list(sorted(array)[0]))

# OR

def two_sort(array: list[str]) -> str:
    return '***'.join(min(array))

#=============================================================================================================

# DESCRIPTION:
# Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.

# For example, if this array were passed as an argument:

# ["Telescopes", "Glasses", "Eyes", "Monocles"]

# Your function would return the following array:

# ["Eyes", "Glasses", "Monocles", "Telescopes"]

# All of the strings in the array passed to your function will be different lengths, so you will not have to decide how to order multiple strings of the same length.

def sort_by_length(arr):
    return sorted(arr, key = len)

#==============================================================================================================
