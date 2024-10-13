#Depth-first-search using adjacency list

input = [[0,1], [0,2], [0,3], [0,4], [1,3], [2,3], [2,4], [2,5], [3,5]]
n = 6 # represents the number of nodes

def DFS(graph, node, visited = set()):
    print(node)
    visited.add(node)

    for child in graph[node]:
        if child not in visited:
            DFS(graph, child, visited)

graph = {}

for i in range(6):
    graph[i] = []

for (u, v) in input:
    graph[u].append(v)
    graph[v].append(u)

DFS(graph, 1)