from numpy import true_divide

#repetitive case: reverse the string
#base case1: the original string is equal to the reversed return true
#else: return false
def isPalindrome(strng):
    if len(strng)==1:
        return True
    elif strng[0] != strng[len(strng)-1]:
        return False
    else:
        return isPalindrome(strng[1:len(strng)-1])
          
print(isPalindrome('tacocat'))