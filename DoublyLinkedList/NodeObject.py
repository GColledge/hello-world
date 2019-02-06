class Node:

    def __init__(self, _previous, _next, data):
        # Node Attributes
        self.next_node = None
        self.prev_node = None
        if(type(_previous) == type(self)):
            self.prev_node = _previous
        else:
            print('Previous was not a node')
        if(type(_next) == type(self)):
            self.next_node = _next
        elif _next is None:
            pass
        else:
            print('Next was not a node')

        self.data = data

    def get_data(self):
        return self.get_data

    def get_next(self):
        return self.next_node

    def set_next(self, _next):
        if(type(_next) == type(self)):
            self.next_node = _next
        else:
            print('Next was not a node')

    def get_prev(self):
        return self.prev_node

    def set_prev(self):
        if(type(_previous) == type(self)):
            self.prev_node = _previous
        else:
            print('Previous was not a node')

    # Recursive method that allows the user to examine what is in the list
    # in order.

    def printNodeRec(self):
        print(str(self.data))
        if(self.next_node is not None):
            self.next_node.printNodeRec()
