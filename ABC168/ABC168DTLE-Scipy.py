import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
# from scipy.special import comb,perm #permはnPk

N,M = map(int,input().split())
length = N

i = [] #頂点(始点)
j = [] #頂点(終点)
d = [] #頂点間の距離
for _ in range(M):
    A,B = map(int,input().split())
    i.append(A-1)
    j.append(B-1)
    d.append(1)

graph = csr_matrix((d, (i, j)), shape=(N, N)) # 頂点i,jはゼロスタートである必要ある

#返り値は各頂点間の距離の値を含んだ隣接行列(float64型のnp.array)
dist,pred = dijkstra(graph, directed=False,indices=0,return_predecessors=True,unweighted=True)

pred = pred + 1
print("Yes")
print(*pred[1:],sep="\n")