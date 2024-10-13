# Adjacency Matrix representation of a undirected-graph

input = [[0,1], [0,2], [0,3], [0,4], [1,3], [2,3], [2,4], [2,5], [3,5]]
n = 6 # represents the number of nodes
matrix = [] #empty list that will hold the adjacency matrix

#creating nXn matrix
for i in range(6):
    temp = []
    for j in range(6):
        temp.append(0)
    matrix.append(temp)

#as it is undirected so the edeges are bi-directional
for (u,v) in input:
    matrix[u][v]= 1
    matrix[v][u] = 1

for item in matrix:
    print(item)
