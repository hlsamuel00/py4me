# DESCRIPTION:
# Sort the given array of strings in alphabetical order, case insensitive. For example:

# ["Hello", "there", "I'm", "fine"]  -->  ["fine", "Hello", "I'm", "there"]
# ["C", "d", "a", "B"])              -->  ["a", "B", "C", "d"]

def sortme(words: list[str]) -> list[str]:
    return sorted(words, key = str.lower)