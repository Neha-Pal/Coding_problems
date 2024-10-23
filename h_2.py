# Given an array od integers, find the sum of its elements.
# for example-  arr = [1,2,3]. then it will return 6(1+2+3 = 6)

def findSum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

arr = [1,2,3]
print(findSum(arr))