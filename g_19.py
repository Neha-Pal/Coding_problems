# Find Pair Given Difference
# Given an array arr[] of size n and an integer x, return 1 if there exists a pair of elements in the array whose absolute difference is x, otherwise, return -1.

# Example 1:

# Input:
# n = 6
# x = 78
# arr[] = {5, 20, 3, 2, 5, 80}
# Output:
# 1
# Explanation:
# Pair (2, 80) have absolute difference of 78.
# Example 2:

class Solution():
    def findPair(self, arr, n, x):
        seen = set()

        for i in range(n):
            if arr[i]-x in seen or arr[i]+x in seen:
                return 1
            seen.add(arr[i])
        return -1
sol=Solution()
n = 6
x = 78
arr= [5, 20, 3, 1, 5, 80]
print(sol.findPair(arr,n,x))