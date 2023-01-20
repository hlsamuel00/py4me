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