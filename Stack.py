from Node import Node

class Stack:
    """Stack implementation using Nodes"""

    def __init__(self):
        """Create new stack"""
        self.top = None

    def __str__(self):
        """Returns a string representation of the stack, for example [a, b, c]"""
        #The newest item is at the left
        pass

    def push(self, item):
        """Add an item to the stack"""
        newNode = Node(item)
        newNode.next = self.top
        self.top = newNode

    def pop(self):
        """Removes and returns an item from the stack"""
        #if there are no more items, a ValueError should be raised
        top = self.top
        if self.top:
            self.top = None
            return top
        else:
            raise ValueError("The stack is empty")

    def is_empty(self):
        """Check if the stack is empty"""
        if self.top:
            return True
        else:
            return False
            
    def peek(self):
        """Get the value of the top item in the stack"""
        #if there are no more items None should be returned
        if self.top:
            return self.top
        else:
            return None

    def size(self):
        """Get the number of items in the stack"""
        """
        tmp = 0
        nextNode = True
        while nextNode:
            if self.is_empty():
                return tmp
            elif """
        pass
            

s = Stack()
s.push("hi")
s.push("hello")
print(s.peek())
s.pop()
print(s.peek())
