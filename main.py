# from math import factorial,sqrt,ceil #gcd
# from itertools import permutations,combinations,combinations_with_replacement
# from collections import deque,Counter
# from bisect import bisect_left
# from heapq import heapify,,heappush,heappop
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from fractions import gcd
# from string import ascii_lowercase # ascii_lowercase は "abcdefghijklmnopqrstuvwxyz"

# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# from numba import njit, b1, i1, i4, i8, f8
# import numpy as np    # np.lcm(),np.gcd()
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb,perm #permはnPk
# import networkx as nx
# G = Graph()

import sys
sys.setrecursionlimit(10 ** 6)

MOD = 10**9 + 7
INF = float("INF")
S = input()
N = int(input())
N, M = list(map(int, input().split()))
lisA = list(map(int, input().split()))
# arrA = np.array(input().split(),dtype=np.int64)
# pow(n,-1,mod) # 逆元求めるやつ

ans = "test"
print(ans)
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
