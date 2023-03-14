# DESCRIPTION:
# HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of order! Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.

# The sorting should NOT be case sensitive

def sorter(textbooks: list[str]) -> list[str]:
    return sorted(textbooks, key = str.lower)

#==============================================================================================================

# DESCRIPTION:
# Simple enough this one - you will be given an array. The values in the array will either be numbers or strings, or a mix of both. You will not get an empty array, nor a sparse one.

# Your job is to return a single array that has first the numbers sorted in ascending order, followed by the strings sorted in alphabetic order. The values must maintain their original type.

# Note that numbers written as strings are strings and must be sorted with the other strings.

def db_sort(arr: list) -> list:
    nums = [num for num in arr if type(num) is int]
    strings = [string for string in arr if type(string) is str]
    return sorted(nums) + sorted(strings)

# OR

def db_sort(arr: list) -> list:
    return sorted(arr, key = lambda item: (isinstance(item, str), item))


#==============================================================================================================

# In this kata, you will sort elements in an array by decreasing frequency of elements. If two elements have the same frequency, sort them by increasing value.

# solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
# -- We sort by highest frequency to lowest frequency.
# -- If two elements have same frequency, we sort by increasing value.
# More examples in test cases.

# Good luck!

def solve(arr: list[int]) -> list[int]:
    return sorted(arr, key = lambda num : (-arr.count(num), num))


#==============================================================================================================

# There's a waiting room with N chairs set in single row. Chairs are consecutively numbered from 1 to N. First is closest to the entrance (which is exit as well).

# For some reason people choose a chair in the following way

# Find a place as far from other people as possible
# Find a place as close to exit as possible
# All chairs must be occupied before the first person will be served

# So it looks like this for 10 chairs and 10 patients

# Chairs	1	2	3	4	5	6	7	8	9	10
# Patients	1	7	5	8	3	9	4	6	10	2
# Your task is to find last patient's chair's number.

# Input: number of chairs N, an integer greater than 2.
# Output: a positive integer, the last patient's chair number.
# Have fun :)

def last_chair(n):
    # the patter emerges that the last seat filled will always be the next from the end
    return n - 1