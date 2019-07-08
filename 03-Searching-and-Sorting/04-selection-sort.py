# Implementation of th Selection Sort Algorithm O(n^2)

# Selection Sort, sort values in ascendinding order by picking each next 
# smaller number at a time

# Sorts a sequence in ascending order using selection sort

def selectionSort(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
         # Assume the ith element is the smallest
        smallNdx = i
         # Determine if any other element contains a smaller value
        for j in range(i + 1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j

         # Swap the ith value and smallNdx value only if the smalles value is
         # not already in its proper position. Some implementation omit testing
         # the condintion and always swap the two values.
        if smallNdx != i:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp 

    return theSeq

print(selectionSort([8,3,22,15,5,13,9]))