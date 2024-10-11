# Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

# Examples:

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: true
# Explanation: The given array is sorted.

class Solution():
    def sortedOrNot(self, arr)->bool:
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                return False
        return True
    
sol = Solution()
arr = [90,110,115,243]
print(sol.sortedOrNot(arr))
            
