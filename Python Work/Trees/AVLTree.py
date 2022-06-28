from Queue import LLQueue as queue

# AVL Node Class 

class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    # in order traversal 
       
    def printInOrder(self,root, val = 0):
            if not root:
                return 
            self.printInOrder(root.left, val + 1)
            print(" " * val, root.value)
            self.printInOrder(root.right, val + 1)
    
    # pre order traversal 

    def printPreOrder(self,root, val = 0):
            if not root:
                return 
            print(" " * val, root.value)  
            self.printPreOrder(root.left, val + 1)
            self.printPreOrder(root.right, val + 1)

    # post order traversal 

    def printPostOrder(self, root, val = 0):
            if not root:
                return 
            self.printPostOrder(root.left, val + 1)
            self.printPostOrder(root.right, val + 1)
            print(" " * val, root.value)

# Functions for AVL Tree Implementation: 

# search for node in AVL Tree

def search(root, value):
    if root is None:
        return
    if root.value == value:
        return root
    elif root.value > value and root.left is not None:
        if root.left.value == value:
            return root.left
        else:
            root = search(root.left, value)
            return root
    elif root.value < value and root.right is not None:
        if root.right.value == value:
            return root.right 
        else:
            root = search(root.right, value) 
            return root

# Rotate Right 

def rotateRight(disbalancedNode):
    new = disbalancedNode.left 
    disbalancedNode.left = disbalancedNode.left.right 
    new.right = disbalancedNode
    return new

# Rotate Left 

def rotateLeft(disbalancedNode):
    new = disbalancedNode.right
    disbalancedNode.right = disbalancedNode.right.left 
    new.left = disbalancedNode
    return new

# Check if node is unbalanced 

def checkUnbalance(node, isbalanced = True):
    if node is None:
        return 0, isbalanced, 0
    left_height, isbalanced, difference =  checkUnbalance(node.left)
    right_height, isbalanced, difference = checkUnbalance(node.right)
    if abs(left_height - right_height) > 1:
        isbalanced = False 
    return max(left_height, right_height) + 1, isbalanced, left_height - right_height

# Global rotate function: test the balance, test which way it balances in, check which way to rotate

def rotate(node): 
    if node is None:
        return 
    node.left =  rotate(node.left)
    node.right = rotate(node.right)
    if checkUnbalance(node)[1]:
        return node   
    if checkUnbalance(node)[2] > 1:
        if checkUnbalance(node.left)[2] < 0 and checkUnbalance(node.left)[1] is False:
            if node.left.left is not None:
                node.left = rotateLeft(node.left)
        node = rotateRight(node)  
    elif checkUnbalance(node)[2] < -1:
        if checkUnbalance(node.right)[2] > 0 and checkUnbalance(node.right)[1] is False:
            if node.right.left is not None:
                node.right = rotateRight(node.right)
        node = rotateLeft(node)
    return node

# Insert function for placing nodes in Tree and rotating

def insert(root,value): 
    if root is None:
        return 
    else:
        node = AVLNode(value) 
        h = 1
        orig = root
        while root:
            if value > root.value:
                if root.right is None:
                    root.right = node 
                    h+=1 
                    root.right.height = h 
                    break
                else:
                    root = root.right 
                    h+=1
            elif value < root.value: 
                if root.left is None: 
                    root.left = node 
                    h +=1 
                    root.left.height = h
                    break
                else:
                    root = root.left
                    h+=1 
        root = orig
        root = rotate(root)
        return root

# delete node and rotate 
       
def deleteNode(root, value):
    if root is None:
        return root
    elif root.value < value:
        root.right = deleteNode(root.right, value)
    elif root.value > value:
        root.left = deleteNode(root.left, value)
    else:
        if root.left is None and root.right is None:
            return None
        if root.right is None:
            return root.left 
        if root.left is None:
            return root.right
        else:
            min = findMin(root.left)
            deleteNode(root, min.value)
            root.value = min.value
            root = rotate(root) 
    return root  

# find min in node

def findMin(node):
    if node.right is None:
        return node
    else:
        node = findMin(node.right)
        return node

# remove the duplicate node 

def removeDupe(node,orig): 
    if node.right is None:
        return node 
    elif node.right is orig:
        node.right = None 
        return 
    else:
        node = removeDupe(node.right,orig)
        return node
        
# test
  
__name__ == "__main__"

tempAVL = AVLNode(11)
tempAVL = insert(tempAVL, 9)
tempAVL = insert(tempAVL, 12)
tempAVL = insert(tempAVL,10)
tempAVL = insert(tempAVL, 7)
tempAVL =insert(tempAVL, 5)
tempAVL = insert(tempAVL,13)
tempAVL = insert(tempAVL, 14)
tempAVL = insert(tempAVL, 4)
tempAVL = insert(tempAVL, 8)
print('inorder')
tempAVL.printInOrder(tempAVL)
print('postorder')
tempAVL.printPostOrder(tempAVL)
print('preorder')
tempAVL.printPreOrder(tempAVL)

deleteNode(tempAVL, 9)
deleteNode(tempAVL, 11)
deleteNode(tempAVL, 13)

tempAVL.printPreOrder(tempAVL)



