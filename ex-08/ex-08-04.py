file_name = input("Enter file name: ")
file_handle = open(file_name)
word_list = list()

for line in file_handle:
    line_split = line.rstrip().split()
    for word in line_split:
        if not word_list.count(word):
            word_list.append(word)
            
word_list.sort()
print(word_list)