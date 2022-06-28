# queue implementation for use in trees
# node class

class Node:
    def __init__(self, value= None):
        self.next = None 
        self.value = value 

# list queue 

class LQueue: 
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def createQueue(self,val):
        self.list = [val]
    
    def enqueue(self,val):
        self.list.append(val)
    
    def dequeue(self):
        if len(self.list)>1:
            deq = self.list[0]
            self.list = self.list[1:]
            return deq
        elif len(self.list) == 1:
            deq = self.list[0]
            return deq
        else:
            raise Exception('queue is empty')
        
    
    def peek(self):
        if len(self.list) > 0:
            print(self.list[0])
        else:
            raise Exception('queue is empty')
    
    def isEmpty(self):
        return True if self.list == [] else False
    
    def deleteQueue(self):
        self.list = []

# List Queue Bounded 

class LQueueCapped: 
    def __init__(self, maxSize):
        self.list = []
        self.maxSize = maxSize

    def __str__(self):
        values = [str(x) for x in self.list]
        return "\n".join(values)
        
    def createQueue(self, val):
        self.list = [val]
    
    def enqueue(self, val):
        if len(self.list) < self.maxSize:
            self.list.append(val)
        else:
            raise Exception('queue full')
    
    def dequeue(self):
        if len(self.list)>1:
            deq = self.list[0]
            self.list = self.list[1:]
            return deq
        elif len(self.list) == 1:
            deq = self.list[0]
            return deq
        else:
            raise Exception('queue is empty')
            
    def peek(self):
        if len(self.list) > 0:
            print(self.list[0])
        else:
            raise Exception('queue is empty')
    
    def isEmpty(self):
        return True if len(self.list) == 0 else False 
    
    def isFull(self):
        return True if len(self.list) == self.maxSize else False
    
    def deleteQueue(self):
        self.list = []

# linked list queue 

class LLQueue:
    def __init__(self):
        self.head = None 
        self.tail = None

    def __str__(self):
        a = []
        curr = self.head 
        while curr:
            a.append(curr.value)
            curr = curr.next 
        values = [str(x) for x in a]
        return "\n".join(values)

    def createQueue(self, val):
        node = Node(val)
        self.head = node
        self.tail = node
        
    
    def enqueue(self, val):
        node = Node(val)
        self.tail.next = node 
        self.tail = node

    def dequeue(self):
        val = self.head 
        self.head = self.head.next 
        return val
    
    def peek(self):
        print(self.head.value)
    
    def isEmpty(self):
        return True if self.head is None else False 
    
    def deleteQueue(self):
        self.head = None 
        self.Tail = None





