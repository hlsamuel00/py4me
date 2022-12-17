# DESCRIPTION:
# Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60

from statistics import mean
def get_grade(s1, s2, s3):
    avg = mean((s1,s2,s3))
    if avg < 60:
        return 'F'
    if avg < 70:
        return 'D'
    if avg < 80:
        return 'C'
    if avg < 90:
        return 'B'
    else:
        return 'A'
    
