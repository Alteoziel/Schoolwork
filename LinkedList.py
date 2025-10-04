from Node import Node
import time


class LinkedList:
    """A list of (non-sorted) items"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def __str__(self):
        """Returns a string representation of the queue, for example [a, b, c]"""
        a = []
        b = self.head
        while b != None:
            a.append(str(b.data))
            b = b.next
        return ('[%s]' % ', '.join(a))
    
    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        if self.tail == None:
            self.tail = temp
            self.head = temp
            self.len += 1
            return
        temp.next = self.head
        self.head = temp
        self.len += 1
        

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next

        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next

        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            self.head = current.next
            if current.next == None:
                self.tail = None
            self.len -= 1
        else:
            previous.next = current.next
            self.len -= 1

    def append(self, item):
        """This method adds item to the end of the list"""
        tmp = Node(item)
        if self.tail == None:
            self.tail = tmp
            self.head = self.tail
            self.len += 1
            return
        self.tail.next = tmp
        self.tail = tmp
        self.len += 1

    def index(self, item):
        """This method returns the position of item in the list or raises a ValueError"""
        current = self.head
        i = 0
        while current is not None:
            if current.data == item:
                return i
            current = current.next
            i+=1

        if current is None:
            raise ValueError("{} is not in the list".format(item))
        if i == 0:
            return i
        raise ValueError("This item is not in the list.")

    def insert(self, posn, item):
        """adds a new item to the list at position posn or raises a ValueError."""
        current = self.head
        previous = None
        i = 0
        while self.len >= posn:
            if i == posn:
                break
            previous = current
            current = current.next
            i += 1

        if previous is None:
            temp = Node(item)
            if self.tail == None:
                self.tail = temp
                self.head = temp
                self.len += 1
                return
            else:
                a = self.head
                temp.next = a
                self.head = temp
                self.len += 1
        else:
            temp = Node(item)
            if self.tail == None:
                self.tail = temp
                self.head = self.tail
                self.len += 1
                return
            else:
                temp.next = current
                previous.next = temp
                self.len += 1
        

    def pop(self):
        """removes and returns the last item in the list or raises a ValueError"""
        current = self.head
        previous = None


        if current == None:
            if previous is None:
                raise ValueError("Nothing in this list.")
            else:
                a = previous
                self.head = None
                self.tail = None
                return a.data
        while current.next is not None:
            if current.next == None:
                break
            previous = current
            current = current.next
            """
            print(previous)
            print(current)
            print(current.next)
            print("\n")
            """

        if previous is None:
            a = self.head
            self.head = None
            self.tail = None
            return a.data
            
        else:
            a = self.tail
            current = None
            self.tail = previous
            previous.next = current
            return a.data

    def pop_at_position(self, posn):
        """removes and returns the item at position posn or raises a ValueError."""
        current = self.head
        temp = None
        previous = None
        i = 0
        while i != posn:
            if current is None:
                raise ValueError("This position does not exist.")
            previous = current
            current = current.next
            i+=1
        if previous is None:
            a = current
            self.head = current.next
            return a.data
            
        else:
            a = current
            previous.next = current.next
            return a.data






"""

L = LinkedList()
l = list()


#Test 1
start = time.time()
for i in range(1,1001):
    L.add(1)
for i in range(1,1001):
    L.pop_at_position(0)
end = time.time()
print(end-start)

start = time.time()
for i in range(1,10001):
    L.add(1)
for i in range(1,10001):
    L.pop_at_position(0)
end = time.time()
print(end-start)

start = time.time()
for i in range(1,100001):
    L.add(1)
for i in range(1,100001):
    L.pop_at_position(0)
end = time.time()
print(end-start)

start = time.time()
for i in range(1,1000001):
    L.add(1)
for i in range(1,1000001):
    L.pop_at_position(0)
end = time.time()
print(end-start)

start = time.time()
for i in range(1,1001):
    l.insert(0,1)
for i in range(1,1001):
    l.pop(0)
end = time.time()
print(end-start)

start = time.time()
for i in range(1,10001):
    l.insert(0,1)
for i in range(1,10001):
    l.pop(0)
end = time.time()
print(end-start)

start = time.time()
for i in range(1,100001):
    l.insert(0,1)
for i in range(1,100001):
    l.pop(0)
end = time.time()
print(end-start)

start = time.time()
for i in range(1,1000001):
    l.insert(0,1)
for i in range(1,1000001):
    l.pop(0)
end = time.time()
print(end-start)




#Test 2
start = time.time()
size = L.size()
for i in range(1,1001):
    L.insert(int(size/2), 1)
for i in range(1,1001):
    L.pop_at_position(int(size/2))
end = time.time()
print(end-start)

size = L.size()
start = time.time()
for i in range(1,10001):
    L.insert(int(size/2), 1)
for i in range(1,10001):
    L.pop_at_position(int(size/2))
end = time.time()
print(end-start)

size = L.size()
start = time.time()
for i in range(1,100001):
    L.insert(int(size/2), 1)
for i in range(1,100001):
    L.pop_at_position(int(size/2))
end = time.time()
print(end-start)

size = L.size()
start = time.time()
for i in range(1,1000001):
    L.insert(int(size/2), 1)
for i in range(1,1000001):
    L.pop_at_position(int(size/2))
end = time.time()
print(end-start)



size = len(l)
start = time.time()
for i in range(1,1001):
    l.insert(int(size/2),1)
for i in range(1,1001):
    l.pop(int(size/2))
end = time.time()
print(end-start)

size = len(l)
start = time.time()
for i in range(1,10001):
    l.insert(int(size/2),1)
for i in range(1,10001):
    l.pop(int(size/2))
end = time.time()
print(end-start)

size = len(l)
start = time.time()
for i in range(1,100001):
    l.insert(int(size/2),1)
for i in range(1,100001):
    l.pop(int(size/2))
end = time.time()
print(end-start)

size = len(l)
start = time.time()
for i in range(1,1000001):
    l.insert(int(size/2),1)
for i in range(1,1000001):
    l.pop(int(size/2))
end = time.time()
print(end-start)



#Test 3
start = time.time()
for i in range(1,1001):
    L.append(1)
for i in range(1,1001):
    L.pop()
end = time.time()
print(end-start)

start = time.time()
for i in range(1,10001):
    L.append(1)
for i in range(1,10001):
    L.pop()
end = time.time()
print(end-start)

start = time.time()
for i in range(1,100001):
    L.append(1)
for i in range(1,100001):
    L.pop()
end = time.time()
print(end-start)

start = time.time()
for i in range(1,1000001):
    L.append(1)
for i in range(1,1000001):
    L.pop()
end = time.time()
print(end-start)



start = time.time()
for i in range(1,1001):
    l.append(1)
for i in range(1,1001):
    l.pop()
end = time.time()
print(end-start)

start = time.time()
for i in range(1,10001):
    l.append(1)
for i in range(1,10001):
    l.pop()
end = time.time()
print(end-start)

start = time.time()
for i in range(1,100001):
    l.append(1)
for i in range(1,100001):
    l.pop()
end = time.time()
print(end-start)

start = time.time()
for i in range(1,1000001):
    l.append(1)
for i in range(1,1000001):
    l.pop()
end = time.time()
print(end-start)
"""
