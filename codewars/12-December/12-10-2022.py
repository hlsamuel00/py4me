# Write a function to split a string and convert it into an array of words.

# Examples (Input ==> Output):
# "Robin Singh" ==> ["Robin", "Singh"]

# "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]

def string_to_array(s):
    return s.split(' ')

#==============================================================================================================

# Create a function with two arguments that will return an array of the first n multiples of x.

# Assume both the given number and the number of times to count will be positive numbers greater than 0.

# Return the results as an array or list ( depending on language ).

# Examples
# count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) #should return [2,4,6,8,10]

def count_by(x, n):
    return [ idx * x for idx in range(1,n+1) ]

#==============================================================================================================

# DESCRIPTION:
# If you can't sleep, just count sheep!!

# Task:
# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    string = ''
    for idx in range(n):
        string += f'{idx+1} sheep...'
    return string
# OR

def count_sheep(number_of_sheep):
    return ''.join(f'{idx + 1} sheep...' for idx in range(number_of_sheep))
