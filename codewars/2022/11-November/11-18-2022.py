# Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

# [Make sure you type the exact thing I wrote or the program may not execute properly]

def greet(name):
    return 'Hello, ' + name + ' how are you doing today?'

# OR

def greet(name):
    return f"Hello, {name} how are you doing today?"

#==============================================================================================================

# Your task is to create a function that does four basic mathematical operations.

# The function should take three arguments - operation(string/char), value1(number), value2(number).
# The function should return result of numbers after applying the chosen operation.

# Examples(Operator, value1, value2) --> output
# ('+', 4, 7) --> 11
# ('-', 15, 18) --> -3
# ('*', 5, 5) --> 25
# ('/', 49, 7) --> 7

def basic_op(operator, value1, value2):
    def add(val1,val2):
        return val1 + val2
    def subtract(val1,val2):
        return val1 - val2
    def multiply(val1,val2):
        return val1 * val2
    def divide(val1,val2):
        return val1 / val2

    operators = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }
    return operators[operator](value1, value2)

# OR

def basic_op(operator, value1, value2):
    operators = {
        '+': lambda val1,val2: val1 + val2,
        '-': lambda val1,val2: val1 - val2,
        '*': lambda val1,val2: val1 * val2,
        '/': lambda val1,val2: val1 / val2
    }
    return operators[operator](value1, value2)


# OR
def basic_op(operator, value1, value2):
    return eval(f"{value1} {operator} {value2}")