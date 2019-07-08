# Given a string, count the number of consonants.
# Note a consonant is a letter that is not a vowel
# i.e. a letter that is not a,e,i,o, or u

input_str_1 = 'abc de'
input_str_2 = "LuCiDProGrAmMinNG"

vowels = 'aeiou'

def iter_count_consonant(input_str):
    count = 0 
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowels and input_str[i].isalpha():
            count += 1
    return count

def rec_count_consonant(input_str):
    if input_str == '':
        return 0
    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + rec_count_consonant(input_str[1:])
    else:
        return rec_count_consonant(input_str[1:])


print(iter_count_consonant(input_str_1))
print(iter_count_consonant(input_str_2))

print('--------------------------')

print(rec_count_consonant(input_str_1))
print(rec_count_consonant(input_str_2))
