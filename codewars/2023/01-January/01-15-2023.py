# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
#     Input: s = "abcabcbb"
#     Output: 3
#     Explanation: The answer is "abc", with the length of 3.

# Example 2:
#     Input: s = "bbbbb"
#     Output: 1
#     Explanation: The answer is "b", with the length of 1.

# Example 3:
#     Input: s = "pwwkew"
#     Output: 3
#     Explanation: The answer is "wke", with the length of 3.

# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:
#     0 <= s.length <= 5 * 104
#     s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr, max_count = '', 0
        for char in s:
            if char not in substr:
                substr += char
            else:
                substr = substr[substr.index(char) + 1:] + char
            
            if max_count < len(substr): max_count = len(substr)
        
        return max_count

#==============================================================================================================

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
#     Input: s1 = "ab", s2 = "eidbaooo"
#     Output: true
#     Explanation: s2 contains one permutation of s1 ("ba").

# Example 2:
#     Input: s1 = "ab", s2 = "eidboaoo"
#     Output: false
 

# Constraints:
#     1 <= s1.length, s2.length <= 104
#     s1 and s2 consist of lowercase English letters.


from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1) # setting the window to the length of the test string
        s1_counter = Counter(s1) # create a count of all letters in the test string
        
        for i in range(len(s2) - window + 1): # creating boundaries so check remains within length of string
            if s1_counter == Counter(s2[i : i + window]): # creating a new count of all of the letters in the string and testing count of letters in string with the letter count in test string
                return True # return true if they match
            
        return False # if loop wasn't broken, no permutation exists