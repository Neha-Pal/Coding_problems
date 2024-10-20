# how to find connected component in an Undirected Graph.

edges = [['A','B'],['A','C'],['A','D'],['D','E'],['B','E'],['F','H'],['F','G'],['I','J'],['K']]
nodes = ['A','B','C','D','E','F','G','H','I','J','K']

def DFS(graph, node, visited):
    visited.add(node)
    sm = 1
    
    for child in graph[node]:
        if child not in visited:
            sm += DFS(graph, child, visited)
    return sm

graph = {}
for key in nodes:
    graph[key] = []

for edge in edges:
    if len(edge) ==2:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)

visited = set()
ans = []
for node in nodes:
    if node not in visited:
        temp = DFS(graph, node, visited)
        ans.append(temp)
print(ans)