# Calculate the absolute diff between the sum of the diagonal of a square matrix

def findDiff(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0

    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n-1-i]
    result = abs(primary_sum-secondary_sum)
    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

result = findDiff(matrix)
print("Difference between the sums of the diagonals:", result)