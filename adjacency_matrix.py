def adj_matrix(n, edges):
    matrix = [[0]*n for _ in range(n)]

    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1


    return matrix


input = [[0,1], [0,2], [0,3], [0,4], [1,3], [2,3], [2,4], [2,5], [3,5]]
n = 6 
matrix = adj_matrix(n, input)

for item in matrix:
    print(item)
