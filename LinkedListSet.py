from LinkedList import LinkedList
from Node import Node

class LinkedListSet(LinkedList):
    def __init__(self):
        super().__init__()

    def add(self, item):
        a = self.search(item)
        if a == True:
            return
        else:
            temp = Node(item)
            temp.next = self.head
            self.head = temp

    def append(self, item):
        """This method adds item to the end of the list"""
        a = self.search(item)
        if a == True:
            return
        if self.head == None:
            self.head = Node(item)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(item)

    def insert(self, posn, item):
        """adds a new item to the list at position posn or raises a ValueError."""
        a = self.search(item)
        if a == True:
            return
        if posn == 0:
            tmp = Node(item)
            tmp.next = self.head
            self.head = tmp
        else:
            current = self.head
            index = 0
            while current.next is not None:
                if(index == posn-1):
                    tmp = Node(item)
                    tmp.next = current.next
                    current.next = tmp
                    return
                else:
                    current = current.next
                    index += 1
            if index == posn-1:
                current.next = Node(item)
            else:
                raise ValueError("posn is out of bounds")
    
    def union(self, set1, set2):
        set3 = LinkedListSet()
        set1temp = LinkedListSet()
        set2temp = LinkedListSet()
        current = set1.head
        
        while current is not None:
            set1temp.append(current.data)
            current = current.next
        current = set2.head
        while current is not None:
            set2temp.append(current.data)
            current = current.next
        
        for i in range(0,set1temp.size()):
            b = set1temp.pop()
            set3.add(b)
        for i in range(0,set2temp.size()):
            a = set2temp.pop() 
            if set3.search(a) == False:
                set3.add(a)
        return set3

    def intersection(self, set1, set2):
        set3 = LinkedListSet()
        set1temp = LinkedListSet()
        set2temp = LinkedListSet()
        
        current = set1.head
        while current is not None:
            set1temp.append(current.data)
            current = current.next
        current = set2.head
        while current is not None:
            set2temp.append(current.data)
            current = current.next
        
        for i in range(0,set1temp.size()):
            a = set1temp.pop() 
            if set2temp.search(a) == True:
                set3.add(a)
        return set3

    def difference(self, set1, set2):
        set3 = LinkedListSet()
        set1temp = LinkedListSet()
        set2temp = LinkedListSet()
        
        current = set1.head
        while current is not None:
            set1temp.append(current.data)
            current = current.next
        current = set2.head
        while current is not None:
            set2temp.append(current.data)
            current = current.next
                
        for i in range(0,set1.size()):
            a = set1temp.pop()
            if set2temp.search(a) == False:
                set3.add(a)


        return set3
