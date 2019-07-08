# Implementation of the Binary Search Algorithm O(log n)

# - Variables low and high are used to mark the range of elements
# - First step is to determine the midpoint in each iteration of the sequence
# - if sequence contains an even number of elements, the midpoint will be chosen
#   such that the left sequence contains one less than the right

def binarySearch(theValues, target):
     # Start with the entire sequence of elements
    low = 0
    high = len(theValues) - 1 

     # Repeatedly subdivide the sequence in half until the target is found
    while low <= high:
           # Find the midpoint of the sequence
        mid = (high + low) // 2
           # Does the midpoint contain the target?
        if theValues[mid] == target:
            return True
           # Or does the target precede the midpoint?
        elif target < theValues[mid]:
            high = mid - 1
           # Or does it follow the midpoint?
        else:
            low = mid + 1

     # If the sequence cannot be subdivided further, we're done
    return False 

print(binarySearch([2,4,5,10,13,18,23,29,31,51,64], 10))
print(binarySearch([2, 4, 5, 10, 13], 10))
print(binarySearch([10, 13], 10))

# mid is 18, greater than 10, discard upper half
# repeat the process, mid is 5, less than 10, discard lower half
# repeat, then we find 10
        
