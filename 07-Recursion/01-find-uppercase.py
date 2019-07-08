# Given a string, find the first uppercase Character
# Solve using both iterative and recursive solution

input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"

def find_upper_iter(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]

    return "No uppercase found"

def find_upper_rec(input_str, indx=0):
    if input_str[indx].isupper():
        return input_str[indx]
    if indx == len(input_str) - 1:
        return 'No uppercase found'

    return find_upper_rec(input_str, indx + 1)


print(find_upper_iter(input_str_1))
print(find_upper_iter(input_str_2))
print(find_upper_iter(input_str_3))

print('---------------------------')

print(find_upper_rec(input_str_1))
print(find_upper_rec(input_str_2))
print(find_upper_rec(input_str_3))
