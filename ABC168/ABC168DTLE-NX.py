# from math import factorial,sqrt,ceil #,gcd
# from itertools import permutations,combinations,combinations_with_replacement
# from collections import deque,Counter
# import re
# from bisect import bisect_left
# from heapq import heappush,heappop
# from numba import njit
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from fractions import gcd

# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
from networkx import Graph,shortest_path,single_target_shortest_path,astar_path
G = Graph()
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb,perm #permはnPk

# slist = "abcdefghijklmnopqrstuvwxyz"
N,M = map(int,input().split())

# G.add_nodes_from(list(range(1,N+1)))
for _ in range(M):
    A,B = map(int,input().split())
    G.add_edge(A, B)

# shortestPath = shortest_path(G,target=1)
shortestPath = single_target_shortest_path(G,target=1)
# shortestPath = astar_path(G,target=1)
# print(shortestPath)
if len(shortestPath) != N:
    print("No")
    exit()

print("Yes")
for i in range(2,N+1):
    print(shortestPath[i][1])

# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
