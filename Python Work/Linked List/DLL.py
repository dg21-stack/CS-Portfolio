#Doubly Linked List 
import time
import random

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:    
    def __init__(self):
        self.head = None 
        self.tail = None 

    def __iter__(self):
        node = self.head 
        while node:
            yield node 
            node = node.next
    
    def create(self, val):
        node = Node(val)
        node.prev = None 
        node.next = None
        self.head = node
        self.tail = node

    def append(self,val):
        node = Node(val)
        if self.head == None:
            return 'empty DLL'
        else: 
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            
            
    def insert(self, loc, val):
        node = Node(val)
        if self.head == None:
            return 'empty DLL'
        else:
            if loc == 0:
                temp = self.head
                temp.prev = node
                node.next = temp
                self.head = node
                return
            else:
                if loc == 1:
                    temp = self.head 
                    node.next = self.head.next
                    a = self.head.next
                    node.prev = temp
                    temp.next = node
                    a.prev = node
                    return 
                temp = self.head
                i = 1
                while i < loc: 
                    temp = temp.next 
                    i+=1
                if temp.next is None:
                    self.tail.next = node
                    node.prev = temp
                    self.tail = node
                    node.next = None 
                    return
                else:
                    node.next = temp.next
                    node.prev = temp
                    temp.next.prev = node
                    temp.next = node
                    return 

    def removeVal(self,val):
        if self.head == None:
            return 'nothin in DLL'
        else:
            cursor = self.head
            if self.head.value == val:
                self.head = self.head.next 
            else:
                while cursor is not None:
                    if cursor.value == val:
                       tmp = cursor.prev
                       tmp1 = cursor.next
                       tmp1.prev = tmp
                       tmp.next = tmp1 
                       return
                    cursor = cursor.next

    def clear(self):
        if self.head == None:
            return 'already empty'
        else:
            self.head = None
            self.tail = None
                    
                
#test 
__name__ = "__main__"

DLL = DoublyLinkedList()
DLL.create(5)
n = []
start = time.process_time()
for i in range(0, 100): 
    DLL.insert(i,i)
print("time taken:", time.process_time() - start)
n.append(time.process_time() - start)
DLL.clear()
DLL.create(5)
start = time.process_time()
for i in range(0, 1000):
   DLL.insert(i,i)
print("time taken:", time.process_time() - start)
n.append(time.process_time() - start)
DLL.clear()
DLL.create(5)
start = time.process_time()
for i in range(0, 10000):  
    DLL.insert(i,i)
print("time taken:", time.process_time() - start)
n.append(time.process_time() - start)
DLL.clear()
print(n)






                    


