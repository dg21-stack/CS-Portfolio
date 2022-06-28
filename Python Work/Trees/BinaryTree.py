from Queue import LLQueue as queue

# Binary Node Implementation 

class BinaryNode:
    def __init__(self,value = None):
        self.value = value 
        self.left = None 
        self.right = None

# Functions for implementing and traversing Binary Tree 

# pre order traversal 
def preOrderTraverse(node):
    if not node:
        return
    print(node.value)
    preOrderTraverse(node.left)
    preOrderTraverse(node.right)

# in order traversal 

def inOrderTraverse(node, val = 0):
    if not node:
        return
    inOrderTraverse(node.left, val + 1)
    print(" " * val, node.value)
    inOrderTraverse(node.right, val+ 1)

# post order traversal

def postOrderTraverse(node, val = 0):
    if not node:
        return 
   
    postOrderTraverse(node.left, val + 1)
    postOrderTraverse(node.right,val + 1)
    print(" " * val, node.value)


# level order traversal

def levelOrderTraverse(node, val = 0):
    if not node:
        return 
    else:
        customQueue = queue()
        customQueue.createQueue(node)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.value)
            if (root.value.left is not None):
                if customQueue.isEmpty():
                    customQueue.createQueue(root.value.left)
                else:
                    customQueue.enqueue(root.value.left)
            if (root.value.right is not None):
                if customQueue.isEmpty():
                    customQueue.createQueue(root.value.right)
                else:
                    customQueue.enqueue(root.value.right)

# search for value using level order search

def levelOrderSearch(node,search):
    if not node:
        return False 
    else:
        customQueue = queue()
        customQueue.createQueue(node)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value == search:
                return True
            else: 
                if (root.value.left is not None):
                    if customQueue.isEmpty():
                        customQueue.createQueue(root.value.left)
                    else:
                        customQueue.enqueue(root.value.left)
                if (root.value.right is not None):
                    if customQueue.isEmpty():
                        customQueue.createQueue(root.value.right)
                    else:
                        customQueue.enqueue(root.value.right)
        return False

# insert value using level order traversal

def levelOrderInsert(node, value):
    if not node:
        return
    else:
        customQueue = queue()
        customQueue.createQueue(node)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.left is None:
                root.value.left = value 
                break
            elif root.value.right is None and root.value.left is not None:
                root.value.right = value
                break
            if (root.value.left is not None):
                        if customQueue.isEmpty():
                            customQueue.createQueue(root.value.left)
                        else:
                            customQueue.enqueue(root.value.left)
            if (root.value.right is not None):
                if customQueue.isEmpty():
                    customQueue.createQueue(root.value.right)
                else:
                    customQueue.enqueue(root.value.right)

# get deepest value 

def getDeepest(node):
    if not node:
        return 
    else: 
        customQueue = queue()
        customQueue.createQueue(node)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if (root.value.left is not None):
                        if customQueue.isEmpty():
                            customQueue.createQueue(root.value.left)
                        else:
                            customQueue.enqueue(root.value.left)
            if (root.value.right is not None):
                if customQueue.isEmpty():
                    customQueue.createQueue(root.value.right)
                else:
                    customQueue.enqueue(root.value.right)
        node = root.value 
        return node


# switch 

def switch(delNode,deepest):
    if not deepest or not delNode:
        return 
    else:
        temp = delNode.value
        delNode.value = deepest.value 
        deepest.value = temp
   

# delete Last 

def deleteLast(node, deepest):
    if not node:
        return
    else:
        customQueue = queue()
        customQueue.createQueue(node)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.left == deepest:
                root.value.left = None
                return
            elif root.value.right == deepest:
                root.value.right = None
                return 
            if (root.value.left is not None):
                        if customQueue.isEmpty():
                            customQueue.createQueue(root.value.left)
                        else:
                            customQueue.enqueue(root.value.left)
            if (root.value.right is not None):
                if customQueue.isEmpty():
                    customQueue.createQueue(root.value.right)
                else:
                    customQueue.enqueue(root.value.right)
        
            
# delete Node 

def deleteNode(node, delNode):
    if not node:
        return 
    else:
        deepest = getDeepest(node)
        switch(delNode,deepest)
        deleteLast(a,deepest)

# delete Tree

def deleteEntireTree(node):
    if not node:
        return 
    else:
        node.left = None 
        node.right = None
        node = None 

__name__ = "__main__"

a = BinaryNode("Rootdrinks")
c = BinaryNode("R0coffee")
b = BinaryNode("L0tea")
a.left=  b
a.right = c
d = BinaryNode("L1black")
b.left = d
b.right = BinaryNode("R1green")
d.left = BinaryNode("L2Earl Grey")
d.right = BinaryNode("R2Jasmine")
c.left = BinaryNode("L1Columbian")
c.right = BinaryNode("R1Italian")
new = BinaryNode('L2hello!')
levelOrderInsert(a,new)
print(levelOrderSearch(a,new))
inOrderTraverse(a)
deleteNode(a,b)
deleteNode(a,a)
print("-------")
postOrderTraverse(a)

            

