# Failed Sort - Bug Fixing #4
# Oh no, Timmy's Sort doesn't seem to be working? Your task is to fix the sortArray function to sort all numbers in ascending order
# DEBUGGINGSORTING

def sort_array(value):
    return "".join(sorted(value, key = int))

# OR

def sort_array(value: str) -> str:
    return "".join(sorted(value))

#==============================================================================================================
