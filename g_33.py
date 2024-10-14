# Given two unsorted arrays arr1[]  and arr2[], the task is to find all pairs whose sum equals x from both arrays.

# Note: All pairs should be returned in increasing order of u. For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then (u1,v1) should be returned first else second.

# Examples:

# Input: x = 9, arr1[] = [1, 2, 4, 5, 7], arr2[] = [5, 6, 3, 4, 8]
# Output: 
# 1 8
# 4 5 
# 5 4
# Explanation: (1, 8), (4, 5), (5, 4) are the pairs which sum to 9.
# Input: x = 8, arr1[] = [-1, -2, 4, -6, 5, 7], arr2[] = [6, 3, 4, 0]
# Output:
# 4 4 
# 5 3

class Solution:
    def allPairs(self, x, arr1, arr2):
        # Use a set for quick lookup of elements in arr2
        seen_2 = set(arr2)
        result = []
        
        for num1 in arr1:
            num2 = x - num1
            if num2 in seen_2:
                result.append((num1, num2))
        return sorted(result)

# Example usage
sol = Solution()
arr1 = [1, 2, 4, 5, 7]
arr2 = [5, 6, 3, 4, 8]
x = 9

output = sol.allPairs(x, arr1, arr2)
print(output)
