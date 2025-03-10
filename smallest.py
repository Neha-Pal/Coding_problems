# Problem Statement: Given an array, we have to find the smallest element in the array.
# Example 1:
# Input: arr[] = {2,5,1,3,0};
# Output: 0
# Explanation: 0 is the smallest element in the array.

def findSmallest(arr):
    arr.sort()
    return arr[0]

arr = list(map(int, input().split()))
print(findSmallest(arr))