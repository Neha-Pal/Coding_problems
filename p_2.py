# Given an array arr[] of integers, your task is to determine the number of subarrays where the minimum and maximum elements are equal.

# Examples:

# Input: arr[] = [1, 1, 3]
# Output: 4
# Explanation: 
# The subarrays where the minimum and maximum elements are the same are: (1), (1), (3) and (1, 1) 

class Solution:
    def countSubArray(self, arr):
        n = len(arr)
        total_subarrays = 0
        count = 1  # To track the length of contiguous identical elements

        for i in range(1, n):
            if arr[i] == arr[i - 1]:
                count += 1  # Continue the contiguous segment
            else:
                # When the segment ends, count the subarrays for the current segment
                total_subarrays += (count * (count + 1)) // 2
                count = 1  # Reset the count for the new segment

        # Handle the last segment
        total_subarrays += (count * (count + 1)) // 2

        return total_subarrays


# Test the function
sol = Solution()
arr = [1, 1, 3]
print('Total subarray - ' + str(sol.countSubArray(arr)))  # Output: 4

