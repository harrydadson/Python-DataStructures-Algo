# Implementation of the Linear Search on an Unsorted Sequence

def linearSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        # if the target is in the ith element, return true
        if theValues[i] == target:
            return True
        return False

# print(linearSearch([2,5,1,6,7], 2)) ans: True


# Searching a Sorted Sequence

def sortedLinearSearch(theValues2, targetitem):
    n = len(theValues2)
    for i in range(n):
        # if the target is found in the ith element, return True
        if theValues2[i] == targetitem:
            return True
        # if the target is larger than the ith element, it's not in the sequence
        elif theValues2[i] > targetitem:
            return False

    return False

print(sortedLinearSearch([1,3,4,5,8,12], 5))


# Finding the Smallest Value in an Unsorted Sequence O(n)

def findSmallest(theValues3):
    n = len(theValues3)
     # Assume the first item is the smallest value
    smallest = theValues3[0]
     # Determine if any other item in the sequence is smaller
    for i in range(1, n):
        if theValues3[i] < smallest:
            smallest = theValues3[i]

    return smallest 

print(findSmallest([5,1,3,4,5]))


