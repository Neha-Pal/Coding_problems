# Given a sorted array arr[] of size n without duplicates, and given a value x. Floor of x is defined as the largest element k in arr[] such that k is smaller than or equal to x. Find the index of k(0-based indexing).

# Examples

# Input: n = 7, x = 0 arr[] = {1,2,8,10,11,12,19}
# Output: -1
# Explanation: No element less than 0 is found. So output is "-1".
# Input: n = 7, x = 5 arr[] = {1,2,8,10,11,12,19}
# Output: 1
# Explanation: Largest Number less than 5 is 2 (i.e k = 2), whose index is 1(0-based indexing).

class Solution():
    def findFloor(self, arr, n, x):
        l=0
        h=n-1
        floor_index=-1

        while l<=h:
            mid = (l+h)//2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                floor_index = mid
                l = mid+1
            else:
                h = mid-1
        return floor_index
n=7
x=5
arr=[1,2,8,10,11,12,19]

sol = Solution()

print(sol.findFloor(arr, n, x))
            