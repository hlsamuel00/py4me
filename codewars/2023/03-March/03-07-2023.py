# DESCRIPTION:
# Sort the given array of strings in alphabetical order, case insensitive. For example:

# ["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
# ["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]

def sortme(words: list[str]) -> list[str]:
    return sorted(words, key = str.lower)

#==============================================================================================================

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
#     Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#     Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
#     Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#     Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:
#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 10
#     -100 <= matrix[i][j] <= 100

class Solution(object):
    def spiralOrder(self, matrix:list[list[int]]):
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        result = []

        while left <= right and top <= bottom:
            
            for ltr in range(left, right + 1):
                result.append(matrix[top][ltr])
            top += 1

            for ttb in range(top, bottom + 1):
                result.append(matrix[ttb][right])
            right -= 1

            if top <= bottom:
                for rtl in range(right, left -1, -1):
                    result.append(matrix[bottom][rtl])
                bottom -= 1

            if left <= right:
                for btt in range(bottom, top - 1, -1):
                    result.append(matrix[btt][left])
                left += 1

        return result

#==============================================================================================================

