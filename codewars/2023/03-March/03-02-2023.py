# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:
#     Input: temperatures = [73,74,75,71,69,72,76,73]
#     Output: [1,1,4,2,1,1,0,0]

# Example 2:
#     Input: temperatures = [30,40,50,60]
#     Output: [1,1,1,0]

# Example 3:
#     Input: temperatures = [30,60,90]
#     Output: [1,1,0]

# Constraints:
#     1 <= temperatures.length <= 105
#     30 <= temperatures[i] <= 100

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack, result = [0], [0] * len(temperatures)
        for idx in range(len(temperatures)):
            while len(stack) and temperatures[idx] > temperatures[stack[-1]]:
                result[stack[-1]] = idx - stack[-1]
                stack.pop()
            stack.append(idx)

        return result

#==============================================================================================================

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

from re import findall
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(findall('\w+', s)[-1])
    
# OR

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for idx in range(-1, -(len(s) + 1), -1):
            if s[idx] == ' ':
                if count:
                    return count
                continue
            count += 1

        return count