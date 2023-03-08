hours_string = input('Enter hours: ') 
rate_string = input('Enter rate: ')

def compute_pay(hours, rate):
    try : 
        hours_float = float(hours_string)
        rate_float = float(rate_string)
    except : 
        print('Error, please provide numeric value.')
        quit()

    pay = hours_float * rate_float

    if hours_float > 40:
        overtime_pay = (hours_float - 40) * rate_float * 1.5
        regular_pay = 40 * rate_float
        pay = overtime_pay + regular_pay

    print("Pay:", pay)

compute_pay(hours_string, rate_string)