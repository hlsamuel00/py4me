# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

# Example 1:
#     Input: s = "Hello"
#     Output: "hello"

# Example 2:
#     Input: s = "here"
#     Output: "here"

# Example 3:
#     Input: s = "LOVELY"
#     Output: "lovely"
 
# Constraints:
#     1 <= s.length <= 100
#     s consists of printable ASCII characters.

class Solution:
    def toLowerCase(self, s: str) -> str:
        new_str = ''

        for char in s:
            if char.isupper():
                char = char.lower()
            
            new_str += char
        
        return new_str

# OR

class Solution:
    def toLowerCase(self, string: str) -> str:
        return string.lower()

#==============================================================================================================

# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.

# The test cases are generated so that a unique mapping will always exist.

# Example 1:
#     Input: s = "10#11#12"
#     Output: "jkab"
#     Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

# Example 2:
#     Input: s = "1326#"
#     Output: "acz"
 
# Constraints:
#     1 <= s.length <= 1000
#     s consists of digits and the '#' letter.
#     s will be a valid string such that mapping is always possible.

from re import findall

class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha, new_str = ' abcdefghijklmnopqrstuvwxyz', ''
        
        for matched in findall('\d\d#|\d', s): 
            new_str += alpha[int(matched.replace('#', ''))]
        
        return new_str

#==============================================================================================================

# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

# Example 1:
#     Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
#     Output: true
#     Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

# Example 2:
#     Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
#     Output: false
#     Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

# Example 3:
#     Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
#     Output: false
#     Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 
# Constraints:
#     1 <= words.length <= 100
#     1 <= words[i].length <= 20
#     order.length == 26
#     All characters in words[i] and order are English lowercase letters.

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        return words == sorted(words, key = lambda word: list(map(order.index, word)))