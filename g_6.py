# Given a sorted array arr and an integer k, find the position(0-based indexing) at which k is present in the array using binary search.

# Examples:

# Input: k = 4, arr= [1, 2, 3, 4, 5]  
# Output: 3
# Explanation: 4 appears at index 3.


class Solution:
    def binarySearch(self, arr, k):
        h = len(arr) - 1
        l = 0
        while(l<=h):
            mid = (l+h) // 2

            if arr[mid] == k:
                return mid
            if arr[mid] < k:
                l = mid+1
            else:
                h = mid-1

        return -1
    
k = 4
arr = [2,3,4,6,8]
sol = Solution()
print(sol.binarySearch(arr,k))