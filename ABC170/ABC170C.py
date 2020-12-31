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

# slist = "abcdefghijklmnopqrstuvwxyz"
X,N = map(int,input().split())
lisP = list(map(int,input().split()))

tmp = 1000
ans = 1000
for p in range(-120,121):
    if p in lisP:
        continue
    num = abs(X-p)
    if num == tmp:
        ans = min(ans,p)
    elif num < tmp:
        tmp = num
        ans = p

print(ans)
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
