# DESCRIPTION:
# The objective is to return all pairs of integers from a given array of integers that have a difference of 2.

# The result array should be sorted in ascending order of values.

# Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter.

# Examples
# [1, 2, 3, 4]  should return [(1, 3), (2, 4)]

# [4, 1, 2, 3]  should also return [(1, 3), (2, 4)]

# [1, 23, 3, 4, 7] should return [(1, 3)]

# [4, 3, 1, 5, 6] should return [(1, 3), (3, 5), (4, 6)]

def twos_difference(nums: list[int]) -> list[tuple[int, int]]: 
    return [(num, num + 2) for num in sorted(nums) if num + 2 in nums]

#==============================================================================================================

# You are given a binary tree:

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
# Your task is to return the list with elements from tree sorted by levels, which means the root element goes first, then root children (from left to right) are second and third, and so on.

# Return empty list if root is None.

# Example 1 - following tree:

#                  2
#             8        9
#           1  3     4   5
# Should return following list:

# [2,8,9,1,3,4,5]
# Example 2 - following tree:

#                  1
#             8        4
#               3        5
#                          7
# Should return following list:

# [1,8,4,3,5,7]

def tree_by_levels(tree: Node) -> list[int]:
    queue, node_list = [tree], []
    
    while queue:
        node = queue.pop(0)
        if node:
            queue += [node.left, node.right]
            node_list.append(node.value)
            
    return node_list