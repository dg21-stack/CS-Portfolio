import random 

def selectionSort(arr, val = 0):
    if arr == []:
       return arr
    min = arr[0]
    minindex = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            minindex = i
    temp = arr[minindex]
    arr[minindex] = arr[0]
    arr[0] = temp
    n = arr.pop(0)
    arr = [n] + selectionSort(arr) 
    return arr

__name__ = "__main__"

arr = random.sample(range(10,100),10)
print(arr)
print(selectionSort(arr))

    
    