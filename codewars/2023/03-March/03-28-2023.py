# DESCRIPTION:
# Return true when any odd bit of x equals 1; false otherwise.

# Assume that:

# x is an unsigned, 32-bit integer;
# the bits are zero-indexed (the least significant bit is position 0)
# Examples
#   2  -->  1 (true) because at least one odd bit is 1 (2 = 0b10)
#   5  -->  0 (false) because none of the odd bits are 1 (5 = 0b101)
# 170  -->  1 (true) because all of the odd bits are 1 (170 = 0b10101010)

def any_odd(num: int) -> bool:
    for bit in range(1, len(bin(num)), 2):
        if num & (1 << bit):
            return True
        
    return False
#==============================================================================================================

# DESCRIPTION:
# Take the following IPv4 address: 128.32.10.1 This address has 4 octets where each octet is a single byte (or 8 bits).

# 1st octet 128 has the binary representation: 10000000
# 2nd octet 32 has the binary representation: 00100000
# 3rd octet 10 has the binary representation: 00001010
# 4th octet 1 has the binary representation: 00000001
# So 128.32.10.1 == 10000000.00100000.00001010.00000001

# Because the above IP address has 32 bits, we can represent it as the 32 bit number: 2149583361.

# Write a function ip_to_int32(ip) ( JS: ipToInt32(ip) ) that takes an IPv4 address and returns a 32 bit number.

#   ip_to_int32("128.32.10.1") => 2149583361

def ip_to_int32(ip: str) -> int:
    return int(''.join(map(lambda num: bin(int(num))[2:].rjust(8,'0'), ip.split('.'))), 2)

# OR

def ip_to_int32(ip: str) -> int:
    ip_pieces, results = ip.split('.'), 0

    for idx, part in enumerate(ip_pieces):
        results += int(part) << 8 * (len(ip_pieces) - 1 - idx)
    
    return results

#==============================================================================================================

# DESCRIPTION:
# The odd and even numbers are fighting against each other!

# You are given a list of positive integers. The odd numbers from the list will fight using their 1 bits from their binary representation, while the even numbers will fight using their 0 bits. If present in the list, number 0 will be neutral, hence not fight for either side.

# You should return:

# odds win if number of 1s from odd numbers is larger than 0s from even numbers
# evens win if number of 1s from odd numbers is smaller than 0s from even numbers
# tie if equal, including if list is empty
# Please note that any prefix that might appear in the binary representation, e.g. 0b, should not be counted towards the battle.

# Example:
# For an input list of [5, 3, 14]:

# odds: 5 and 3 => 101 and 11 => four 1s
# evens: 14 => 1110 => one 0
# Result: odds win the battle with 4-1

def bits_battle(numbers: list[int]) -> str:
    odds = evens = 0
    
    for num in numbers:
        if num:
            if num & 1:
                odds += bin(num)[2:].count('1')
            else:
                evens += bin(num)[2:].count('0')
            
    return 'odds win' if odds > evens else 'evens win' if evens > odds else 'tie'

#==============================================================================================================

