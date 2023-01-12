# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

#     Input: nums = [0,1,0,3,12]
#     Output: [1,3,12,0,0]
#     Example 2:

#     Input: nums = [0]
#     Output: [0]

# Constraints:

#     1 <= nums.length <= 104
#     -231 <= nums[i] <= 231 - 1

# Follow up: Could you minimize the total number of operations done?

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        nums[:] = [num for num in nums if num] + [0] * nums.count(0)

# OR

class Solution:
    def moveZeroes(self, nums: list[int]):
        slower_idx = 0
        for idx in range(len(nums)):
            if nums[idx]:
                nums[slower_idx], nums[idx] = nums[idx], nums[slower_idx]
                slower_idx += 1

#==============================================================================================================

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

# Example 1:
#     Input: numbers = [2,7,11,15], target = 9
#     Output: [1,2]
#     Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
#     Input: numbers = [2,3,4], target = 6
#     Output: [1,3]
#     Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
#     Input: numbers = [-1,0], target = -1
#     Output: [1,2]
#     Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

# Constraints:
#     2 <= numbers.length <= 3 * 104
#     -1000 <= numbers[i] <= 1000
#     numbers is sorted in non-decreasing order.
#     -1000 <= target <= 1000
#     The tests are generated such that there is exactly one solution.

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for (idx, num) in enumerate(numbers):
            if target - num in numbers[idx + 1:]:
                return [idx + 1, numbers[idx + 1:].index(target - num) + (len(numbers[: idx + 1]) + 1) ]

# OR

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        front = 0
        back = len(numbers) - 1
        
        while numbers[front] + numbers[back] != target:
            sum = numbers[front] + numbers[back]        
            if sum > target: back -= 1
            else: front += 1 
    
        return [front + 1 , back + 1]