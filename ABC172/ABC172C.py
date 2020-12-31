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

import numpy as np    # numpy.lcm()
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb,perm #permはnPk
# import networkx as nx
# G = Graph()

# slist = "abcdefghijklmnopqrstuvwxyz"
MOD = 10**9 + 7
N,M,K = map(int,input().split())
# lisA = list(map(int,input().split()))
arrA = np.array([0] + list(map(int,input().split())))
arrB = np.array([0] + list(map(int,input().split())))

arrA = np.cumsum(arrA,dtype="int64")
arrB = np.cumsum(arrB,dtype="int64")

# memo = np.add.outer(arrA,arrB) <= K
j = M
ans = 0
for i in range(N+1):
    while j >= 0:
        if arrA[i]+arrB[j] <= K:
            ans = max(i+j,ans)
            break
        j -= 1

print(ans)
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
