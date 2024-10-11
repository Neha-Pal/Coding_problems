# Given an integer array arr, return all the unique pairs [arr[i], arr[j]] such that i != j and arr[i] + arr[j] == 0.

# Note: The pairs must be returned in sorted order, the solution array should also be sorted, and the answer must not contain any duplicate pairs.

# Examples:

# Input: arr = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, 1]]
# Explanation: arr[0] + arr[2] = (-1)+ 1 = 0.
# arr[2] + arr[4] = 1 + (-1) = 0.
# The distinct triplets are [-1,1].
# Input: arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
# Output: [[-6, 6],[-1, 1]]
# Explanation: The distinct triplets are [-1, 1] and [-6, 6].

class Solution():
    def dPairs(self,arr):
        arr.sort()
        seen = set(arr)
        result = []

        for n1 in arr:      
            n2 = 0 - n1
            if n2 in seen and n1 < n2:
                result.append((n1, n2))

        return sorted(result)
    
sol = Solution()
arr = [6, 1, 8, 0, 4, -9, -1, -10, -6, -5]
print(sol.dPairs(arr))
