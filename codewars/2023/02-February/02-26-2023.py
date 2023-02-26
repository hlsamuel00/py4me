# Given a binary tree, determine if it is 
# height-balanced

# Example 1:
#     Input: root = [3,9,20,null,null,15,7]
#     Output: true

# Example 2:
#     Input: root = [1,2,2,3,3,null,null,4,4]
#     Output: false

# Example 3:
#     Input: root = []
#     Output: true
 
# Constraints:
#     The number of nodes in the tree is in the range [0, 5000].
#     -104 <= Node.val <= 104



# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: return True

        left = self.height(root.left)
        right = self.height(root.right)

        if(abs(left - right) <= 1) and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        
        return False

    def height(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(self.height(root.right), self.height(root.left)) + 1
    

# OR

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True

        left = self.isBalanced(root.left)
        if not left:
            return False
        
        right = self.isBalanced(root.right)
        if not right:
            return False

        if abs(left - right) > 1:
            return False
        else:
            return 1 + max(left, right)
    
#==============================================================================================================

# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# Example 1:
#     Input: s = "abab"
#     Output: true
#     Explanation: It is the substring "ab" twice.

# Example 2:
#     Input: s = "aba"
#     Output: false

# Example 3:
#     Input: s = "abcabcabcabc"
#     Output: true
#     Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 
# Constraints:
#     1 <= s.length <= 104
#     s consists of lowercase English letters.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]