# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:
#     Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#     Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
#     Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#     Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
# Constraints:
#     n == matrix.length == matrix[i].length
#     1 <= n <= 20
#     -1000 <= matrix[i][j] <= 1000

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        dummy_matrix = matrix[:]

        for r_idx in range(len(matrix)):
            new_row = []

            for c_idx in range(len(matrix[0])):
                new_row.append(dummy_matrix[(len(matrix[0]) - 1) - c_idx][r_idx])
            
            matrix[r_idx] = new_row

#==============================================================================================================

# Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.

# Example 1:
#     Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
#     Output: true
#     Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

# Example 2:
#     Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
#     Output: false
#     Explanation: It is impossible to make mat equal to target by rotating mat.

# Example 3:
#     Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
#     Output: true
#     Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

# Constraints:
#     n == mat.length == target.length
#     n == mat[i].length == target[i].length
#     1 <= n <= 10
#     mat[i][j] and target[i][j] are either 0 or 1.

class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for _ in range(4):
            self.rotate(mat)
            if mat == target: return True
        
        return False
    
    def rotate(self, mat: list[list[int]]) -> None:
        temp_mat = mat[:]

        for r_idx in range(len(mat)):
            new_row = []
            for c_idx in range(len(mat[0])):
                new_row.append(temp_mat[(len(mat[0]) - 1) - c_idx][r_idx])

            mat[r_idx] = new_row