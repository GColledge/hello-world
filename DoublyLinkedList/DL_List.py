## Double Linked List Class
# -----------------------------------
# @package DoublyLinkedList
# @author: Greg Colledge
#  Feb 5, 2019 - This is my implementation of a linked list. It can be used
# as a queue or stack.
# -----------------------------------
import NodeObject


class DLList:

    def __init__(self, _head):
        ## ----- Constructor -----
        # @param[in] _head : The first data to store in the list.
        # @warning the type of object that is passed in as the _head parameter
        # will determine the data type this list holds

        # Attributes
        self.head = None
        self.tail = None
        self.listType = None
        self.length = 0
        # Need to deal with the None type.
        if(_head is None):
            raise Exception("Not a valid data type")
        else:
            self.listType == type(_head)

        # create first Node
        self.head = NodeObject.Node(None, None, _head)
        self.tail = self.head
        self.length = 1

    ## ----- Append method -----
    # This appends a new node at the end of the list
    # @param[in] data : the data that will be held in the list.

    def append(self, data):

        # check for single Node
        if(self.length == 1):
            newNode = NodeObject.Node(self.head, None, data)
            self.head.set_next(newNode)
            self.tail = newNode
        elif(self.length == 0):
            # Factor out constructor and use here
            print('this is printed when the length reaches zero.')
        else:
            newNode = NodeObject.Node(self.tail, None, data)
            self.tail.set_next(newNode)
            self.tail = newNode
        self.length += 1

    ## ----- Insert Method -----
    # This method will insert the data at the specified location in the list.
    # TODO: write this method. Search from the back if it is faster.

    ## ----- Delete Position Method -----
    # This method deletes the node in the specified location.
    # @param[in] position : an int defining which node in the list to delete.
    # @return The data that was held in the node that was deleted.
    # TODO: write this function

    ## ----- Delete Data Method -----
    # This method deletes the first node containing the given Data
    # @param[in] data : the value that should be removed from the list.
    # @param[in] front : a keywordf argument telling wether to start looking
    # from the back or the front of the list.
    # @return the position of that the value was in, or None if not found.
    # TODO: write this method.

    ## ----- Print List Method -----
    # This function prints the data of every node in the list.

    def printList(self):
        self.head.printNodeRec()
