# Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

# Return the decimal value of the number in the linked list.

# The most significant bit is at the head of the linked list.

# Example 1:
#     Input: head = [1,0,1]
#     Output: 5
#     Explanation: (101) in base 2 = (5) in base 10

# Example 2:
#     Input: head = [0]
#     Output: 0
 
# Constraints:
#     The Linked List is not empty.
#     Number of nodes will not exceed 30.
#     Each node's value is either 0 or 1.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = []
        def getValue(node):
            if not node: 
                return
            else:
                binary.append(str(node.val))
                getValue(node.next)
        
        getValue(head)
        return int(''.join(binary), 2)

# OR

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = ''

        while head:
            binary += str(head.val)
            head = head.next
        
        return int(binary, 2)

#==============================================================================================================

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:
#     Input: head = [1,2,3,4,5]
#     Output: [3,4,5]
#     Explanation: The middle node of the list is node 3.

# Example 2:
#     Input: head = [1,2,3,4,5,6]
#     Output: [4,5,6]
#     Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
# Constraints:
#     The number of nodes in the list is in the range [1, 100].
#     1 <= Node.val <= 100

class Solution:
    def middleNode(self, head: ListNode):
        if not head and not head.next: return head

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

#==============================================================================================================

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
#     Input: root = [3,9,20,null,null,15,7]
#     Output: 3

# Example 2:
#     Input: root = [1,null,2]
#     Output: 2

# Constraints:
#     The number of nodes in the tree is in the range [0, 104].
#     -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

#==============================================================================================================

# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

# Example 1:
#     Input: root = [3,9,20,null,null,15,7]
#     Output: 24
#     Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

# Example 2:
#     Input: root = [1]
#     Output: 0
 
# Constraints:
#     The number of nodes in the tree is in the range [1, 1000].
#     -1000 <= Node.val <= 1000

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        if root.left and not root.left.left and not root.left.right: 
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)