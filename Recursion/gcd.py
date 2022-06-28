
def gcd(x,n):
    assert int(x) == x and int(n) == n, "needs to be int"
    if x < 0:
        x*=-1
    if n<0:
        n*=-1
    if n == 0: 
        return x
    else:
        return gcd(n,x%n) 

print(gcd(148,108))