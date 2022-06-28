def capitalizeWords(arr): 
    if isinstance(arr,str):
        print(arr)
        return arr.upper()
    for i in range(len(arr)):
        if arr[i] != arr[i].upper():
            
            arr[i] = capitalizeWords(arr[i])
            print(arr[i])
    
   
    
    return arr
            
print(capitalizeWords(['i','am','learning','recursion']))