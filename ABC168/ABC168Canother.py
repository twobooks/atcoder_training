import math
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
# import networkx as nx
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb,perm #permはnPk

# slist = "abcdefghijklmnopqrstuvwxyz"
MOD = 10**9 + 7
A,B,H,M = map(int,input().split())

kakuH = 30 * H + 0.5 * M
kakuM = 6 * M

xH = A*math.cos(math.radians(kakuH))
yH = A*math.sin(math.radians(kakuH))
xM = B*math.cos(math.radians(kakuM))
yM = B*math.sin(math.radians(kakuM))

ans = (xH-xM)**2 + (yH-yM)**2
ans = math.sqrt(ans)
print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
