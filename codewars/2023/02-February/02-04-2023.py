# DESCRIPTION:
# In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

# Example
#     filter_list([1,2,'a','b']) == [1,2]
#     filter_list([1,'a','b',0,15]) == [1,0,15]
#     filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def filter_list(l):
    return [ val for val in l if type(val) is int ]

#============================================================================================================

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false

def is_isogram(string):
    for letter in string.lower():
        if string.lower().count(letter) > 1:
            return False        
    
    return True

#==============================================================================================================

# DESCRIPTION:
# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

# Example: 
# The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n):
    return bin(n).count('1')