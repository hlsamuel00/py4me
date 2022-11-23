# DESCRIPTION:
# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]

def maps(array):
    return [ element * 2 for element in array ]

#==============================================================================================================

# DESCRIPTION:
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# patrick feeney => P.F

def abbrev_name(name):
    return '.'.join([part[0].upper() for part in name.split()])

# OR

def abbrev_name(name:str):
    first,last = name.upper().split()
    return f'{first[0]}.{last[0]}'

#=============================================================================================================