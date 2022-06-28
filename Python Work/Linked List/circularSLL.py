#circular Singly Linked List 

class Node:
    def __init__(self, value = None):
        self.value = value 
        self.next = None

class circularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break

            node = node.next
    
    def createSLL(self, nodeval):
        node = Node(nodeval)
        node.next = node
        self.head = node
        self.tail = node
        return 'the CSLL created'

    def append(self, val):
        if self.head is None:
            return 'empty SLL'
        else:
            node = Node(val)
            self.tail.next = node
            node.next = self.head
            self.tail = node

    def insert(self,loc, val):
        node = Node(val)
        if self.head is None:
            return 'empty SLL'
        else:
            if loc == 0:
                temp = self.head 
                node.next = temp
                self.head = node 
                self.tail.next = node
            else:
                tempNode = self.head.next
                prevNode = self.head
                i = 1
                while prevNode.next is not self.head:
                    if i == loc:
                        node.next = tempNode
                        prevNode.next = node
                       
                        return 'inserted at position: ' + str(loc)
                    tempNode = tempNode.next 
                    prevNode = prevNode.next
                    i+=1   
                temp = prevNode
                node.next = self.head
                self.tail = node
                prevNode.next = node

    def traverse(self):
        if self.head is None:
            return 'empty CSLL'
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next
                if temp == self.tail.next:
                    break
    
    def delete(self,value):
        if self.head is None:
            return 'empty CSLL'
        else:
            if self.head.value == value:
                self.head = self.head.next
                self.tail.next = self.head
            else:
                prev = self.head
                temp = prev.next
                while temp:
                    if temp.value == value:
                        prev.next = temp.next
                    prev = prev.next 
                    temp = temp.next 
                    if temp == self.tail.next:
                        break

    def clear(self):
        if self.head is None:
            return 'already empty'
        else:
            self.head = None
            self.tail = self.head
                    


                
#tests 
__name__ = "__main__"         

sll = circularSLL()
sll.createSLL(1)
sll.append(3)
sll.append(5)
sll.insert(2,4)
sll.insert(0,0)
sll.insert(1,2)
sll.insert(1,3)
sll.insert(2,2)
print([node.value for node in sll])
sll.delete(3)
sll.delete(0)
print([node.value for node in sll])
sll.traverse()
        