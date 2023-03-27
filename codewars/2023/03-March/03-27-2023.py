# DESCRIPTION:
# Write a function that reverses the bits in an integer.

# For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.

# You can assume that the number is not negative.

def reverse_bits(n: int) -> int:
    bin_num = (bin(n)).replace('0b', '')
    new_bin = ''
    
    for i in range(-1, -len(bin_num) - 1, -1):
        new_bin += bin_num[i]
    
    return int(new_bin, 2)

# OR

def reverse_bits(n):
    return int(bin(n).replace('0b','')[::-1], 2)

#==============================================================================================================
# Complete the function to determine the number of bits required to convert integer A to integer B (where A and B >= 0)

# The upper limit for A and B is 216, int.MaxValue or similar.

# For example, you can change 31 to 14 by flipping the 4th and 0th bit:

#  31  0 0 0 1 1 1 1 1
#  14  0 0 0 0 1 1 1 0
# ---  ---------------
# bit  7 6 5 4 3 2 1 0
# Thus 31 and 14 should return 2.

def convert_bits(a, b):
    bits, count = a ^ b, 0
    
    while bits:
        bits &= bits - 1
        count += 1
        
    return count

# OR

def convert_bits(a:int, b:int) -> int:
    return bin(a ^ b).count('1')

#==============================================================================================================

# DESCRIPTION:
# Task
# You are given two numbers a and b where 0 ≤ a ≤ b. Imagine you construct an array of all the integers from a to b inclusive. You need to count the number of 1s in the binary representations of all the numbers in the array.

# Example
# For a = 2 and b = 7, the output should be 11

# Given a = 2 and b = 7 the array is: [2, 3, 4, 5, 6, 7]. Converting the numbers to binary, we get [10, 11, 100, 101, 110, 111], which contains 1 + 2 + 1 + 2 + 2 + 3 = 11 1s.

# Input/Output
# [input] integer a
# Constraints: 0 ≤ a ≤ b.

# [input] integer b
# Constraints: a ≤ b ≤ 100.

# [output] an integer

def range_bit_count(a: int, b: int) -> int:
    return sum(bin(num).count('1') for num in range(a, b + 1))

# OR

def range_bit_count(a: int, b: int) -> int:
    return sum(num.bit_count() for num in range(a, b + 1))

#==============================================================================================================

# Task
# You are given a string representing a number in binary. Your task is to delete all the unset bits in this string and return the corresponding number (after keeping only the '1's).

# In practice, you should implement this function:

# def eliminate_unset_bits(number):
# Examples
# eliminate_unset_bits("11010101010101") ->  255 (= 11111111)
# eliminate_unset_bits("111") ->  7
# eliminate_unset_bits("1000000") -> 1
# eliminate_unset_bits("000") -> 0

def eliminate_unset_bits(number):
    new_bin = '0'
    for bit in number:
        if int(bit):
            new_bin += bit
            
    return int(new_bin, 2)

# OR

def eliminate_unset_bits(number: str) -> int:
    return 2 ** number.count('1') - 1

#==============================================================================================================

# Complete the method that returns true if 2 integers share at least two 1 bits, otherwise return false. For simplicity assume that all numbers are non-negative.

# Examples
#  7  =  0111 in binary
# 10  =  1010
# 15  =  1111
# 7 and 10 share only a single 1-bit (at index 2) --> false
# 7 and 15 share 3 1-bits (at indexes 1, 2, and 3) --> true
# 10 and 15 share 2 1-bits (at indexes 0 and 2) --> true
# Hint: you can do this with just string manipulation, but binary operators will make your life much easier.

def shared_bits(a: int, b: int) -> bool:
    return bin(a & b).count('1') > 1