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

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1. 

# Example 1:
#     Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
#     Output: 4

# Example 2:
#     Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
#     Output: -1
#     Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
#     Input: grid = [[0,2]]
#     Output: 0
#     Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# Constraints:
#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 10
#     grid[i][j] is 0, 1, or 2.

def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        
        while fresh:
            if not rotting: return -1
            rotting = {(i + di, j + dj) for (i, j) in rotting for (di, dj) in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i + di, j + dj) in fresh}
            fresh -= rotting
            timer += 1
        
        return timer

#==============================================================================================================

# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Note: Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
 
# Example 1:
#     Input: n = 00000000000000000000000000001011
#     Output: 3
#     Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# Example 2:
#     Input: n = 00000000000000000000000010000000
#     Output: 1
#     Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

# Example 3:
#     Input: n = 11111111111111111111111111111101
#     Output: 31
#     Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(1 for _ in bin(n).replace('0b', '') if int(_))

#==============================================================================================================

