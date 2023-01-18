# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

# Example 1:
#     Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
#     Output: [[0,0,0],[0,1,0],[0,0,0]]

# Example 2:
#     Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
#     Output: [[0,0,0],[0,1,0],[1,2,1]]
 

# Constraints:
#     m == mat.length
#     n == mat[i].length
#     1 <= m, n <= 104
#     1 <= m * n <= 104
#     mat[i][j] is either 0 or 1.
#     There is at least one 0 in mat.


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        for r_idx in range(len(mat)):
            for c_idx in range(len(mat[0])):
                if mat[r_idx][c_idx]!=0:
                    top = mat[r_idx - 1][c_idx] if r_idx > 0 else float('inf')
                    left = mat[r_idx][c_idx - 1] if c_idx > 0 else float('inf')
                    mat[r_idx][c_idx] = min(top,left) + 1
        
        for r_idx in range(len(mat) - 1, -1, -1):
            for c_idx in range(len(mat[0]) - 1, -1, -1):
                if mat[r_idx][c_idx]!=0:
                    down = mat[r_idx + 1][c_idx] if r_idx < len(mat) - 1 else float('inf')
                    right = mat[r_idx][c_idx + 1] if c_idx < len(mat[0]) - 1 else float('inf')
                    mat[r_idx][c_idx] = min(mat[r_idx][c_idx], min(down,right) + 1)
        
        return mat  

#=============================================================================================================

      