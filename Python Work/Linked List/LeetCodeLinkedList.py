# Implementation of Linked List Leet Code problem 
# node class 

class Node:
    def __init__(self,value =None):
        self.next = None 
        self.value = value

# linked list class

class MyLinkedList:

    def __init__(self):
        self.head = None 
        self.tail = None 
        
    def __iter__(self):   
        node = self.head
        while node:
            yield node
            node = node.next       

    def length(self):
        res = 0
        node = self.head
        while node:
            node = node.next 
        return res 

    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current:
            if count == index:
                if current.value == None:
                    return -1
                return current.value 
            count += 1
            current = current.next
        return -1
        
    def addAtHead(self, val: int) -> None:
        if self.head is None:
            node = Node(val)
            self.head = node
            self.tail = self.head   
        else:
            node = Node(val)
            node.next = self.head 
            self.head = node
                
    def addAtTail(self, val: int) -> None:
        
        current = self.head
        node = Node(val)
        if current is None:
            self.head = node 
            self.tail = self.head
        else:
            while current.next:
                current = current.next 
            current.next = node
            self.tail = current.next
            
    def addAtIndex(self, index: int, val: int) -> None:
        node = Node(val)
        if index == 0:
            self.addAtHead(val)
        else:
            i = 0
            t = self.head
            while t:
                if i == index - 1:
                    node.next = t.next
                    t.next = node
                    return
                t = t.next 
                i+=1

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return 'empty'
        else:
            if index == 0:
                t = self.head 
                self.head = self.head.next 
                t = None
            else:
                i = 0 
                t = self.head
                tn = t.next
                while tn:
                    if tn.next is not None and i is index - 1:
                        t.next  = tn.next 
                        tn = None
                        return 
                    elif tn.next is None and i is index-1:
                        t.next = None
                        self.tail = t
                        return  
                    t = t.next
                    tn = tn.next
                    i+=1
                   
