# DESCRIPTION:
# Write function bmi that calculates body mass index (bmi = weight / height2).

# if bmi <= 18.5 return "Underweight"

# if bmi <= 25.0 return "Normal"

# if bmi <= 30.0 return "Overweight"

# if bmi > 30 return "Obese"

def bmi(weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5: 
        return "Underweight"
    if bmi <= 25.0:
        return "Normal"
    if bmi <= 30.0:
        return "Overweight"
    if bmi > 30:
        return "Obese"
    else:
        return 'Invalid Entry'

# OR

def bmi(weight, height):
    bmi_calc = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(bmi_calc > 30) + (bmi_calc > 25) + (bmi_calc > 18.5)]