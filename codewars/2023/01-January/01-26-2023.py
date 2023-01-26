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