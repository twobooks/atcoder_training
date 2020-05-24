# from math import factorial,sqrt,ceil #,gcd
# from itertools import permutations,combinations,combinations_with_replacement
# from collections import deque,Counter
# from bisect import bisect_left
# from heapq import heappush,heappop
# from numba import njit
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from fractions import gcd

# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb,perm #permはnPk
# import networkx as nx
# G = Graph()

# slist = "abcdefghijklmnopqrstuvwxyz"
MOD = 10**9 + 7
N,M,Q = map(int,input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)
node_colors = [0] + list(map(int,input().split()))
querys = [list(map(int,input().split())) for _ in range(Q)]

for i in range(Q):
    qcode = querys[i][0]
    node_num = querys[i][1]
    print(node_colors[node_num])
    if qcode==1:
        for j in G[node_num]:
            node_colors[j] = node_colors[node_num]
    else:
        node_colors[node_num] = querys[i][2]
