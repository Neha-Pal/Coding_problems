# Given an array arr of positive integers and another number target. Determine whether two elements exist in arr whose sum is exactly target or not. Return a boolean value true if two elements exist in arr else return false.

# Examples:

# Input: arr[] = [1, 4, 45, 6, 10, 8], target =16
# Output: true
# Explanation: arr[3] + arr[4] = 6 + 10 = 16
# Input: arr[] = [1, 2, 4, 3, 6], target = 11
# Output: false
# Explanation: None of the pair makes a sum of 11

class Solution():
    def pairSum(self, arr, target):
        seen = set()

        for num in arr:
            complement = target - num
            if complement in seen:
                return True
            seen.add(num)
        return False
sol = Solution()
arr = [1, 4, 45, 6, 10, 8]
target = 16

print(sol.pairSum(arr, target))