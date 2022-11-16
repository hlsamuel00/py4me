file_name = input("Enter file name: ")
email_count = dict()
largest = None

if len(file_name) < 1:
    file_name = "mbox-short.txt"

file_handle = open(file_name)

for line in file_handle:
    if line.startswith('From '):
        email = line.split()[1]
        email_count[email] = email_count.get(email, 0) + 1

for email in email_count:
    if email_count[email] > email_count.get(largest, 0):
        largest = email

print(largest, email_count[largest])