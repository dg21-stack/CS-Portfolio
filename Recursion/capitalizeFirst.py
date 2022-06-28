def capitalizeFirst(arr):
    i = 0
    if isinstance(arr,str):
        print(arr)
        arr = arr.replace(arr[0][0], arr[0][0].upper())
        print(arr)
        return arr
    if isinstance(arr,str) == False:
        print(arr)
        while i< len(arr):
            if arr[i][0] == arr[i][0].upper():
                print(arr[i][0])
                i+=1
            else:
                
                arr[i] = capitalizeFirst(arr[i]) 
                print(arr)
                i+=1
         

    return arr



print(capitalizeFirst(['car','taco','banana']))