# Given an array arr containing only 0s, 1s, and 2s. Sort the array in ascending order.
# Input: arr[]= [0, 2, 1, 2, 0]
# Output: 0 0 1 2 2
# Explanation: 0s 1s and 2s are segregated into ascending order.

class Solution:
    def sort012(sekf, arr):
        arr.sort()
        return arr
    
sol = Solution()
n=5,
arr = [2,1,0,0,2]
print(sol.sort012(arr))