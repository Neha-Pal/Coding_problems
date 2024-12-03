# Take a = 4 X 4 matrix and b = 4 X 1 matrix and perform the multiplication of a and b (a X b) without any
# library.

# Define matrices
A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

B = [
    [1],
    [2],
    [3],
    [4]
]
result = [[0] for _ in range(len(A))]

for i in range(len(A)): 
    for j in range(len(B)): 
        result[i][0] += A[i][j] * B[j][0]

print(result)
