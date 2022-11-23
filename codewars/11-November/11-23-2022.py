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

# DESCRIPTION:
# Can you find the needle in the haystack?

# Write a function findNeedle() that takes an array full of junk but containing one "needle"

# After your function finds the needle it should return a message (as a string) that says:

# "found the needle at position " plus the index it found the needle, so:

# Example(Input --> Output)

# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
# Note: In COBOL, it should return "found the needle at position 6"

def find_needle(haystack:list):
    idx = haystack.index('needle')
    return f'found the needle at position {idx}'