hours_string = input('Enter hours: ') 
rate_string = input('Enter rate: ')
hours_float = float(hours_string)
rate_float = float(rate_string)
pay = hours_float * rate_float

if hours_float > 40:
    overtime_float = hours_float - 40
    hours_float = hours_float - overtime_float
    pay = hours_float * rate_float + (overtime_float * rate_float * 1.5)

print("Pay:", pay)