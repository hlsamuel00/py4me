# DESCRIPTION:
# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

def fake_bin(x):
    new_x = ''
    for char in x:
        if int(char) < 5:
            new_x += '0'
        else:
            new_x += '1'
    return new_x

# OR

def fake_bin(x):
    return ''.join([ '0' if int(char) < 5 else '1' for char in x ])