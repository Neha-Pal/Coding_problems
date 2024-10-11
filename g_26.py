# Given an array Arr consisting of N distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.
 
# Example 1:

# Input: 
# N = 4 
# arr[] = {1, 5, 3, 2}
# Output: 2 
# Explanation: There are 2 triplets:
#  1 + 2 = 3 and 3 +2 = 5

class Solution():
    def countTriplets(self, arr):
        count = 0
        arr.sort()

        for i in range(len(arr)):
            seen = set()
            for j in range(i):
                required_sum = arr[i] - arr[j]
                if required_sum in seen:
                    count += 1
                seen.add(arr[j])
        return count
sol = Solution()
arr = [1, 5, 3, 2]
print(sol.countTriplets(arr))