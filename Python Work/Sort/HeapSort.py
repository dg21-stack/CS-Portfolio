import random 
from BinaryHeap import BH

def heapSort(arr):
    binaryHeap = BH(len(arr))
    for values in arr:
        binaryHeap.insert(values,"Min")
    arr = []
    while binaryHeap.sizeOf() != 0: 
        arr.append(binaryHeap.popRoot("Min"))
    return arr

__name__ = "__main__"

arr = random.sample(range(10,100),10)
print(arr)
print(heapSort(arr))
