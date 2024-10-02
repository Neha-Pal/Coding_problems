# Given a sorted array containing only 0s and 1s, find the transition point, i.e., the first index where 1 was observed, and before that, only 0 was observed.

# Example 1:

# Input:
# N = 5
# arr[] = {0,0,0,1,1}
# Output: 3
# Explanation: index 3 is the transition 
# point where 1 begins.

class Solution():
    def findTransition(self,arr):
        for i in range(len(arr)):
            if arr[i] == 1:
                return i
        return -1
        
sol=Solution()
arr=[1,1]
print(sol.findTransition(arr))