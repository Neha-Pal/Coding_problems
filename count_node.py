# Problem statement
# Return the number of undirected graphs that can be formed using 'N' vertices, allowing for disconnected components within the graph. Self-edges and multiple edges are not allowed.



# For Example:
# For N = 2,
# Count is 2.
# Consider the vertices to be ‘A’ and ‘B’.
# These are the possible 2 graphs.  

from typing import *
def countGraph(N):
    n_edges = (N*(N-1))//2
    return 2** n_edges

N = 2
print(countGraph(N))
