# Given an array arr of size n−1 that contains distinct integers in the range of 1 to n (inclusive), find the missing element. The array is a permutation of size n with one element missing. Return the missing element.

# Examples:
# Input: n = 5, arr[] = [1,2,3,5]
# Output: 4
# Explanation : All the numbers from 1 to 5 are present except 4.

class Solution:
    def missing_number(self,arr,n):
        #calculate total sum
        total_sum = n*(n+1)/2
        arr_sum = sum(arr)

        missing_no = int(total_sum  - arr_sum)

        return (missing_no)
    
n=5
arr = [1,2,4,5]

# Create an instance of the Solution class
sol = Solution()

print(sol.missing_number(arr,n))