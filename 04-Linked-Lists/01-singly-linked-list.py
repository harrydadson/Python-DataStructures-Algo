# Implements the Bag ADT using a Singly Linked List

class Bag:
     # constructs an empty bag
    def __init__(self):
        self._head = None
        self._size = 0

     # Returns the number of items in the bag
    def __len__(self):
        return self._size

     # Determines if an item is contained in the bag.
    def __contains__(self, target):
        currNode = self._head
        while currNode is not None and currNode.item != target:
            currNode = currNode.next
        return currNode is not None

     # Adds new item to the bag
    def add(self, item):
        newNode = _BagListNode(item)
        newNode.next = self._head
        self._head = newNode
        self._size += 1

     # Removes an instance of the item from the bag
    def remove(self, item):
        predNode = None
        currNode = self._head
        while currNode is not None and currNode.item != item:
            predNode = currNode
            currNode = currNode.next 

         # The item has to be in the bag to remove it
        assert currNode is not None, "the item is in the bag."

         # Unlink the node and return the item
        self._size -= 1
        if currNode is self._head:
            self._head = currNode.next 
        else:
            predNode.next = currNode.next 
        return currNode.item 

     # Returns an iterator for traversing the list of items
    

 # Defines a private storage for creating list nodes
class _BagListNode(object):

    def __init__(self, item):
        self.item = item
        self.next = None

 # Defines a linked list iterator for the Bag ADT
class _BagIterator:
    def __init__(self, listHead):
        self._currNode = listHead

    def next(self):
        if self._currNode is None:
            raise StopIteration
        else:
            item = self._currNode.item 
            self._currNode = self._currNode.next 
            return item  