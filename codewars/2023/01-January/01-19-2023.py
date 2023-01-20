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

#==============================================================================================================

# You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y). You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi). A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

# Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location. If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

# The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2). 

# Example 1:
#     Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
#     Output: 2
#     Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.

# Example 2:
#     Input: x = 3, y = 4, points = [[3,4]]
#     Output: 0
#     Explanation: The answer is allowed to be on the same location as your current location.

# Example 3:
#     Input: x = 3, y = 4, points = [[2,3]]
#     Output: -1
#     Explanation: There are no valid points.
 

# Constraints:
#     1 <= points.length <= 104
#     points[i].length == 2
#     1 <= x, y, ai, bi <= 104

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # set min distance to largest int possible and index to -1 to return without changes
        min_distance, index = float('inf'), -1

        # Loop through list of points and grab the index and the points
        for (idx, [a, b]) in enumerate(points):
            # check if the point is 'valid' (x1 == x2 or y1 == y2)
            if a == x or b == y:
                # calculate the distance
                distance = abs(a - x) + abs(b - y)
                # check if the distance calculated is lower than our minimum distance so far
                if distance < min_distance:
                    # if true, update min distance to the distance calculated and update the index 
                    min_distance = distance
                    index = idx
        
        # return the index (either index gathered in loop or -1 if none was true)
        return index

        