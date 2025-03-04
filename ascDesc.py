# Problem Statement: Rearrange the array such that the first half is arranged in increasing order, and the second half is arranged in decreasing order
# Example 1:
# Input: 8 7 1 6 5 9
# Output: 1 5 6 9 8 7
# Explanation: First three elements are in the ascending order and next three elements are in the descending order.

def ascDesc(arr):
    arr.sort()
    n = len(arr)
    for i in range(0, n//2):
        print(arr[i], end = " ")
    for i in range(n-1, n//2-1, -1):
        print(arr[i], end = " ")

arr = list(map(int, input().split()))
ascDesc(arr)
