import random

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    a = mergeSort(arr[:len(arr)//2]) 
    b = mergeSort(arr[len(arr)//2:])
    arr = []
    i = 0 
    j = 0 
    lastA = False
    lastB = False
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            if j < len(b) - 1:
                arr.append(b[j])
                j+=1
            elif j == len(b) - 1:
                if lastB == False:
                    arr.append(b[j])
                    lastB = True
                arr.append(a[i])
                i+=1
        else:
            if i < len(a) - 1:
                arr.append(a[i])
                i+=1
            elif i == len(a) -1:
                if lastA == False:
                    arr.append(a[i])
                    lastA = True
                arr.append(b[j])
                j+=1
    return arr

__name__ = "__main__"

arr = random.sample(range(10,100),10)
print(arr)
print(mergeSort(arr))