# A string str is given to represent a positive number. The task is to round str to the nearest multiple of 10.  If you have two multiples equally apart from str, choose the smallest element among them.

# Examples:

# Input: str = 29 
# Output: 30
# Explanation: Close multiples are 20 and 30, and 30 is the nearest to 29. 
# Input: str = 15
# Output: 10
# Explanation: 10 and 20 are equally distant multiples from 20. The smallest of the two is 10.

class Solution:
    def nearestMul10(self, n):
        value = n % 10

        if value <= 5:
            return n - value
        else:
            return n + (10- value)
        
sol = Solution()
n = 21
print(sol.nearestMul10(n))