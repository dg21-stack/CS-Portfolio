import random

class Node:
    def __init__(self, value = None):
        self.next = None
        self.prev = None
        self.value = value 
    def __str__(self):
        return str(self.value) 

# linked list class

class LinkedList:
    def __init__(self, value = None):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        curNode = self.head 
        while curNode:
            yield curNode 
            curNode = curNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ','.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result +=1 
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node
            
        else:
            node = Node(value)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        return self.tail

    def removeDup(self):
        if self.head is None:
            return
        else:
            s = []
            t = self.head
            while t:
                if t.value in s:
                    
                    temp = t.prev 
                    if  t.next == None:
                        temp.next = t.next 
                    else:
                        temp.next = t.next 
                        t.next.prev = temp 
                else:
                    s.append(t.value)
                    
                t = t.next
           
    def generate(self,n, min_val, max_val):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(random.randint(min_val,max_val))
    
# functions implementing linked list as well as tests

__name__ = "__main__"

LL = LinkedList()
LL.generate(30,0,1)
print(LL)
print(len(LL))

# 1 remove duplicates 

LL.generate(30,0,9)
print(LL)
LL.removeDup()
print(LL)

# 2 Nth to Last 

def returnNth(i,LL):
    a = LL.tail
    while i>0:
        if a is None:
            return None
        a = a.prev 
        i-=1
    return a

print(returnNth(6,LL))
LL = LinkedList()
LL.add(11)
LL.add(14)
LL.add(3)
LL.add(9)
LL.add(1)
LL.add(3)
LL.add(14)
LL.add(10)
LL.add(8)
LL.add(25)
LL.add(9)
LL.add(5)

# 3 partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x

def partition(x,LL):
    a = LL.head
    a = a.next 
    print(a)
    while a:
        if a.value < x:
                node = Node(a.value)
                LL.head.prev = node
                node.next = LL.head
                LL.head = node
                if a != LL.tail:
                    a.prev.next = a.next
                    a.next.prev = a.prev
                else: 
                    LL.tail = LL.tail.prev
                    LL.tail.next = None           
        a = a.next     
    return LL
         
print(partition(11,LL))

# 4 Sum Linked Lists

list1 = LinkedList()
list1.add(7)
list1.add(1)
list1.add(6)
list2 = LinkedList() 
list2.add(5)
list2.add(9)
list2.add(2)

def sumLists(list1,list2):
    a = list1.head
    b = list2.head
    extra = 0
    string = ''
    while a and b:
        n = str(a.value + b.value + extra)
        if len(n) > 1:
            string =  str(n)[1] + string 
            extra = 0
            extra+= int(str(a.value+b.value)[0])
        else:
            extra = 0
            string = str(n) + string
        a = a.next 
        b = b.next 
    return string 

print(sumLists(list1,list2))
    
# 5 determine if intersecting

inter = LinkedList()
inter1 = LinkedList()
inter.add(3)
inter1.add(2)
inter.add(1) 
inter1.add(4)
inter.add(5) 
inter1.add(6)
inter.add(9)
a = inter.head
b = inter1.head 
while a is not inter.tail:
    a = a.next 
while b is not inter1.tail:
    b = b.next 
inter2 = LinkedList()
inter2.add(7)
inter2.add(2)
inter2.add(1)
a.next = inter2.head
b.next = inter2.head
inter1.tail = inter2.tail
inter.tail = inter2.tail
# inter.add(7) 
# inter.add(2)
# inter.add(1)
# inter1.add(7)
# inter1.add(2)
# inter1.add(1)
print(inter1,inter)

def intersect(inter1,inter2):
    a = inter1.head
    b = inter2.head
    if len(inter1) > len(inter2):
        while b:
            a = inter1.head
            while a: 
                if a == b:
                    return True
                a = a.next 
            b = b.next 
    else:
        while a:
            b = inter2.head
            while b:
                if a == b:
                    return True
                
                b = b.next 
            a = a.next 
    return False

print(intersect(inter,inter1))