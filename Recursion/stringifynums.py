def stringifyNumbers(obj):
    # TODO
    if isinstance(obj, int):
        return str(obj)
    if isinstance(obj,dict):
        for i in obj:
           
            if isinstance(obj[i],int) and str(obj[i]) != 'True':
                obj[i] = stringifyNumbers(obj[i])
            if isinstance(obj[i],dict):
                stringifyNumbers(obj[i])
        
    return obj

obj2 = {
  'num':1,
  'test':[],
  'data': {'val':4,'info':{'isRight':True, 'random':'66'}}
}

print(stringifyNumbers(obj2))