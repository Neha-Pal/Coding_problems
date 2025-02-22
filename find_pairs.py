# Count Pairs divisible by 2
# You are given an array arr of length N. You have to calculate the count of pairs in an array such that the sum of pairs is divisible by 2.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of two lines of input.
# The first line of each test case contain N, length of array arr.
# The second line consist of the array arr.

# Output Format
# For each test case, output on a new line the number of divisible pairs.
# Input - 
# 3
# 4
# 6 1 2 3
# 6
# 2 2 1 7 5 3
# 2
# 4 8
# Output -
# 2
# 7
# 1

def find_pairs(arr):
    odd_count = 0
    even_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    even_pairs = (even_count * (even_count - 1)) // 2
    odd_pairs = (odd_count * (odd_count - 1)) // 2
    return even_pairs + odd_pairs

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_pairs(arr))
