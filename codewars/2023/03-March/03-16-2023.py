# Failed Sort - Bug Fixing #4
# Oh no, Timmy's Sort doesn't seem to be working? Your task is to fix the sortArray function to sort all numbers in ascending order
# DEBUGGINGSORTING

def sort_array(value):
    return "".join(sorted(value, key = int))

# OR

def sort_array(value: str) -> str:
    return "".join(sorted(value))

#==============================================================================================================

# DESCRIPTION:
# Christmas is coming, and Santa has a long list to go through, to find who deserves presents for the big day. Go through a list of children, and return a list containing every child who appeared on Santa's list. Do not add any child more than once. Output should be sorted.

# Comparison should be case sensitive and the returned list should contain only one copy of each name: "Sam" and "sam" are different, but "sAm" and "sAm" are not.

def find_children(santas_list: list[str], children: list[str]):
    return sorted(child for child in set(children) if child in santas_list)

#==============================================================================================================
