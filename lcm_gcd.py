# Given two integers a and b, write a function lcmAndGcd() to compute their LCM and GCD. The function inputs two integers a and b and returns a list containing their LCM and GCD.

# Examples:

# Input: a = 5 , b = 10
# Output: [10, 5]
# Explanation: LCM of 5 and 10 is 10, while their GCD is 5.
import math

def LcmGcd(a,b):
    gcd = math.gcd(a,b)

    lcm = abs(a*b) // gcd

    return [lcm, gcd]

a = 5
b = 10
print(LcmGcd(a, b))
