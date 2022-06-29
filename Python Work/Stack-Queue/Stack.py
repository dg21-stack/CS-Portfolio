class Node:
    def __init__(self, value = None):
        self.next = None 
        self.value = value
        self.prev = None

# List Stack, Not Bounded 

class LStack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse()
        return '\n'.join(values)
    
    def createStack(self, val):
        self.list = [val] 
       

    def push(self,val):
        self.list.append(val)
       

    def pop(self):
        if len(self.list)>1:
            return self.list.pop(len(self.list)-1)
        else:
            raise Exception("Stack underflow!")

    def peek(self):
         if len(self.list)>1:
            return self.list[len(self.list)-1] 
         else:
            raise Exception("Stack underflow!")

    def isEmpty(self):
        return True if len(self.list) == 0 else False

    def isFull(self):
        return 

    def deleteStack(self):
        self.list = []

 # List Stack Bounded 
   
class LStackCapped:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []
    

    def __str__(self):
        self.list.reverse()
        values = [str(x) for x in self.list]
        self.list.reverse()
        return '\n'.join(values)
     
    def createStack(self,val):
        self.list = [val]

    def isFull(self):
        return True if len(self.list) == self.maxSize else False 
    
    def isEmpty(self):
        return True if self.list == 0 else False
    
    def deleteStack(self):
        self.list = []
    
    def push(self, val):
        if len(self.list) == self.maxSize:
            raise Exception('Stack overflow!')
        else:
            self.list.append(val)
          
    
    def pop(self):
        if len(self.list) >= 1:
            poppable = self.list[len(self.list)-1]
            self.list = self.list[:len(self.list)-1]
            return poppable
        else:
            raise Exception("Stack underflow!")

    def peek(self):
        if len(self.list) >= 1:
            print(self.list[len(self.list)-1])
        else:
            raise Exception("Stack underflow!")

# Linked List Stack Unbounded 

class LLStack():

    def __init__(self):
        self.head = None 
        self.tail = None 

    def __str__(self):
        a = []
        curr = self.head
        while curr:
            a.append(curr.value)
            curr= curr.next
        a.reverse()
        values = [str(x) for x in a]
        return '\n'.join(values) 

    def createStack(self,val):
        node = Node(val)
        self.head = node
        self.tail = self.head
        node.prev = None 
        node.next = None
    
    def push(self,val):
        node = Node(val)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node 
    
    def pop(self):
        value = self.tail.value
        if self.tail.prev is not None:
            self.tail = self.tail.prev 
            self.tail.next = None
        return value
    
    def peek(self):
        print(str(self.tail.value))

    def isEmpty(self):
        return True if self.head is None else False

    def deleteStack(self):
        self.head = None 
        self.tail = None
        
# testing 

stack1 = LStack()

stack1.createStack(3)
stack1.push(4)
stack1.push(5)
print(stack1.pop())
print()
stack1.peek()
print(stack1)
stack1.deleteStack()
print()
stack2 = LStackCapped(5)
stack2.createStack(3)
stack2.push(4)
stack2.push(6)
stack2.push(12)
stack2.push(4)
print(stack2)
print()
print(stack2.pop())
print()
stack2.push(2)
print(stack2)
print()
print(stack2.pop())

stack2.peek()
print()
stack3 = LLStack()
stack3.createStack(3)
stack3.push(4)
stack3.push(6)
# stack3.peek()
print(stack3,'\n')
stack3.pop()
stack3.push(14)
print(stack3)


