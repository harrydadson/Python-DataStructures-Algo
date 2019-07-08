# Given two numbers, find their product using recursion

x = 500
y = 2000

# 5 x 3

def recursive_multiply(x, y):
     # this cuts down on the total of recursive calls:

    if x < y:
        return recursive_multiply(y, x)
    
    if y == 0:
        return 0

    return x + recursive_multiply(x, y - 1)

print(x * y)
print(recursive_multiply(x, y))
    