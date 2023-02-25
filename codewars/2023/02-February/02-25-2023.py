# DESCRIPTION:
# Scenario
# Now that the competition gets tough it will Sort out the men from the boys .

# Men are the Even numbers and Boys are the odd!alt!alt
# Task
# Given an array/list [] of n integers , Separate The even numbers from the odds , or Separate the men from the boys!alt!alt
# Notes
# Return an array/list where Even numbers come first then odds

# Since , Men are stronger than Boys , Then Even numbers in ascending order While odds in descending .

# Array/list size is at least 4 .

# Array/list numbers could be a mixture of positives , negatives .

# Have no fear , It is guaranteed that no Zeroes will exists .!alt
# Repetition of numbers in the array/list could occur , So (duplications are not included when separating).

# Input >> Output Examples:
# menFromBoys ({7, 3 , 14 , 17}) ==> return ({14, 17, 7, 3}) 
# Explanation:
# Since , { 14 } is the even number here , So it came first , then the odds in descending order {17 , 7 , 3}.

def men_from_boys(arr: list[int]) -> list[int]:
    evens, odds = [], []
    for person in arr:
        if not person % 2 and person not in evens:
            evens.append(person)
        
        if person % 2 and person not in odds:
            odds.append(person)
        
    return sorted(evens) + sorted(odds, reverse = True)

# OR

def men_from_boys(arr: list[int]) -> list[int]:
    men, boys = [],[]

    for person in sorted(set(arr)):
        if not person % 2:
            men.append(person)
        else:
            boys.append(person)
        
    return men + boys[::-1]