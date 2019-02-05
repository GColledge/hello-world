import NodeObject
class DLList:
    # Constructor
    def __init__(self, _head):
        # Attributes
        self.head = None
        self.tail = None
        self.listType = None
        self.length = 0
        #Need to deal with the None type.
        if(_head == None):
            raise Exception("Not a valid data type")
        else:
            self.listType == type(_head)

        #create first Node
        self.head = NodeObject.Node(None, None, _head)
        self.tail = self.head
        self.length = 1

    def insert(self, data):
        #check for single Node
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

    def printList(self):
        self.head.printNodeRec()
