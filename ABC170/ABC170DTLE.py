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
N = int(input())
lisA = list(map(int,input().split()))

lisA.sort()

needcheck = set()
divable = set()
for i in range(N):
    if i == 0:
        needcheck.add(lisA[i])
        continue
    else:
        for num in needcheck:
            if lisA[i] % num == 0:
                divable.add(lisA[i])
                break
        else:
            needcheck.add(lisA[i])

ans = needcheck - divable
print(len(ans))
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
