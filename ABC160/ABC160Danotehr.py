# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

import numpy as np
from scipy.sparse.csgraph._shortest_path import dijkstra, floyd_warshall, bellman_ford, johnson, shortest_path
from scipy.sparse import csr_matrix

# strlist = "abcdefghijklmnopqrstuvwxyz"
n,x,y = map(int,input().split())

length = n
d = [1 for _ in range(n)]
i = list(range(0,n-1)) + [x-1]
j = list(range(1,n)) + [y-1]
# print(d,i,j,sep="\n")

graph = csr_matrix((d, (i, j)), shape=(n, n)) # 頂点i,jはゼロスタートである必要ある
# print(type(csr),csr,sep="\n")

#返り値は各頂点間の距離の値を含んだ隣接行列(float64型のnp.array)
dist = dijkstra(graph, directed=False).astype(int)
# dist = shortest_path(graph, directed=False).astype(int)
# print(type(dist),dist,sep="\n")

dist = dist.ravel() #配列の一次元化
# print(type(dist),dist,sep="\n")

ans = np.bincount(dist, minlength=n) // 2  #bincountは[0の個数,1の個数,2の個数…nの個数]を返す
# print(type(ans),ans,sep="\n")

print(*ans[1:], sep='\n')