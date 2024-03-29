# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples: 
#     (a, b) --> output (explanation)
#     (1, 0) --> 1 (1 + 0 = 1)
#     (1, 2) --> 3 (1 + 2 = 3)
#     (0, 1) --> 1 (0 + 1 = 1)
#     (1, 1) --> 1 (1 since both are same)
#     (-1, 0) --> -1 (-1 + 0 = -1)
#     (-1, 2) --> 2 (-1 + 0 + 1 + 2 = 2)

def get_sum(a: int, b: int) -> int:
    return sum(range(min(a,b), max(a,b) + 1))

# OR

def get_sum(a: int, b: int) -> int:
    if a == b: return a

    if a > b: (a, b) = (b, a)
    
    return(sum(range(a, b + 1)))