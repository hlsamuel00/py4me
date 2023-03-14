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