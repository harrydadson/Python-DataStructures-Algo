# given an array of non-negative integers, Ex: [3,3,1,0,2,0,1]
# each number represents the maximum you can advance
# is it possible to advance from the start to last?

def array_advance(A):

    furthest_reach = 0 
    last_indx = len(A) - 1
    i = 0
    while i <= furthest_reach and furthest_reach < last_indx:
        furthest_reach = max(furthest_reach, A[i] + i)
        i += 1
        
    return furthest_reach >= last_indx


A1 = [3, 3, 1, 0, 2, 0, 1]

print(array_advance(A1))
