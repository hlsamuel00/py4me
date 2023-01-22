# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
#     Input: n = 2
#     Output: 2
#     Explanation: There are two ways to climb to the top.
#         1. 1 step + 1 step
#         2. 2 steps

# Example 2:
#     Input: n = 3
#     Output: 3
#     Explanation: There are three ways to climb to the top.
#         1. 1 step + 1 step + 1 step
#         2. 1 step + 2 steps
#         3. 2 steps + 1 step
 
# Constraints:
# 1 <= n <= 45

class Solution:
    def climbStairs(self, n: int) -> int:
        solutions = {}

        def climb(num):
            if num < 3: return num
            elif num in solutions: return solutions[num]
            else:
                answer = climb(num - 1) + climb(num - 2)
                solutions[num] = answer
                return answer
        
        return climb(n)

#==============================================================================================================

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

# Example 1:
#     Input: nums = [1,2,3,1]
#     Output: 4
#     Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#     Total amount you can rob = 1 + 3 = 4.

# Example 2:
#     Input: nums = [2,7,9,3,1]
#     Output: 12
#     Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#     Total amount you can rob = 2 + 9 + 1 = 12.
 
# Constraints:
#     1 <= nums.length <= 100
#     0 <= nums[i] <= 400


class Solution:
    def rob(self, nums: list[int]) -> int:

        if len(nums) <= 2: return max(nums)

        robbed = [0] * (len(nums)+1)
        robbed[1] = nums[0]

        for n in range(1,len(nums)):
            robbed[n+1] = max(robbed[n], nums[n] + robbed[n-1])
    
        return robbed[-1]  

#==============================================================================================================