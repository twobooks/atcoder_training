# from math import factorial,sqrt,ceil #gcd
# from itertools import permutations,combinations,combinations_with_replacement
# from collections import deque,Counter
# from bisect import bisect_left
# from heapq import heapify,,heappush,heappop
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from fractions import gcd
# ascii_lowercase は "abcdefghijklmnopqrstuvwxyz"
from string import ascii_lowercase

# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# from numba import njit
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
X = input()
N = int(input())
S = []
for _ in range(N):
    S.append(input())

alphaDict = {X[i]: ascii_lowercase[i] for i in range(26)}

ans = []
for sStr in S:
    tmp = sStr
    key = ""
    for c in tmp:
        key += alphaDict[c]
    ans.append((key, sStr))

ans.sort()
for key, val in ans:
    print(val)
