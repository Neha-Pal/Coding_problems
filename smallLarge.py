# Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.
# Example 1:
# Input:
#  [1,2,4,7,7,5]
# Output:
#  Second Smallest : 2
# 	Second Largest : 5

def findSecondSmall(arr):
    arr.sort()
    if len(arr) < 2:
        return -1
    return arr[1]

def findSecondLargest(arr):
    arr.sort()
    if len(arr) < 2:
        return -1
    return arr[-2]

arr = list(map(int, input().split()))
print("Second Smallest :", findSecondSmall(arr))
print("Second Largest :", findSecondLargest(arr))