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

# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

# Example 1:
    # Input: s = "Let's take LeetCode contest"
    # Output: "s'teL ekat edoCteeL tsetnoc"

# Example 2:
    # Input: s = "God Ding"
    # Output: "doG gniD"
 

# Constraints:
    # 1 <= s.length <= 5 * 104
    # s contains printable ASCII characters.
    # s does not contain any leading or trailing spaces.
    # There is at least one word in s.
    # All the words in s are separated by a single space.

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda x: x[::-1],s.split(' ')))

# OR

class Solution:
    def reverseWords(self, s:str) -> str:
        return ' '.join([word[::-1] for word in str.split(' ')])