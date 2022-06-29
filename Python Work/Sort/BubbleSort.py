import random 

def bubbleSort(arr):
    if len(arr) == 0:
        return arr
    i = 0
    t = False
    while i < len(arr) - 1:
        if arr[i] > arr[i+1]:
            temp = arr[i+1]
            arr[i+1] = arr[i]
            arr[i] = temp 
            t = True 
        i+=1 
    if t == True:
        arr = bubbleSort(arr[:i]) + arr[i:]
    return arr 

__name__ = "__main__"

arr = random.sample(range(10,100),10)
print(arr)
arr = bubbleSort(arr)
print(arr)


