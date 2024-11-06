import math
def checkPrime(n:int)->int:
    if n <= 1:
        return 'NO'
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return 'NO'
    return 'YES'

n = 4
print(checkPrime(n))