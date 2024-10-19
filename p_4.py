# You are given a 3-digit number n, Find whether it is an Armstrong number or not.

# An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371. 

# Note: Return "true" if it is an Armstrong number else return "false".

# Examples

# Input: n = 153
# Output: true
# Explanation: 153 is an Armstrong number since 1^3 + 5^3 + 3^3 = 153. Hence answer is "true".
import math
class Solution:
    def findAmstrong(self, N):
        n_str = str(N)
        total_digits = len(n_str)

        sum_digits = 0

        for digit in n_str:
            sum_digits += int(digit) ** total_digits

        if sum_digits == N:
            return True
        else:
            return False
        
sol = Solution()
N = 153
print(sol.findAmstrong(N))