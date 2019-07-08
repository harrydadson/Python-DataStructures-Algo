# Implementation of Bubble Sort Algorithm O(n^2)

# Bubble Sort moves numbers around until sorted from smaller to bigger

 # Sorts a sequence in ascending order using the bubble sort algorithm
def bubbleSort(theSeq):
    n = len(theSeq)
     # Perform n-1 buble operations on the sequence
    for i in range(n - 1):
         # Bubble the largest item to the end
        for j in range(i + n - 1):
            if theSeq[j] > theSeq[j + 1]:  # swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp

print(bubbleSort([10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]))
