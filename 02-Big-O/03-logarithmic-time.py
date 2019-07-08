# instead of incrementing (or decrementing) by one
# it cuts the loop variable in half each time through the loop

def examp(n):
    count = 0
    i = n
    while i >= 1:
        count += 1
        i = i // 2
    return count  # O(log n)

# print(examp(16)) count is 5 [16, 8, 4, 2, 1]

def examp2(n):
    count = 0 
    for i in range(n):
        count += examp(n)
    return count
# print(examp2(10)) # O(n log n)