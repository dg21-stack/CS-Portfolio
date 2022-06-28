def flatten(arr):
    values = 0
    while values < len(arr):
        if isinstance(arr[values], int):
            values+=1
        else: 
            arr = arr[:values] + flatten(arr[values]) + arr[values+1:]
           
          
         
    return arr
           
print(flatten([1, [2, [3, 4], [[5]]]]))
