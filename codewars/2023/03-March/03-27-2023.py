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

