def checkPalindrome(myString):
    s=myString [::-1]
    if s==myString:
        return True
    
    return False
myString=input()
print(checkPalindrome(myString))
