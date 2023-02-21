# Challenge:

# Given a two-dimensional array of integers, return the flattened version of the array with all the integers in the sorted (ascending) order.

# Example
#     Given [[3, 2, 1], [4, 6, 5], [], [9, 7, 8]], your function should return [1, 2, 3, 4, 5, 6, 7, 8, 9]

def flatten_and_sort(array: list[list[int]]) -> list[int]:
    return sorted([val for subarray in array for val in subarray])

#==============================================================================================================

# DESCRIPTION:
# Complete the method which accepts an array of integers, and returns one of the following:

    # "yes, ascending" - if the numbers in the array are sorted in an ascending order
    # "yes, descending" - if the numbers in the array are sorted in a descending order
    # "no" - otherwise
# You can assume the array will always be valid, and there will always be one correct answer.

def is_sorted_and_how(arr):
    ascending, descending = 0,0
    
    for idx in range(1, len(arr)):
        if arr[idx - 1] > arr[idx]:
            descending += 1
        if arr[idx - 1] < arr[idx]:
            ascending += 1

    return 'no' if descending and ascending else 'yes, ascending' if ascending else 'yes, descending'

#==============================================================================================================
