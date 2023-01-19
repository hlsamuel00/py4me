# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 
# Example 1:
#     Input: list1 = [1,2,4], list2 = [1,3,4]
#     Output: [1,1,2,3,4,4]

# Example 2:
#     Input: list1 = [], list2 = []
#     Output: []

# Example 3:
#     Input: list1 = [], list2 = [0]
#     Output: [0]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1: return list2
        if not list2: return list1

        if list1.val <= list2.val:
            newList = ListNode(list1.val)
            newList.next = self.mergeTwoLists(list1.next, list2)
            return newList
        else:
            newList = ListNode(list2.val)
            newList.next = self.mergeTwoLists(list2.next, list1)

        return newList

#==============================================================================================================

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
#     Input: head = [1,2,3,4,5]
#     Output: [5,4,3,2,1]

# Example 2:
#     Input: head = [1,2]
#     Output: [2,1]

# Example 3:
#     Input: head = []
#     Output: []

# Constraints:
#     The number of nodes in the list is the range [0, 5000].
#     -5000 <= Node.val <= 5000

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        newNode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return newNode