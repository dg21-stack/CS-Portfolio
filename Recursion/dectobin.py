
def dectobin(x):
    assert int(x) == x and x > 0, 'positive integer needed'
    if x in [0,1]:
        return str(x)
    return dectobin(int(x/2)) + str(x%2)

print(dectobin(13))