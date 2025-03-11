# Problem Statement: Given an array, we have to find the sum of all the elements in the array.
# Example 1:
# Input: N = 5, array[] = {1,2,3,4,5}
# Output: 15
# Explanation: Sum of all the elements is 1+2+3+4+5 = 15

def findSum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

n = int(input())
arr = list(map(int, input().split()))
print(findSum(arr))