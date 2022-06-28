
import sys
sys.setrecursionlimit(10000)

def factorial(n):
    # assertion case
    assert n >=0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0,1]:
        # base case
        return 1
    else:
        # recursive case
        return n*factorial(n-1)

print(factorial(4))