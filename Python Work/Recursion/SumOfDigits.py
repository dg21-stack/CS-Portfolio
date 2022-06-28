# how to find the sum of digits of a positive integer number using recursion?

def sumofDigits(n):
    assert n>=0, "Only positive ints allowed"
    if len(str(n)) == 1:
        return n
    else:
        print(int(n/10), int(n%10))
        return sumofDigits(int(n/10)) + n%10

print(sumofDigits(5643))