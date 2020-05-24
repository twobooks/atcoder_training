import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix
# from scipy.special import comb,perm #permはnPk

N,M = map(int,input().split())
length = N

d = [1 for _ in range(M)]
arr = np.array([list(map(int,input().split())) for _ in range(M)])
arr = arr.T - 1
graph = csr_matrix((d, (arr[0], arr[1])), shape=(N, N)) # 頂点i,jはゼロスタートである必要ある

#返り値は各頂点間の距離の値を含んだ隣接行列(float64型のnp.array)
dist,pred = dijkstra(graph, directed=False,indices=0,return_predecessors=True,unweighted=True)

pred = pred + 1
print("Yes")
print(*pred[1:],sep="\n")