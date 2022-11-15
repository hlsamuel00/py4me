file_name = input("Enter file name: ")
file_handle = open(file_name)
word_list = list()

for line in file_handle:
    line_split = line.rstrip().split()
    for word in line_split:
        if word not in word_list:
            word_list.append(word)
            
word_list.sort()
print(word_list)