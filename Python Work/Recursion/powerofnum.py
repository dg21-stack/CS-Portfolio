
def powerofnum(x,n):
    assert int(n) == n, "Needs to be int"
    if n == 0:
        return 1
    if n == 1:
        return x
    elif n < 0:
        return 1/x * powerofnum(x,n+1)
    else:
        return x * powerofnum(x,n-1)
    
print(powerofnum(4,-3))