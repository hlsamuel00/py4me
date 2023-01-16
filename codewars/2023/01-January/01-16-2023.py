# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.


# Example 1:
#     Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
#     Output: [[2,2,2],[2,2,0],[2,0,1]]
#     Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
#     Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

# Example 2:
#     Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
#     Output: [[0,0,0],[0,0,0]]
#     Explanation: The starting pixel is already colored 0, so no changes are made to the image.
 
# Constraints:
#     m == image.length
#     n == image[i].length
#     1 <= m, n <= 50
#     0 <= image[i][j], color < 216
#     0 <= sr < m
#     0 <= sc < n

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]

        def fill(row, column):
            # ensure that the row and column are within the bounds of the image size
            if row < 0 or row >= len(image) or column < 0 or column >= len(image[0]): return None

            # ensure that the current color isnt already the target color is different from starting color
            if image[row][column] == color or image[row][column] != starting_color : return None

            # set target pixel to color
            image[row][column] = color

            # after conditionals, run for 4 directions
            fill(row - 1, column)
            fill(row + 1, column)
            fill(row, column - 1)
            fill(row, column + 1)

        fill(sr,sc)
        return image

#==============================================================================================================

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Example 1:
#     Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#     Output: 6
#     Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:
#     Input: grid = [[0,0,0,0,0,0,0,0]]
#     Output: 0
 

# Constraints:
#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 50
#     grid[i][j] is either 0 or 1.


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        maxArea = 0

        # verifiy if location is land
        def is_land(row, column):
            # ensure that location is within bounds of the grid
            if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]): return False

            # ensure that location is indeed land
            if not grid[row][column]: return False

            # if we've made it this far, location is indeed land
            return True

        # calculate area of land found
        def calc_area(row, column):
            # determine if location is land
            if not is_land(row,column): return 0

            grid[row][column] = 0
            #determine surrounding if areas are land
            up, down, left, right = calc_area(row - 1, column), calc_area(row + 1, column), calc_area(row, column - 1), calc_area(row, column + 1)

            # return total count of area
            return up + down + left + right + 1


        # run for loop through the grid for each point
        for r_idx in range(len(grid)):
            for c_idx in range(len(grid[r_idx])):
                area = calc_area(r_idx,c_idx)
                if area > maxArea: maxArea = area
        
        return maxArea