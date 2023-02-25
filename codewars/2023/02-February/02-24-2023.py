# Given a string s. You have to return another string such that even-indexed and odd-indexed characters of s are grouped and groups are space-separated (see sample below)

# Note: 
# 0 is considered to be an even index. 
# All input strings are valid with no spaces
# input: 'CodeWars'
# output 'CdWr oeas'

# S[0] = 'C'
# S[1] = 'o'
# S[2] = 'd'
# S[3] = 'e'
# S[4] = 'W'
# S[5] = 'a'
# S[6] = 'r'
# S[7] = 's'
# Even indices 0, 2, 4, 6, so we have 'CdWr' as the first group
# odd ones are 1, 3, 5, 7, so the second group is 'oeas'
# And the final string to return is 'Cdwr oeas'

def sort_my_string(s:str) -> str:
    evens, odds = '', ''
    
    for idx in range(len(s)):
        if not idx % 2:
            evens += s[idx]
        else:
            odds += s[idx]
            
    return f'{evens} {odds}'

#==============================================================================================================
# An array is monotonic if it is either monotone increasing or monotone decreasing.

# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
 
# Example 1:
#     Input: nums = [1,2,2,3]
#     Output: true

# Example 2:
#     Input: nums = [6,5,4,4]
#     Output: true

# Example 3:
#     Input: nums = [1,3,2]
#     Output: false
 
# Constraints:
#     1 <= nums.length <= 105
#     -105 <= nums[i] <= 105


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        ascending, descending = 0,0
        for idx in range(1, len(nums)):
            if nums[idx - 1] < nums[idx]:
                ascending += 1
            
            if nums[idx - 1] > nums[idx]:
                descending += 1

        return ascending and not descending or descending and not ascending or not ascending and not descending
    
    # OR

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        monotonic = True

        if nums[-1] <= nums[0]:
            for idx in range(1, len(nums)):
                if nums[idx - 1] < nums[idx]:
                    monotonic = False
                    break

        if nums[-1] >= nums[0]:
            for idx in range(1, len(nums)):
                if nums[idx - 1] > nums[idx]:
                    monotonic = False
                    break
        
        return monotonic

#==============================================================================================================

