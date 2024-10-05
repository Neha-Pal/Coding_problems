# Given an array nums[], construct a Product Array nums[] such that nums[i] is equal to the product of all the elements of nums except nums[i].

# Examples:

# Input: nums[] = [10, 3, 5, 6, 2]
# Output: [180, 600, 360, 300, 900]
# Explanation: For i=0, P[i] = 3*5*6*2 = 180.
# For i=1, P[i] = 10*5*6*2 = 600.
# For i=2, P[i] = 10*3*6*2 = 360.
# For i=3, P[i] = 10*3*5*2 = 300.
# For i=4, P[i] = 10*3*5*6 = 900.

class Solution():
    def productExceptSelf(self,arr):
        n = len(arr)

        result = [1]*n
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= arr[i]
        
        right_product = 1

        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= arr[i]

        return result
sol = Solution()
arr = [10, 3, 5, 6, 2]
print(sol.productExceptSelf(arr))

