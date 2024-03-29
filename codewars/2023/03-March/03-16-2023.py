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

# DESCRIPTION:
# You are a barista at a big cafeteria. Normally there are a lot of baristas, but your boss runs a contest and he told you that, if you could handle all the orders with only one coffee machine in such a way that the sum of all the waiting times of the customers is the smallest possible, he will give you a substantial raise.

# So you are the only barista today, and you only have one coffee machine that can brew one coffee at a time.
# People start giving you their orders.
# Let's not think about the time you need to write down their orders, but you need 2 additional minutes to clean the coffee machine after each coffee you make.

# Now you have a list coffees of the orders and you write down next to each of the orders the time you need to brew each one of those cups of coffee.

# Task:

# Given a list of the times you need to brew each coffee, return the minimum total waiting time.
# If you get it right, you will get that raise your boss promised you!

# Note that:

# It is possible to receive no orders. (It's a free day :), maybe the next day your boss will start giving you some orders himself, you probably don't want that :) )

# You can only brew one coffee at a time.

# Since you have one coffee machine, you have to wait for it to brew the current coffee before you can move on to the next one.

# Ignore the time you need to serve the coffee and the time you need to take the orders and write down the time you need to make each one of them.

# If you have three customers with times [4,3,2], the first customer is going to wait 4 minutes for his coffee, the second customer is going to wait 4 minutes (the time needed for the first customer to get his coffee), another 2 minutes (the time needed to clean the machine) and 3 more minutes (the time you need to brew his coffee), so in total 9 minutes. The third customer, by the same logic, is about to wait 9 minutes (for the first two customers) + 2 more minutes(cleaning) + 2 minutes (his coffee brewing time). This order of brewing the coffee will end up in a total waiting time of 26 minutes, but note that this may not be the minimum time needed. This time depends on the order you choose to brew the cups of coffee.

# The order in which you brew the coffee is totally up to you.

# Examples:

# coffees = [3,2,5,10,9]  ->  85
# coffees = [20,5]        ->  32
# coffees = [4,3,2]       ->  22

def barista(coffees: list[int]) -> list[int]:
    coffees.sort()

    for idx in range(1, len(coffees)):
        coffees[idx] = coffees[idx - 1] + 2 + coffees[idx]

    return sum(coffees)

# OR 

def barista(coffees: list[int]) -> list[int]:
    total = 0

    for idx, order in enumerate(sorted(coffees)):
        total += order * (len(coffees) - idx) + 2 * idx

    return total

#==============================================================================================================

# DESCRIPTION:
# Description:
# Given a string, you need to write a method that order every letter in this string in ascending order.

# Also, you should validate that the given string is not empty or null. If so, the method should return:

# "Invalid String!"
# Notes
# • the given string can be lowercase and uppercase.
# • the string could include spaces or other special characters like '# ! or ,'. Sort them based on their ASCII codes
# Examples
# "hello world" => " dehllloorw"
# "bobby"       => "bbboy"
# ""            => "Invalid String!"
# "!Hi You!"    => " !!HYiou"
# Good luck! Hope you enjoy it

def order_word(s: str) -> str:
    return 'Invalid String!' if not s else ''.join(sorted(s))

#==============================================================================================================

# The alphabetized kata
# Re-order the characters of a string, so that they are concatenated into a new string in "case-insensitively-alphabetical-order-of-appearance" order. Whitespace and punctuation shall simply be removed!

# The input is restricted to contain no numerals and only words containing the english alphabet letters.

# Example:

# alphabetized("The Holy Bible") # "BbeehHilloTy"

def alphabetized(s: str) -> str:
    return ''.join(sorted((char for char in s if char.isalpha()), key=str.lower))

# OR

def alphabetized(s: str) -> str:
    return ''.join(sorted(filter(str.isalpha, s), key = str.lower))