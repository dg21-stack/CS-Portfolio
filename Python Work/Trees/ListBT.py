# List BT implementation

class LBinaryTree:
    def __init__(self, size):
        self.list = [None] * size 
        self.lastIndex = 1
        self.size = size 
    
    # add node 

    def addNode(self, val):
        if self.lastIndex == self.size:
            return 'full'
        self.list[self.lastIndex] = val
        self.lastIndex += 1
    
    # search for node 

    def searchNode(self, nodeVal):
        for i in range(len(self.list)):
            if self.list[i] == nodeVal:
                return 'exists'
        return 'not found'   

    # delete node 

    def deleteNode(self,val):
        if self.list[1] == None: 
            return 
        else:
            delIndex = self.list.index(val) 
            self.list[delIndex] = self.list[self.lastIndex-1]
            self.list[self.lastIndex-1] = None
            self.lastIndex -= 1 

    # pre order traversal 

    def preOrderTraverse(self, index): 
        if index > self.lastIndex:
            return 
        print(" " * index, self.list[index])
        self.preOrderTraverse(index * 2) 
        self.preOrderTraverse(index * 2 + 1)
    
    # in order traversal

    def inOrderTraverse(self, index):
        if index > self.lastIndex:
            return 
        self.preOrderTraverse(index * 2)
        print(" " * index, self.list[index])
        self.preOrderTraverse(index * 2 + 1)

    # post order traversal 

    def postOrderTraverse(self, index):
        if index > self.lastIndex:
            return 
        self.preOrderTraverse(index * 2)
        self.preOrderTraverse(index * 2 + 1)
        print(" " * index, self.list[index])

    # level order traversal 

    def levelOrderTraverse(self): 
        for i in range(1,self.lastIndex + 1):
            print(self.list[i]) 
    
    # delete tree 

    def deleteTree(self):
        self.list = None

__name___ = "__main__" 

tree = LBinaryTree(10)
tree.addNode(3) #1
tree.addNode(2) #2
tree.addNode(3) #3
tree.addNode(4)
tree.addNode(1)
print(tree.list)
#tree.deleteNode(2)
print(tree.searchNode('T'))
tree.preOrderTraverse(1)
print(tree.list)

    