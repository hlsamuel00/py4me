# DESCRIPTION:
# In this kata you will be given a sequence of the dimensions of rectangles ( sequence with width and length ) and circles ( radius - just a number ).
# Your task is to return a new sequence of dimensions, sorted ascending by area.

# For example,

# seq = [ (4.23, 6.43), 1.23, 3.444, (1.342, 3.212) ] # [ rectangle, circle, circle, rectangle ]
# sort_by_area(seq) => [ ( 1.342, 3.212 ), 1.23, ( 4.23, 6.43 ), 3.444 ]


from math import pi

def sort_by_area(seq: list) -> list: 
    def get_area(shape: int): 
        return shape[0] * shape[1] if type(shape) == tuple else pi * shape ** 2
    
    return sorted(seq, key = get_area)

# OR

def sort_by_area(seq: list) -> list:
    return sorted(seq, key = lambda shape: shape[0] * shape[1] if isinstance(shape, tuple) else pi * shape ** 2)