# binary heap implementation

class BH:
    def __init__(self, size):
        self.list = [None] * (size + 1)
        self.maxSize = size + 1
        self.size = 0

    # peek at the root 

    def peek(self):
        if not self:
            return 
        else:
            return self.list[1]

    # get the size of heap 

    def sizeOf(self):
        return self.size
    
    # traverse the heap

    def levelOrderTraverse(self):
        if not self:
            return 
        else:
            for i in range(1, self.size + 1):
                print(self.list[i])
    
    # insert a node

    def insert(self, val, type = "Max"):
        if self.list[1] is None:
            self.list[self.size + 1] = val 
            self.size += 1
            
        else:
            self.size += 1
            self.list[self.size] = val 
            self.heapify(self.size, type)

    # heapify the heap after insertion

    def heapify(self,index,type):
        parent = int( index / 2 )
        if parent < 1:
            return 
        elif type == "Min":
            if self.list[parent] > self.list[index]:
                temp = self.list[parent]
                self.list[parent] = self.list[index]
                self.list[index] = temp
            self.heapify(parent, type)
        else:
            if self.list[parent] < self.list[index]:
                temp = self.list[parent]
                self.list[parent] = self.list[index]
                self.list[index] = temp 
            self.heapify(parent, type)

    # reheapify heap after the deletion

    def reheapify(self, index, type):
        child1 = index * 2
        child2 = index * 2 + 1
        if child1 > self.size:
            return
        elif child1 == self.size:
            if type == "Min":
                if self.list[index] > self.list[child1]:
                    temp = self.list[child1]
                    self.list[child1] = self.list[index]
                    self.list[index] = temp
                return 
            else:
                if self.list[index] < self.list[child1]:
                    temp = self.list[child1]
                    self.list[child1] = self.list[index]
                    self.list[index] = temp
                return 
        else:
            if type == "Min":
                if self.list[child1] < self.list[child2]:
                    min = child1
                else:
                    min = child2
                if self.list[index] > self.list[min]:
                    temp = self.list[min]
                    self.list[min] = self.list[index]
                    self.list[index] = temp 
                self.reheapify(min, type)
            else:
                if self.list[child1] > self.list[child2]:
                    max = child1
                else:
                    max = child2
                if self.list[index] < self.list[max]:
                    temp = self.list[max]
                    self.list[max] = self.list[index]
                    self.list[index] = temp
                self.reheapify(max, type)

    # get the root of Heap

    def popRoot(self,type = "Max"):
        if self.list[1] is None:
            return
        else:
           temp = self.list[1]
           self.list[1] = self.list[self.size]
           self.list[self.size] = None 
           self.size -=1
           self.reheapify(1,type)
           return temp 
        
    # delete heap

    def deleteFull(self):
        self.list = None 
        self.size = 0


# test
__name__ = "__main__"

# Heap = BH(5) 
# print(Heap.peek())
# Heap.insert(4)
# Heap.insert(5)
# Heap.insert(2)
# Heap.insert(1)
# Heap.levelOrderTraverse()
# Heap.popRoot()
# Heap.levelOrderTraverse()
# Heap.deleteFull()
# Heap.levelOrderTraverse()