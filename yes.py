# Here's the question based on the provided image:

# Question 1

# Write a program that extracts all unique prime numbers in the ascending order that can be found within the decimal representation of a given integer, N. The program should identify not only individual primes contained in the digits but also primes that can be formed by combining consecutive digits in the number. If there is no prime number found, print "No prime numbers found".

# Read the input from STDIN and write the output to STDOUT. You should not write arbitrary strings while reading the input and while printing as these contribute to the standard output.   

# Constraints: 1 <= N <= 10^8   

# Input Format:

# The only line of input should contain an integer N, an input number.

# Output Format:

# The output should display the list of integers (each separated by a single space) where each integer is a prime number found within the decimal representation of N. The primes in the list should be presented in increasing order. If there is no prime number found, print "No prime numbers found".

# Let me know if you'd like a solution to this question in a specific programming language.

import itertools

# Helper function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_number(n):
    str_n = str(n)
    primes = set()

    # Generate all substrings of the number
    for length in range(1, len(str_n) + 1):
        for i in range(len(str_n) - length + 1):
            substring = str_n[i:i + length]
            num = int(substring)
            if is_prime(num):
                primes.add(num)

    # Return sorted list of unique primes
    return sorted(primes)

# Main function
if __name__ == "__main__":
    # Read input
    n = int(input().strip())

    # Find primes in the number
    primes = find_primes_in_number(n)

    # Print the result
    if primes:
        print(" ".join(map(str, primes)))
    else:
        print("No prime numbers found")
