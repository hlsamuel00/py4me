import re
# number_list = list()

# file_name = 'regex_sum_1688330.txt'
# file_handle = open(file_name)

# for line in file_handle:
#     for number in re.findall('[0-9]+', line.rstrip()):
#         number = int(number)
#         number_list.append(number)

# print(sum(number_list))


#==============================================================================================================

print( sum( [ int(number) for number in re.findall('[0-9]+', open('regex_sum_1688330.txt', 'r').read()) ] ) )

x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)