# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
file_handle = open(fname)
count = 0
total = 0

for line in file_handle:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    total = total + float(line[line.find(':')+1:])
    count = count + 1

print('Average spam confidence:', total / count)