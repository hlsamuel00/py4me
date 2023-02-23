# DESCRIPTION:
# Just a simple sorting usage. Create a function that returns the elements of the input-array / list sorted in lexicographical order.

def sortme(names):
    return sorted(names)

#==============================================================================================================

# Task
# You are given a dictionary/hash/object containing some languages and your test results in the given languages. Return the list of languages where your test score is at least 60, in descending order of the scores.

# Note: the scores will always be unique (so no duplicate values)

# Examples
# {"Java": 10, "Ruby": 80, "Python": 65}    -->  ["Ruby", "Python"]
# {"Hindi": 60, "Dutch" : 93, "Greek": 71}  -->  ["Dutch", "Greek", "Hindi"]
# {"C++": 50, "ASM": 10, "Haskell": 20}     -->  []

def my_languages(results: dict) -> list:
    filtered_results = [key for key,value in results.items() if value > 59]
    return sorted(filtered_results, key = results.get, reverse = True)

# OR

def my_languages(results: dict) -> list:
    return sorted([key for key,value in results.items() if value > 59], key = results.get, reverse = True)