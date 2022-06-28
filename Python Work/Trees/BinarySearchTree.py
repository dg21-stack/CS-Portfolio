# left subtree the value of node is less than or equal to its paret node's value
# right subtree the value of a node is greater than its parent node's value 

# binary search tree implementation 

class BinaryNode:
    def __init__(self,value : int):
        self.value = value
        self.left = None 
        self.right = None

class BSTree: 
    def __init__(self):
        self.root = None 

    # insert
        
    def insertNode(self, val : int):
        if self.root is None:
            node = BinaryNode(val)
            self.root = node
        else:
            temp = self.root
            node = BinaryNode(val)
            while temp:
                if temp.value < val:
                    if temp.right is None:
                        temp.right = node  
                        break
                    else:
                        temp = temp.right
                elif temp.value > val:
                    if temp.left is None:
                        temp.left = node 
                        break
                    else:
                        temp = temp.left 

    # delete node 

    def delete(self,root, val : int):
        if root is None:
            return 
        elif root.value > val:
            root.left = self.delete(root.left,val) 
        elif root.value < val:
            root.right = self.delete(root.right, val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min = self.findMin(root.left)
                self.delete(root, min.value)
                root.value = min.value 
        return root 
    
    # find minimum for deletion in worst case 

    def findMin(self, node):
        if node.right is None:
            return node
        else:
            node = self.findMin(node.right)
            return node

    # delete entire tree 

    def deleteEntire(self):
        self.root.left = None 
        self.root.right = None 
        self.root = None  
    
    # pre order traverse

    def printPreOrder(self,root, val = 0):
        if not root:
            return 
        print(" " * val, root.value)  
        self.printPreOrder(root.left, val + 1)
        self.printPreOrder(root.right, val + 1)
    
    # post order traverse 

    def printPostOrder(self, root, val = 0):
        if not root:
            return 
        self.printPostOrder(root.left, val + 1)
        self.printPostOrder(root.right, val + 1)
        print(" " * val, root.value)
    # in order traverse 

    def printInOrder(self,root, val = 0):
        if not root:
            return 
        self.printInOrder(root.left, val + 1)
        print(" " * val, root.value)
        self.printInOrder(root.right, val + 1)

# test 

__name__ = "__main__"

bn = BSTree()

bn.insertNode(15)
bn.insertNode(20)
bn.insertNode(13)
bn.insertNode(14)
bn.insertNode(12)

bn.delete(bn.root,13)
bn.delete(bn.root,14)
bn.printInOrder(bn.root)
print()
bn.printPreOrder(bn.root)
print()
bn.printPostOrder(bn.root)
