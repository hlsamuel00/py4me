# Given a binary tree root and a linked list with head as the first node. 

# Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

# In this context downward path means a path that starts at some node and goes downwards.

# Example 1:
#     Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
#     Output: true
#     Explanation: Nodes in blue form a subpath in the binary Tree.  

# Example 2:
#     Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
#     Output: true

# Example 3:
#     Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
#     Output: false
#     Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
 
# Constraints:
#     The number of nodes in the tree will be in the range [1, 2500].
#     The number of nodes in the list will be in the range [1, 100].
#     1 <= Node.val <= 100 for each node in the linked list and binary tree.


from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def search(h: ListNode, r: TreeNode):
            if not h: return True
            if not r: return False
            return r.val == h.val and (search(h.next, r.left) or search(h.next, r.right))
        
        if not head: return True
        if not root: return False
        return search(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    

#==============================================================================================================


# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:
#     Input: num1 = "2", num2 = "3"
#     Output: "6"

# Example 2:
#     Input: num1 = "123", num2 = "456"
#     Output: "56088"
    
# Constraints:
#     1 <= num1.length, num2.length <= 200
#     num1 and num2 consist of digits only.
#     Both num1 and num2 do not contain any leading zero, except the number 0 itself.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1) * int(num2))