# Problem Statement: Given an array, we have to find the largest element in the array.
# Example 1:
# Input:
#  arr[] = {2,5,1,3,0};
# Output:
#  5

def findLargest(arr):
    arr.sort()
    return arr[-1]

arr = list(map(int, input().split()))
print(findLargest(arr))