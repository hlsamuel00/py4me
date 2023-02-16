# DESCRIPTION:
# Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))
#     1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
#     5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

def add_binary(num1: int, num2: int) -> str:
    return bin(num1 + num2).replace('0b', '')

#==============================================================================================================

# In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

# At the end of the first year there will be: 
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants

# At the end of the 2nd year there will be: 
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)

# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213

# It will need 3 entire years.

def nb_year(p0, percent, aug, p, year_count = 0):
    
    while p0 < p:
        p0 += int(p0 * percent/100) + aug
        year_count += 1
    
    return year_count

# OR (with recursion)

def nb_year(p0, percent, aug, p, years = 0):
    if p0 < p:
        return nb_year((p0 + int(p0 * (percent / 100)) + aug), percent, aug, p, years + 1)
    else:
        return years