file_name = input("Enter file:")
hour_count = dict()

if len(file_name) < 1:
    file_name = "mbox-short.txt"

file_handle = open(file_name)

for line in file_handle:
    if line.startswith('From '):
        hour = line.split()[5].split(':')[0]
        hour_count[hour] = hour_count.get(hour,0) + 1

hour_list = sorted([ (key,value) for key, value in hour_count.items() ])

for key,value in hour_list:
    print(key,value)
