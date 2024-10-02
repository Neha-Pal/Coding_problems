# Given an array arr[], find the first repeating element. The element should occur more than once and the index of its first occurrence should be the smallest.

# Note:- The position you return should be according to 1-based indexing. 

# Examples:

# Input: arr[] = [1, 5, 3, 4, 3, 5, 6]
# Output: 2
# Explanation: 5 appears twice and its first appearance is at index 2 which is less than 3 whose first the occurring index is 3.
# Input: arr[] = [1, 2, 3, 4]
# Output: -1
# Explanation: All elements appear only once so answer is -1.
class Solution():
    def repeatedElement(self, arr):
        seen = set()
        repeated_index = -1

        for i in range(len(arr)-1, -1, -1):
            if arr[i] in seen:
                repeated_index = i+1
            seen.add(arr[i])
        return repeated_index
sol = Solution()
arr = [1, 5, 3, 4, 3, 5, 6]
print(sol.repeatedElement(arr))