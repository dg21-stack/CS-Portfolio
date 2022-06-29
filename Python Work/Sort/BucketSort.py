import math
from InsertionSort import insertSort
import random 

def bucketSort(arr):
    bucketNum = round(math.sqrt(len(arr)))
    max = 0
    a = []
    for values in arr:
        if max < values:
            max = values 
    for i in range(bucketNum): 
        a.append([])
    for j in arr:
        appropbuck = math.ceil(j * bucketNum / max)
        a[appropbuck-1].append(j)
    j = []
    for i in range(len(a)):
        j += insertSort(a[i])
    return j

__name__ = "__main__"

arr = random.sample(range(10,100),10)
print(arr)
print(bucketSort(arr))