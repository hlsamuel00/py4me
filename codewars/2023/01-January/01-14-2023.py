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

from math import ceil
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my_list = []
        while head:
            my_list.append(head)
            head = head.next
        
        return my_list[ceil((len(my_list) - 1) / 2)]


# OR

class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

#==============================================================================================================


# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Example 1:
#     Input: head = [1,2,3,4,5], n = 2
#     Output: [1,2,3,5]

# Example 2:
#     Input: head = [1], n = 1
#     Output: []

# Example 3:
#     Input: head = [1,2], n = 1
#     Output: [1]
 
# Constraints:
#     The number of nodes in the list is sz.
#     1 <= sz <= 30
#     0 <= Node.val <= 100
#     1 <= n <= sz

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        
        return head