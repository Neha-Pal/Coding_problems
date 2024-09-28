# Given an array arr of non-negative numbers. The task is to find the first equilibrium point in an array. The equilibrium point in an array is an index (or position) such that the sum of all elements before that index is the same as the sum of elements after it.

# Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists. 

# Examples:

# Input: arr[] = [1, 3, 5, 2, 2]
# Output: 3 
# Explanation: The equilibrium point is at position 3 as the sum of elements before it (1+3) = sum of elements after it (2+2). 

class Solution:
    def equilibriumPoint(self, arr):
        total_sum = sum(arr)
        left_sum = 0
        for i in range(len(arr)):
            right_sum = total_sum - left_sum - arr[i]
            if left_sum == right_sum:
                return i+1
            left_sum += arr[i]
        return -1
    
sol = Solution()
arr = [1, 3, 5, 2, 2]
print(sol.equilibriumPoint(arr))

    