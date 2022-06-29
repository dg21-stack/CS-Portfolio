import random 

def insertSort(arr):
    for i in range(1,len(arr)):
        k = i 
        min = arr[i]
        while k > 0:
            if min < arr[k-1]:
                temp = arr[k-1]
                arr[k-1] = arr[k]
                arr[k] = temp
            k-=1
    return arr

__name__ = "__main__"

arr = random.sample(range(10,100),10)
print(arr)
print(insertSort(arr))

