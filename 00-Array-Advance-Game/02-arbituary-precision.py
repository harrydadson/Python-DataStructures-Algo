"""
Arbituary-precision increment
given an array of non-negative digits that represent a decimal integer

problem: Add one to the integer.
A = [1,4,9] -> 149 then add 1 -> 150
B = [9, 9, 9] -> 999 then add 1 -> 1000
"""

A1 = [1, 4, 9]
A2 = [9,9,9]
# s = ''.join(map(str, A)) # outputs 149

def plus_one(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A

print(plus_one(A1))
print(plus_one(A2))

