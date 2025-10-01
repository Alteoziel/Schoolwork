from Node import Node
class LinkedList:
    """A list of (non-sorted) items"""

    def __init__(self):
        self.head = None
        self.tail = None

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
            self.head = self.tail
            return
        temp.next = self.head
        self.head = temp

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
        else:
            previous.next = current.next

    def append(self, item):
        """This method adds item to the end of the list"""
        tmp = Node(item)
        if self.tail == None:
            self.tail = tmp
            self.head = self.tail
            return
        self.tail.next = tmp
        self.tail = tmp

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

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if i == 0:
            temp = Node(item)
            self.head = temp
            self.tail = temp
            return
        if previous is None:
            temp = Node(item)
            previous.next = temp
            temp.next = current
            
        

    def pop(self):
        """removes and returns the last item in the list or raises a ValueError"""
        current = self.head
        previous = None

        while current is not None:
            previous = current
            current = current.next

        if current is None:
            raise ValueError("Nothing to pop in the list")
        if previous is None:
            self.head = current.next
        else:
            a = self.tail
            self.tail = self.previous
            return a

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
            self.head = current.next
        else:
            previous.next = current.next
