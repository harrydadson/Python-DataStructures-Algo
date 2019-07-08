# ex1() function, which computes the sum of the integer
# values in the range [0..n)

# O(n)

def ex1(n):
    total = 0
    for i in range(n):
        total += i
    return total

# print(ex1(5))

def ex2(n):
    count = 0
    for i in range(n):
        count += 1
    for j in range(n):
        count += 1
    return count

print(ex2(5))