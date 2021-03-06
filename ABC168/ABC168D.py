from networkx import Graph
from networkx.algorithms.traversal.breadth_first_search import bfs_predecessors
G = Graph()

N,M = map(int,input().split())
rows = [list(map(int,input().split())) for _ in range(M)]

G.add_edges_from(rows)

preds = dict(bfs_predecessors(G,source=1))

if len(preds)+1 != N:
    print("No")
    exit()

print("Yes")
for i in range(2,N+1):
    print(preds[i])