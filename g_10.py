# Given a non-negative integer n. The task is to check if it is a power of 2. 

# Examples

# Input: n = 8
# Output: true
# Explanation: 8 is equal to 2 raised to 3 (23 = 8).
# Input: n = 98
# Output: false

class Solution:
    def isPowerOf2(self, n:int)->bool:
        if n<=0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
    
n=20
sol = Solution()
print(sol.isPowerOf2(n))