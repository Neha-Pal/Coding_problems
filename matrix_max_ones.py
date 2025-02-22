# Identify Row with Most 1
# Problem
# You are given a 2D matrix of size n×m consisting only of 0′s and 1′s. Your task is to determine the index of the row that contains the maximum number of 1′s. In the case of multiple rows having the same maximum count of 1′s, return the index of the first such row.

# Input Format
# The first line of input will contain a single integer T, denoting the number of test cases.
# Each test case consists of multiple lines of input.
# The first line contains two integers n and m, representing the number of rows and columns in the matrix, respectively.

# Output Format
# For each test case, output on a new line the index of the row with the maximum number of 1′s. If all rows contain only 0′s, output −1.

# Constraints
# 1 ≤ T ≤ 10
# 1 ≤ n, m ≤ 1000
# Example
# Input
# 3
# 3 4
# 0 1 0 0
# 1 1 0 0
# 0 0 0 1
# 4 4
# 1 1 1 0
# 0 1 1 0
# 0 1 1 1
# 1 1 1 1
# 2 1
# 0
# 0


# Output
# 1
# 3
# -1

def matrix_max_one(matrix, m, n):
    max_ones = 0
    row_index = -1
    for i in range(len(matrix)):
        count = matrix[i].count(1)
        if count > max_ones:
            max_ones = count
            row_index = i
    return row_index

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    result = matrix_max_one(matrix, m, n)
    print(result)
