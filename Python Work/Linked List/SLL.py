#Singly Linked List 


class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class singleLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None: 
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: 
                newNode.next = self.head
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location -1:
                    tempNode = tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def traverse(self):
        if self.head is None:
            print("SLL is empty")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def indexOf(self,value):
        if self.head is None:
            return "SLL is empty"
        else:
            ind = 0
            node = self.head
            while node is not None:
                if node.value == value:
                    return ind
                node = node.next
                ind+=1
            if node is None:
                return 'val not in SLL'
    
    def removeVal(self,value):
        if self.head is None:
            return "SLL is empty"
        else:
            if self.head.value == value:
                self.head = self.head.next
            else:
                prevnode = self.head
                node = prevnode.next
                while node is not None:
                    if node.value == value and node.next is not None:
                        prevnode.next = node.next
                        return
                    elif node.value == value and node.next is None:
                        prevnode.next = None    
                        return 
                    node = node.next
                    prevnode = prevnode.next
                return "value not in SLL"
                
            
    def deleteAll(self):
        if self.head is None:
            return "SLL is empty"
        else:
            self.head = None
            self.tail = None

                    
        
#tests 


singlyLinkedList = singleLinkedList()
node1 = Node(1)
node2 = Node(2)
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)
singlyLinkedList.insertSLL(5,1)
singlyLinkedList.insertSLL(6,1)
a  = singlyLinkedList.indexOf(4)

singlyLinkedList.removeVal(6)

singlyLinkedList.deleteAll()
print([node.value for node in singlyLinkedList])

