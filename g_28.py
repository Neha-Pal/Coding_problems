# Given an array arr of only 0's and 1's. The array is sorted in such a manner that all the 1's are placed first and then they are followed by all the 0's. Find the count of all the 0's
# Examples:
# Input: arr[] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
# Output: 3
# Explanation: There are 3 0's in the given array.

class Solution():
    def countZeros(self, arr):
        count = 0
        for i in range(len(arr)):
            if arr[i] == 0:
                count += 1
        return count
sol = Solution()
arr = [1,1,1,1,1,1,0,0,0,0,0]
print(sol.countZeros(arr))