# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
#     Input: a = "11", b = "1"
#     Output: "100"

# Example 2:
#     Input: a = "1010", b = "1011"
#     Output: "10101"

# Constraints:
#     1 <= a.length, b.length <= 104
#     a and b consist only of '0' or '1' characters.
#     Each string does not contain leading zeros except for the zero itself.


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = list(a.rjust(len(b), '0')),  list(b.rjust(len(a), '0'))

        new_bin = ''
        for idx in range(-1, -(len(a) + 1), -1):
            bin_sum = int(a[idx]) + int(b[idx])
            if bin_sum > 1:
                new_bin = str(bin_sum % 2) + new_bin
                if -idx < len(a): 
                    a[idx - 1] = str(int(a[idx - 1]) + 1)
                else:
                    new_bin = '1' + new_bin
            else:
                new_bin = str(bin_sum) + new_bin

        return new_bin            

# OR

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a.rjust(len(b), '0'), b.rjust(len(a), '0')

        temp, new_bin = 0, ''

        for idx in range(-1, -(len(a) + 1), -1):
            bin_sum = int(a[idx]) + int(b[idx]) + temp
            new_bin = str(bin_sum % 2) + new_bin
            temp = bin_sum // 2

        if temp > 0:
            new_bin = str(temp) + new_bin

        return new_bin
    
# OR

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
    
#==============================================================================================================

