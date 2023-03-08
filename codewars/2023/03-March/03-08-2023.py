# DESCRIPTION:
# To participate in a prize draw each one gives his/her firstname.

# Each letter of a firstname has a value which is its rank in the English alphabet. A and a have rank 1, B and b rank 2 and so on.

# The length of the firstname is added to the sum of these ranks hence a number som.

# An array of random weights is linked to the firstnames and each som is multiplied by its corresponding weight to get what they call a winning number.

# Example:
# names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
# weights: [1, 4, 4, 5, 2, 1]

# PauL -> som = length of firstname + 16 + 1 + 21 + 12 = 4 + 50 -> 54
# The *weight* associated with PauL is 2 so PauL's *winning number* is 54 * 2 = 108.
# Now one can sort the firstnames in decreasing order of the winning numbers. When two people have the same winning number sort them alphabetically by their firstnames.

# Task:
# parameters: st a string of firstnames, we an array of weights, n a rank

# return: the firstname of the participant whose rank is n (ranks are numbered from 1)

# Example:
# names: "COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH"
# weights: [1, 4, 4, 5, 2, 1]
# n: 4

# The function should return: "PauL"

def rank(names: str, weights: list[int], n: int) -> str:
    if not names:
        return 'No participants'

    name_list = names.split(',')
    if n > len(name_list):
        return 'Not enough participants'

    def som(name: str):
        alpha, name_sum = ' abcdefghijklmnopqrstuvwxyz', len(name)

        for char in name:
            name_sum += alpha.index(char.lower())
        name_sum *= weights[name_list.index(name)]

        return name_sum
    
    return sorted(name_list, key = lambda name: (-som(name), name))[n - 1]

# OR

def rank(names: str, weights: list[int], n: int) -> str:
    if not names:
        return 'No participants'

    name_list = names.split(',')
    if n > len(name_list):
        return 'Not enough participants'

    def som(name: str):
        name_sum = len(name)

        for char in name:
            name_sum += ord(char.lower()) - 96
        
        return name_sum * weights[name_list.index(name)]
    
    return sorted(name_list, key = lambda name: (-som(name), name))[n - 1]
    
        