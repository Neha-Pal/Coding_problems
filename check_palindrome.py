def checkPalindrome(n):
    n = str(n)
    rev_num = n[::-1]
    if rev_num == n:
        return True
    else:
        return False
    
n = 123
print(checkPalindrome(n))
