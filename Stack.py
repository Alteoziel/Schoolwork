from Node import Node

class Stack:
    """Stack implementation using Nodes"""

    def __init__(self):
        """Create new stack"""
        self.head = None

    def __str__(self):
        """Returns a string representation of the stack, for example [a, b, c]"""
        c = []
        d = self.head
        while d != None:
            c.append(str(d))
            d = d.next
        return ('[%s]' % ', '.join(c))
        

    def push(self, item):
        """Add an item to the stack"""
        tmp = Node(item)
        tmp.next = self.head
        self.head = tmp

    def pop(self):
        """Removes and returns an item from the stack"""
        #if there are no more items, a ValueError should be raised
        if self.head == None:
            raise ValueError("No more items.")
        else:
            a = self.head.data
            self.head = self.head.next
            return a

    def is_empty(self):
        """Check if the stack is empty"""
        if self.head == None:
            return True
        else:
            return False

    def peek(self):
        """Get the value of the top item in the stack"""
        #if there are no more items None should be returned
        if self.head == None:
            return None
        else:
            return self.head.data

    def size(self):
        """Get the number of items in the stack"""
        tmp = 0
        b = self.head
        while b != None:
            tmp += 1
            b = b.next
        return tmp


#test 100, 1000, 1000000,1000000000 with push and pop
