# Given a string, calculate the length of the string

input_str = 'LucidProgramming'

print(len(input_str))

def iter_str_len(input_str):
    count = 0
    for i in range(len(input_str)):
        count += 1
    return count

def rec_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + rec_str_len(input_str[1:])

print(iter_str_len(input_str))
print(rec_str_len(input_str))