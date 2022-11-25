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
