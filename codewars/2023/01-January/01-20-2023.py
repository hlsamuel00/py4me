# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# Example 1:
#     Input: n = 4, k = 2
#     Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
#     Explanation: There are 4 choose 2 = 6 total combinations.
#     Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:
#     Input: n = 1, k = 1
#     Output: [[1]]
#     Explanation: There is 1 choose 1 = 1 total combination.
 

# Constraints:
#     1 <= n <= 20
#     1 <= k <= n

from itertools import combinations

class Solution:
    def combine(self, n, k):
        return list(combinations(range(1,n+1), k))

#==============================================================================================================

# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

# Example 1:
#     Input: nums = [1,2,3]
#     Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
#     Input: nums = [0,1]
#     Output: [[0,1],[1,0]]

# Example 3:
#     Input: nums = [1]
#     Output: [[1]]
 

# Constraints:
#     1 <= nums.length <= 6
#     -10 <= nums[i] <= 10
#     All the integers of nums are unique.

from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        return list(permutations(nums))

#==============================================================================================================

# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

# Example 1:
#     Input: s = "a1b2"
#     Output: ["a1b2","a1B2","A1b2","A1B2"]

# Example 2:
#     Input: s = "3z4"
#     Output: ["3z4","3Z4"]
 

# Constraints:
#     1 <= s.length <= 12
#     s consists of lowercase English letters, uppercase English letters, and digits.

class Solution:
    def letterCasePermutation(self, s:str) -> list[str]:
        
        def casePermute(string:str, idx = 0):
            if len(string) == len(s):
                ans.append(string)
            else:
                if s[idx].isalpha():
                    casePermute(string + s[idx].swapcase(), idx + 1)
                casePermute(string + s[idx], idx + 1)
            
        ans = []
        casePermute()
        return ans

#==============================================================================================================

# There is a function signFunc(x) that returns:

# 1 if x is positive.
# -1 if x is negative.
# 0 if x is equal to 0.

# You are given an integer array nums. Let product be the product of all values in the array nums.

# Return signFunc(product). 

# Example 1:
#     Input: nums = [-1,-2,-3,-4,3,2,1]
#     Output: 1
#     Explanation: The product of all values in the array is 144, and signFunc(144) = 1

# Example 2:
#     Input: nums = [1,5,0,2,-3]
#     Output: 0
#     Explanation: The product of all values in the array is 0, and signFunc(0) = 0

# Example 3:
#     Input: nums = [-1,1,-1,1,-1]
#     Output: -1
#     Explanation: The product of all values in the array is -1, and signFunc(-1) = -1

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        
        signFunc = lambda x: (x > 0) - (x < 0)
    
        return signFunc(product)

# OR

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        ans = 1
        for num in nums:
            if not num: return 0
            if num < 0: ans *= -1
        
        return ans

#==============================================================================================================

# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

# Example 1:
#     Input: arr = [3,5,1]
#     Output: true
#     Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

# Example 2:
#     Input: arr = [1,2,4]
#     Output: false
#     Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
 

# Constraints:
#     2 <= arr.length <= 1000
#     -106 <= arr[i] <= 106

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = abs(arr[0] - arr[1])
        for idx in range(len(arr)-1):
            if arr[idx + 1] - arr[idx] != d: return False
        
        return True

#==============================================================================================================