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

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


# Example 1:
#     Input: n = 19
#     Output: true
#     Explanation:
#         12 + 92 = 82
#         82 + 22 = 68
#         62 + 82 = 100
#         12 + 02 + 02 = 1

# Example 2:
#     Input: n = 2
#     Output: false
 
# Constraints:
#     1 <= n <= 231 - 1

class Solution:
    def isHappy(self, n: int) -> bool:
        set_of_nums = set()
        while n != 1:
            n = sum([int(digit)**2 for digit in list(str(n))])
            if n in set_of_nums: return False
            set_of_nums.add(n)

        return True

#==============================================================================================================

# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

# Example 1:
#     Input: s1 = "bank", s2 = "kanb"
#     Output: true
#     Explanation: For example, swap the first character with the last character of s2 to make "bank".

# Example 2:
#     Input: s1 = "attack", s2 = "defend"
#     Output: false
#     Explanation: It is impossible to make them equal with one string swap.

# Example 3:
#     Input: s1 = "kelb", s2 = "kelb"
#     Output: true
#     Explanation: The two strings are already equal, so no string swap operation is required.
 

# Constraints:
#     1 <= s1.length, s2.length <= 100
#     s1.length == s2.length
#     s1 and s2 consist of only lowercase English letters.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
            if s1 == s2: return True 
            if sorted(s1) != sorted(s2): return False 
            
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]: count +=1  
            
            return count <= 2
