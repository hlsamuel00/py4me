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

#==============================================================================================================

# Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

# Example 1:
#     Input: nums = [2,1,2]
#     Output: 5
#     Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

# Example 2:
#     Input: nums = [1,2,1,10]
#     Output: 0
#     Explanation: 
#     You cannot use the side lengths 1, 1, and 2 to form a triangle.
#     You cannot use the side lengths 1, 1, and 10 to form a triangle.
#     You cannot use the side lengths 1, 2, and 10 to form a triangle.
#     As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.
 

# Constraints:
#     3 <= nums.length <= 104
#     1 <= nums[i] <= 106

class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort(reverse = True)
        for i in range(3, len(nums) + 1):
            if nums[i-3] < nums[i - 2] + nums[i - 1]:
                return sum(nums[i - 3: i])
        return 0