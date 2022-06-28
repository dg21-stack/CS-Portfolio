# circular Doubly Linked List
import time

class Node:
     def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class circDLL:
    def __init__(self):
        self.head = None
        self.tail = None 

    def __iter__(self):
        node = self.head
        while node:
            yield node 
            node = node.next 
            if node == self.tail.next:
                break 
    
    def create(self, val):
        node = Node(val)
        self.head = node 
        self.tail = node 
        node.next = node
        node.prev = node

    def append(self, val):
        node = Node(val)
        if self.head == None:
            return 'empty'
        else: 
            self.tail.next = node
            node.prev = self.tail
            node.next = self.head
            self.tail = node

    def insert(self, loc, val):
        node = Node(val)
        if self.head == None:
            return 'empty'
        else:
            if loc == 0:
                node.next = self.head
                node.prev = self.tail 
                self.head.prev = node 
                self.tail.next = node
                self.head = node
            else:
                tmp = self.head 
                i = 0
                while i < loc - 1: 
                    tmp = tmp.next 
                    i+=1               
                node.next = tmp
                node.prev = tmp.prev
                tmp.prev.next = node 
                tmp.prev = node
                return 

    def removeVal(self, val):
        if self.head == None:
            return 'already empty'
        else:
            if self.head.value == val: 
                temp = self.head.next
                self.tail.next = temp 
                self.head = temp 
                temp.prev = self.tail              
            else:
                tmp = self.head                
                while tmp:
                    if tmp.value == val:
                        tmp.prev.next = tmp.next 
                        tmp.next.prev = tmp.prev
                        if self.tail == tmp:
                            self.tail = tmp.prev                        
                        return 
                    tmp = tmp.next
                    if tmp == self.head:
                        break                
                return "value doesn't exist"

    def clear(self):
        if self.head == None:
            return 'already empty'
        else:
            self.head = None
            self.tail = None

#tests  

__name__ = "__main__"            
                
dll = circDLL()
dll.create(3)
n = []
start = time.process_time()
for i in range(0, 100):   
    dll.insert(i,i)
print("time taken:", time.process_time() - start)
n.append(time.process_time() - start)
dll.clear()
dll.create(5)
start = time.process_time()
for i in range(0, 1000):   
    dll.insert(i,i)    
print("time taken:", time.process_time() - start)
n.append(time.process_time() - start)
dll.clear()
dll.create(5)
start = time.process_time()
for i in range(0, 10000):   
    dll.insert(i,i)
print("time taken:", time.process_time() - start)
n.append(time.process_time() - start)
print(n)
dll.clear()
dll.create(5)


