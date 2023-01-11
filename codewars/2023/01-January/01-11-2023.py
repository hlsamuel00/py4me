# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(map(lambda x: x ** 2, nums))

#==============================================================================================================

