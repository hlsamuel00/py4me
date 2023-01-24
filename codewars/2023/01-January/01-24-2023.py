# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:
#     Input: word1 = "abc", word2 = "pqr"
#     Output: "apbqcr"
#     Explanation: The merged string will be merged as so:
#     word1:  a   b   c
#     word2:    p   q   r
#     merged: a p b q c r

# Example 2:
#     Input: word1 = "ab", word2 = "pqrs"
#     Output: "apbqrs"
#     Explanation: Notice that as word2 is longer, "rs" is appended to the end.
#     word1:  a   b 
#     word2:    p   q   r   s
#     merged: a p b q   r   s

# Example 3:
#     Input: word1 = "abcd", word2 = "pq"
#     Output: "apbqcd"
#     Explanation: Notice that as word1 is longer, "cd" is appended to the end.
#     word1:  a   b   c   d
#     word2:    p   q 
#     merged: a p b q c   d
 
# Constraints:
#     1 <= word1.length, word2.length <= 100
#     word1 and word2 consist of lowercase English letters.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ''

        for idx in range(max(len(word1),len(word2))):
            if idx >= len(word1): 
                new_str += word2[idx:]
                break
            elif idx >= len(word2): 
                new_str += word1[idx:]
                break
            else:
                new_str += word1[idx] + word2[idx]

        return new_str

#==============================================================================================================

# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.

# Example 1:
#     Input: command = "G()(al)"
#     Output: "Goal"
#     Explanation: The Goal Parser interprets the command as follows:
#     G -> G
#     () -> o
#     (al) -> al
#     The final concatenated result is "Goal".

# Example 2:
#     Input: command = "G()()()()(al)"
#     Output: "Gooooal"

# Example 3:
#     Input: command = "(al)G(al)()()G"
#     Output: "alGalooG"
 
# Constraints:
#     1 <= command.length <= 100
#     command consists of "G", "()", and/or "(al)" in some order.

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')

#==============================================================================================================

