from Node import Node
import time

class Queue:
    """Queue implementation using Nodes"""

    def __init__(self):
        """Create new queue"""
        self.head = None
        self.tail = None

    def __str__(self):
        """Returns a string representation of the queue, for example [a, b, c]"""
        a = []
        b = self.head
        while b != None:
            a.append(str(b))
            b = b.next
        return ('[%s]' % ', '.join(a))

    def enqueue(self, item):
        """Add an item to the queue"""
        tmp = Node(item)
        if self.tail == None:
            self.tail = tmp
            self.head = self.tail
            return
        self.tail.next = tmp
        self.tail = tmp
        
        

    def dequeue(self):
        """Removes and returns an item from the queue"""
        #if there are no more items, a ValueError should be raised
        if self.head == None:
            raise ValueError("No more items.")
        else:
            a = self.head.data
            self.head = self.head.next
            return a

    def is_empty(self):
        """Check if the queue is empty"""
        if self.head == None:
            return True
        else:
            return False

    def peek(self):
        """Get the value of the first item in the queue"""
        #if there are no more items None should be returned
        if self.head == None:
            return None
        else:
            return self.head.data

    def size(self):
        """Get the number of items in the queue"""
        tmp = 0
        c = self.head
        while c != None:
            tmp += 1
            c = c.next
        return tmp


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.peek())
print(q.dequeue())
print(q.dequeue())
q.enqueue(4)
q.enqueue(5)
print(q.size())
print(q.is_empty())


start = time.time()
for i in range(1,1001):
    q.enqueue(1)
for i in range(1,1001):
    q.dequeue()
end = time.time()
print(end-start)

start = time.time()
for i in range(1,10001):
    q.enqueue(1)
for i in range(1,10001):
    q.dequeue()
end = time.time()
print(end-start)

start = time.time()
for i in range(1,100001):
    q.enqueue(1)
for i in range(1,100001):
    q.dequeue()
end = time.time()
print(end-start)

start = time.time()
for i in range(1,1000001):
    q.enqueue(1)
for i in range(1,1000001):
    q.dequeue()
end = time.time()
print(end-start)

