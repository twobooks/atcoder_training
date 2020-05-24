from networkx import Graph,predecessor
G = Graph()

N,M = map(int,input().split())
rows = [list(map(int,input().split())) for _ in range(M)]

G.add_edges_from(rows)

preds = predecessor(G,source=1)

if len(preds) != N:
    print("No")
    exit()

print("Yes")
for i in range(2,N+1):
    print(preds[i][0])