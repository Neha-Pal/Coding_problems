# Given a number N, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number. Return 1 if the number is Perfect otherwise return 0.

# Example 1:

# Input:
# N = 6
# Output:
# 1 
# Explanation:
# Factors of 6 are 1, 2, 3 and 6.
# Excluding 6 their sum is 6 which
# is equal to N itself. So, it's a
# Perfect Number.

import math
class Solution:
    def isPerfect(self, N):
        if N<2:
            return 0
        
        sum_of_factors = 1

        for i in range(2, int(math.sqrt(N))+1):
            if N % i == 0:
                sum_of_factors += i
            
                if i != N//i:
                    sum_of_factors += N // 2

        if sum_of_factors == N:
            return 1
        else:
            return 0
        
sol = Solution()
N = 6
print(sol.isPerfect(N))