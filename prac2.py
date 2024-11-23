#prime or not
import math
def isPrime(n):
    if n < 2:
        return "not prime"
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
             return "not Prime"
        return "Prime"
        
n = 45
print(isPrime(n))
