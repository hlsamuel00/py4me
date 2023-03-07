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

# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Example 1:
#     Input: points = [[1,3],[-2,2]], k = 1
#     Output: [[-2,2]]
#     Explanation:
#         The distance between (1, 3) and the origin is sqrt(10).
#         The distance between (-2, 2) and the origin is sqrt(8).
#         Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
#         We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2:
#     Input: points = [[3,3],[5,-1],[-2,4]], k = 2
#     Output: [[3,3],[-2,4]]
#     Explanation: The answer [[-2,4],[3,3]] would also be accepted.
    

# Constraints:
#     1 <= k <= points.length <= 104
#     -104 < xi, yi < 104

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        def find_distance(point: list[int]) -> float:
            x, y = point
            return (x ** 2 + y ** 2) ** .5
        
        return sorted(points, key = find_distance)[:k]

# OR 

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        return sorted(points, key = lambda point: point[0] ** 2 + point[1] ** 2)[:k]