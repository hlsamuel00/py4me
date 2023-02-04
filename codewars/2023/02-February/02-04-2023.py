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

