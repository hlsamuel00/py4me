# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
    # Input: s = ["h","e","l","l","o"]
    # Output: ["o","l","l","e","h"]

# Example 2:
    # Input: s = ["H","a","n","n","a","h"]
    # Output: ["h","a","n","n","a","H"]
 

# Constraints:
    # 1 <= s.length <= 105
    # s[i] is a printable ascii character.

class Solution:
    def reverseString(self, s: List[str]) -> None:
       s[:] = s[::-1]

# OR

class Solution:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()

# OR

from math import ceil
class Solution:
    def reverseString(self, s: list[str]) -> None:
        mid = ceil(len(s) / 2)
        for idx in range(mid):
            end = -(idx + 1)
            s[idx],s[end] = s[end],s[idx]

# OR

from math import ceil
class Solution:
    def reverseString(self, s: list[str]) -> None:
        start, mid = 0, ceil(len(s) / 2)
        while start < mid:
            end = -(start + 1)
            s[start],s[end] = s[end],s[start]
            start += 1


#==============================================================================================================

