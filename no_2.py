# Write a Python program to check if a number is prime.

def checkPrime(num):
    if num <= 1:
        print("Prime")
        return
    
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print("Not Prime")
            return
        
    print("Prime")

num = 11
checkPrime(num)