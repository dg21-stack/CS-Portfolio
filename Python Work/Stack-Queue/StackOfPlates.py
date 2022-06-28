
# Stack of Plates Problem: A person can only carry n number of plates before they crash down. Implement a Stack with this in mind so that there
# is a set number of plates a person can carry before making a new stack 

class Node:

    def __init__(self,value = None):
        self.next = None 
        self.prev = None 
        self.value = value

# set of stacks implementation 

class SetOfStacks:

    def __init__(self,maxPlates):
        self.maxPlates = maxPlates 
        self.list = [[]]
        self.head = None 
        self.tail = None 
        self.stack = 0

    # to string 

    def __str__(self):
        a = [[]]
        for i in range(0,len(self.list)):
            a[i] = [str(x.value) for x in self.list[i]]
            a.append([])
        string = "\t  Stack:\n\t========\t\n\t|   "
        for values in a:
            string += ("\t|\n\t|   ").join(values)
            string += "\t|\n\t========\n\t|   "
        string+="\t|"
        return string
    
    # create the stack 

    def createStacks(self,val):
        node = Node(val)
        self.head = node
        self.tail = node 
        node.next = None 
        node.prev = None 
        self.list[self.stack] = [node]
       
    # push onto the stack

    def push(self, val):
        if self.maxPlates == len(self.list[self.stack]):
            self.stack+= 1
            self.list.append([])
        node = Node(val)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node 
        self.list[self.stack].append(node)
    
    # pop from the stack

    def pop(self):
        if len(self.list[self.stack]) == 1:
            self.list = self.list[:self.stack]
            if self.stack != 0:
                self.stack-=1
        else:
            self.list[self.stack].pop(len(self.list[self.stack])-1)
        node = self.tail.value
        self.tail = self.tail.prev 
        return node


__name__ = "__main__"   

# tests

stack = SetOfStacks(4)
stack.createStacks(1)
for i in range(0,10):
    stack.push(i)
print(stack)
for i in range(0,11):
    print(stack.pop())
print()
print(stack)
