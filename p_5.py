# You will be given an integer n, your task is to return the sum of all natural number less than or equal to n.

# As the answer could be very large, return answer modulo 109+7.

# Example 1:

# Input:
# n = 6
# Output:
# 21
# Explanation:
# 1+2+3+4+5+6 = 21

class Solution:
    def sumNatural(self, n):
        MOD = 10**9 + 7
        return ((n*(n+1))//2) % MOD
    
sol = Solution()
n=6
print(sol.sumNatural(n))