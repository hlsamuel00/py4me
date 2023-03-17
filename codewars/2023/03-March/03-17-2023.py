# #Sorting on planet Twisted-3-7

# There is a planet... in a galaxy far far away. It is exactly like our planet, but it has one difference: #The values of the digits 3 and 7 are twisted. Our 3 means 7 on the planet Twisted-3-7. And 7 means 3.

# Your task is to create a method, that can sort an array the way it would be sorted on Twisted-3-7.

# 7 Examples from a friend from Twisted-3-7:

# [1,2,3,4,5,6,7,8,9] -> [1,2,7,4,5,6,3,8,9]
# [12,13,14] -> [12,14,13]
# [9,2,4,7,3] -> [2,7,4,3,9]
# There is no need for a precheck. The array will always be not null and will always contain at least one number.

# You should not modify the input array!

# Have fun coding it and please don't forget to vote and rank this kata! :-)

def sort_twisted37(arr: list[int]) -> list[int]:
    
    def twisted(num:int) -> int:
        new_num, swaps = '', '37'

        for digit in str(num):
            if digit in swaps:
                new_num += swaps[(swaps.index(digit) + 1) % len(swaps)]
            else:
                new_num += digit
        return int(new_num)
    
    return sorted(arr, key = twisted )

# OR 

def sort_twisted37(arr: list[int]) -> list[int]:
    
    def twisted(num:int) -> int:
        return int(str(num).translate(str.maketrans('37', '73')))
    
    return sorted(arr, key = twisted )

#==============================================================================================================
