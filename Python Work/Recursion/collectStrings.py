def collectStrings(obj):
    # TODO
    if isinstance(obj, str):
        return obj
    elif isinstance(obj,dict):
        a = []
        for i in obj:
            if isinstance(obj[i], str):
                a.append(collectStrings(obj[i]))
            elif isinstance(obj[i],dict):
                a += collectStrings(obj[i])
        return a

obj2 = {
  "stuff":'foo',
  "data":{
    "val":{
        "thing":
        {"info":"bar","moreInfo":{
            "evenMoreInfo": {
                "weMadeIt": "baz"
            }
        }}
    }
  }
}
print(collectStrings(obj2))