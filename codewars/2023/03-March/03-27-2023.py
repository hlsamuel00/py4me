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