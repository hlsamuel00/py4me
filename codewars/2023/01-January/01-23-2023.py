# Reverse bits of a given 32 bits unsigned integer.

# Note:
#     Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
    
#     In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.
 
# Example 1:
#     Input: n = 00000010100101000001111010011100
#     Output:    964176192 (00111001011110000010100101000000)
#     Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Example 2:
#     Input: n = 11111111111111111111111111111101
#     Output:   3221225471 (10111111111111111111111111111111)
#     Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
 
# Constraints:
#     The input must be a binary string of length 32

# Follow up: 
#     If this function is called many times, how would you optimize it?

class Solution:
    def reverseBits(self, n: int) -> int:
        return int(''.join(list(bin(n).replace('0b','').rjust(32,'0'))[::-1]), 2)

#==============================================================================================================

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
#     Input: nums = [2,2,1]
#     Output: 1

# Example 2:
#     Input: nums = [4,1,2,1,2]
#     Output: 4

# Example 3:
#     Input: nums = [1]
#     Output: 1
 
# Constraints:
#     1 <= nums.length <= 3 * 104
#     -3 * 104 <= nums[i] <= 3 * 104
#     Each element in the array appears twice except for one element which appears only once.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        back = -1
        for idx in range(len(nums)):
            if nums.count(nums[idx]) == 1: return nums[idx]
            if nums.count(nums[back]) == 1: return nums[back]
            back -= 1

# OR

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        answer = 0
        
        for num in nums:
            answer ^= num
        
        return answer

#==============================================================================================================

# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

# Example 1:
#     Input: mat = [[1,2,3],
#                 [4,5,6],
#                 [7,8,9]]
#     Output: 25
#     Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
#     Notice that element mat[1][1] = 5 is counted only once.

# Example 2:
#     Input: mat = [[1,1,1,1],
#                 [1,1,1,1],
#                 [1,1,1,1],
#                 [1,1,1,1]]
#     Output: 8

# Example 3:
#     Input: mat = [[5]]
#     Output: 5
 
# Constraints:
#     n == mat.length == mat[i].length
#     1 <= n <= 100
#     1 <= mat[i][j] <= 100


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total, back, middle = 0, -1, len(mat) // 2
        
        for front in range(len(mat)):
            total += mat[front][front] + mat[front][back]
            back -= 1
        
        if len(mat) % 2: total -= mat[middle][middle]
        
        return total

#==============================================================================================================

