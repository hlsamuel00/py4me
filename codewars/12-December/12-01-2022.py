# DESCRIPTION:
# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

def simple_multiplication(number) :
    return number * (8 if not number % 2 else 9)

# OR

def simple_multiplication(number):
    return number * (8 + number % 2)