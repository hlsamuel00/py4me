file_name = input("Enter file name: ")
count = 0

if len(file_name) < 1:
    file_name = "mbox-short.txt"

file_handle = open(file_name)

for line in file_handle:
    if line.startswith('From '):
        email = line.split()[1]
        count = count + 1
        print(email)

print("There were", count, "lines in the file with From as the first word")

            
