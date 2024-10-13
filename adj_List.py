#Adjacency List representation of a undirected graph

input = [[0,1], [0,2], [0,3], [0,4], [1,3], [2,3], [2,4], [2,5], [3,5]]
n = 6 # represents the number of nodes

list = {}

for i in range(6):
    list[i] = []

for (u,v ) in input:
    list[u].append(v)
    list[v].append(u)
    
for item in list.items():
    print(item)