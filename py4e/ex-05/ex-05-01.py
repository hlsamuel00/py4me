count = 0
total = 0.0

while True:
    string_value = input('Enter a number: ')
    if string_value == 'done':
        break
    try:
        float_value = float(string_value)
    except:
        print('Invalid Input.')
        continue
    count = count + 1
    total = total + float_value 

print('All done!')
print(total, count, total / count)