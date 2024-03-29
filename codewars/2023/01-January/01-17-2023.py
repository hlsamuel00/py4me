# You are given two binary trees root1 and root2.

# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

# Return the merged tree.

# Note: The merging process must start from the root nodes of both trees.

# Example 1:
#     Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
#     Output: [3,4,5,5,4,null,7]

# Example 2:
#     Input: root1 = [1], root2 = [1,2]
#     Output: [2,2]

# Constraints:
#     The number of nodes in both trees is in the range [0, 2000].
#     -104 <= Node.val <= 104

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # check to see if there are two roots, if not, return the other
        if not root1: return root2
        if not root2: return root1

        # if no kickback, we can then create a new tree and set the appropriate values
        newTree = TreeNode(root1.val + root2.val)
        newTree.left = self.mergeTrees(root1.left, root2.left)
        newTree.right = self.mergeTrees(root1.right, root2.right)

        return newTree

#==============================================================================================================

# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

# Node structure {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }

# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

# Initially, all next pointers are set to NULL.

# Example 1:
#     Input: root = [1,2,3,4,5,6,7]
#     Output: [1,#,2,3,#,4,5,6,7,#]
#     Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

# Example 2:
#     Input: root = []
#     Output: []
 
# Constraints:
#     The number of nodes in the tree is in the range [0, 212 - 1].
#     -1000 <= Node.val <= 1000
 
# Follow-up:
#     You may only use constant extra space.
#     The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

#Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def set_right(node, right_node):
            if not node: return
            if right_node: node.next = right_node

            set_right(node.left, node.right)
            set_right(node.right, right_node.left if right_node else right_node)
        
        set_right(root, None)
        return root


#==============================================================================================================

# Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

# Example 1:
#     Input: low = 3, high = 7
#     Output: 3
#     Explanation: The odd numbers between 3 and 7 are [3,5,7].

# Example 2:
#     Input: low = 8, high = 10
#     Output: 1
#     Explanation: The odd numbers between 8 and 10 are [9].
 
# Constraints:
#     0 <= low <= high <= 10^9

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        additional_odd = 1 if low % 2 or high % 2 else 0
        return ((high - low) // 2) + additional_odd

#==============================================================================================================

# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
#     Input: salary = [4000,3000,1000,2000]
#     Output: 2500.00000
#     Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively. Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

# Example 2:
#     Input: salary = [1000,2000,3000]
#     Output: 2000.00000
#     Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively. Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
 

# Constraints:
#     3 <= salary.length <= 100
#     1000 <= salary[i] <= 106
#     All the integers of salary are unique.

class Solution:
    def average(self, salary: List[int]) -> float:
        median_salaries = sorted(salary)[1:-1]
        return sum(median_salaries) / len(median_salaries)