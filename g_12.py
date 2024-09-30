# Given a positive integer n, find the nth fibonacci number. Since the answer can be very large, return the answer modulo 1000000007.

# Note: for the reference of this question take first fibonacci number to be 1.

# Examples :

# Input: n = 2
# Output: 1 
# Explanation: 1 is the 2nd number of fibonacci series.
# Input: n = 5
# Output: 5
# Explanation: 5 is the 5th number of fibonacci series.

class Solution:
    def nthfibonacii(self, n:int)->int:
        if n==0:
            return 0
        if n==1:
            return 1
        a=1
        b=1
        MOD = 1000000007
        for i in range(3, n+1):
            a, b = b, (a+b)%MOD
        return b
n = 5
sol = Solution()
print(sol.nthfibonacii(n))