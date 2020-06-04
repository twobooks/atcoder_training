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

# import numpy as np    # numpy.lcm()
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb,perm #permはnPk
# import networkx as nx
# G = Graph()

N,M,K = map(int,input().split())

for X in range(0,N+1):
    for L in range(0,M+1):
        if X*(M-L)+L*(N-X) == K:
            print("Yes")
            exit()

print("No")
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
