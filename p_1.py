# Given an array arr, find the average or mean of the prefix array at every index.

# Example 1:

# Input: arr[] = [10, 20, 30, 40, 50]
# Output: [10, 15, 20, 25, 30] 
# Explanation: 10 / 1 = 10, (10 + 20) / 2 = 15, (10 + 20 + 30) / 3 = 20 and so on.
# Input: arr[] = [12, 2]
# Output: [12, 7] 


class Solution():
    def AvgPrefix(self, arr):

        result = []
        n = len(arr)
        prefix_sum = 0
         
        for i in range(n):
            prefix_sum += arr[i]
            avg = (prefix_sum) // (i+1)

            result.append(avg)
        return result
sol = Solution()
arr = [10, 20, 30, 40, 50]
print(sol.AvgPrefix(arr))