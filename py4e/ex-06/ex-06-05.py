str = 'X-DSPAM-Confidence:  0.8475   '

strip_index = str.find(':') + 1
str_slice = str[strip_index:].strip()
str_float = float(str_slice)

print(str_float)