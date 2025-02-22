# Factorial without Multiplication & Division
# Problem
# You are given a positive integer N. Your task is to compute the factorial of N without using any multiplication (*) or division (/) operators.

# Example
# Input
# 3
# 0
# 1
# 5

# Output
# 1
# 1
# 120

# Explanation
# In the first test case, the factorial of 0 is 1.
# In the second test case, the factorial of 1 is 1.
# In the third test case, the factorial of 5 is 120.

# Note
# The factorial of a non-negative integer N, denoted by N!, is the product of all positive integers less than or equal to N. Mathematically, it is represented as follows:
# N!=N×(N−1)×(N−2)×...×1.

# Constraints
# 1 ≤ T ≤ 10
# 0 ≤ N ≤ 12
# Hints
# Hint 1
# You can use recursion to solve this problem.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input())
for _ in range(num):
    n = int(input())
    print(factorial(n))