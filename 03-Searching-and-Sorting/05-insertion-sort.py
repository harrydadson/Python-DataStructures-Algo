# Implementation of Insertion Sort Algorithm

# Insertion look at the next index values and pick and put
# them at their right sport in ascending order

# Sorts a sequence in ascending order using Insertion

def insertionSort(theSeq):
    n = len(theSeq)
     # Starts with the first item as the only sorted entry
    for i in range(1, n):
         # Save the value to be positioned
        value = theSeq[i]
         # find the position where the value fits in the ordered part of the list
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
             # shift the items to the right during search
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1

         # Put the saved value into the open slot
        theSeq[pos] = value

    return theSeq

print(insertionSort([8,3,22,15,5,13,9]))
             