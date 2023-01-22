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

# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row. 

# Example 1:
#     Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
#     Output: 11
#     Explanation: The triangle looks like:
#        2
#       3 4
#      6 5 7
#     4 1 8 3
#     The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

# Example 2:
#     Input: triangle = [[-10]]
#     Output: -10
 
# Constraints:
#     1 <= triangle.length <= 200
#     triangle[0].length == 1
#     triangle[i].length == triangle[i - 1].length + 1
#     -104 <= triangle[i][j] <= 104

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for r_idx in range(1, len(triangle)):  
            for col_idx in range(r_idx + 1):           
                triangle[r_idx][col_idx] += min(triangle[r_idx - 1][col_idx - (col_idx == r_idx)], 
                                                triangle[r_idx - 1][col_idx - (col_idx > 0)])  

        return min(triangle[-1])

#==============================================================================================================

# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

# Example 1:
#     Input: root = [1,null,3,2,4,null,5,6]
#     Output: [1,3,5,6,2,4]

# Example 2:
#     Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
#     Output: [1,2,3,6,7,11,14,4,8,12,5,9,13,10]
 

# Constraints:
#     The number of nodes in the tree is in the range [0, 104].
#     0 <= Node.val <= 104
#     The height of the n-ary tree is less than or equal to 1000.

class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        node_list = []

        def find_children(root):
            if not root: return
            node_list.append(root.val)
            for child in root.children:
                find_children(child)

        find_children(root)
        return node_list 

#==============================================================================================================


# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Example 1:
#     Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
#     Output: [-1,3,-1]
#     Explanation: The next greater element for each value of nums1 is as follows:
#     - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
#     - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
#     - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

# Example 2:
#     Input: nums1 = [2,4], nums2 = [1,2,3,4]
#     Output: [3,-1]
#     Explanation: The next greater element for each value of nums1 is as follows:
#     - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
#     - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
 

# Constraints:
#     1 <= nums1.length <= nums2.length <= 1000
#     0 <= nums1[i], nums2[i] <= 104
#     All integers in nums1 and nums2 are unique.
#     All the integers of nums1 also appear in nums2.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = {}
        
        for num in nums2:
            while(stack and num > stack[-1]):
                ans[stack.pop()] = num
            
            stack.append(num)
        
        return [ans.get(e, -1) for e in nums1]

#==============================================================================================================

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Example 1:
#     Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
#     Output: true

# Example 2:
#     Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
#     Output: false

# Constraints:
#     2 <= coordinates.length <= 1000
#     coordinates[i].length == 2
#     -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
#     coordinates contains no duplicate point.

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[0:2]
        
        for x3, y3 in coordinates[2:]:
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1): return False
        
        return True