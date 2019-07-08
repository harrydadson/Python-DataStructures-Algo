"""
Use a stack data structure to convert integer values
to binary

Ex: 242, 242 / 2 = 121 -> 0 even
    121, 121 / 2 = 60 -> 1 odd
    60,  60 / 2  = 30 -> 0
    30,  30 / 2  = 15 -> 0
    15,  15 / 2  = 7.5  -> 1
    7.5, 7.5 / 2 = 3.5  -> 1
    3.5, 3.5 / 2 = 1.75 -> 1
    1.5, 1.5 / 2 = 0  -> 1
"""

from stacks import Stack

def div_by_2(dec_num):
    s = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2

    bin_num = ''
    while not s.is_empty():
        bin_num += str([s.pop()])

    return bin_num