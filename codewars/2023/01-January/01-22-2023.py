# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:
#     Input: n = 1
#     Output: true
#     Explanation: 20 = 1

# Example 2:
#     Input: n = 16
#     Output: true
#     Explanation: 24 = 16

# Example 3:
#     Input: n = 3
#     Output: false

# Constraints:
#     -231 <= n <= 231 - 1

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

#==============================================================================================================

# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Note:
#     Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
#     In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

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
 

# Constraints:
#     The input must be a binary string of length 32.

# Follow up: If this function is called many times, how would you optimize it?

class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(1 for _ in bin(n).replace('0b', '') if int(_))

# OR

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

#==============================================================================================================

# Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.

# A subarray is a contiguous subsequence of the array.

# Example 1:
#     Input: arr = [1,4,2,5,3]
#     Output: 58
#     Explanation: The odd-length subarrays of arr and their sums are:
#     [1] = 1
#     [4] = 4
#     [2] = 2
#     [5] = 5
#     [3] = 3
#     [1,4,2] = 7
#     [4,2,5] = 11
#     [2,5,3] = 10
#     [1,4,2,5,3] = 15
#     If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

# Example 2:
#     Input: arr = [1,2]
#     Output: 3
#     Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

# Example 3:
#     Input: arr = [10,11,12]
#     Output: 66
    
# Constraints:
#     1 <= arr.length <= 100
#     1 <= arr[i] <= 1000

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total, frequency, length = 0, 0, len(arr)
        
        for idx in range(length):
            frequency = frequency - (idx + 1) // 2 + (length - idx + 1 ) // 2
            total += frequency * arr[idx]
        
        return total

#==============================================================================================================

