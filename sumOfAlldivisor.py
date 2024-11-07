# Problem statement
# You are given an integer ‘n’.



# Function ‘sumOfDivisors(n)’ is defined as the sum of all divisors of ‘n’.



# Find the sum of ‘sumOfDivisors(i)’ for all ‘i’ from 1 to ‘n’.



# Example:
# Input: ‘n’  = 5

# Output: 21

# Explanation:
# We need to find the sum of ‘sumOfDivisors(i)’ for all ‘i’ from 1 to 5. 
# ‘sumOfDivisors(1)’ = 1
# ‘sumOfDivisors(2)’ = 2 + 1 = 3
# ‘sumOfDivisors(3)’ = 3 + 1 = 4
# ‘sumOfDivisors(4)’ = 4 + 2 +1 = 7 
# ‘sumOfDivisors(5)’ = 5 + 1 = 6

def sumOfAllDivisor(n: int) -> int:
    total_sum = 0
    for i in range(1, n+1):
        divisor_sum = 0
        for j in range(1, i+1):
            if i % j == 0:
                divisor_sum += j
        total_sum += divisor_sum
    return total_sum

n = 5
print(sumOfAllDivisor(n))