# from math import factorial,sqrt,ceil #,gcd
# from itertools import permutations,combinations,combinations_with_replacement
from collections import deque,Counter
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

kv1 = Counter(lisA[0:N:2]).most_common()
kv2 = Counter(lisA[1:N:2]).most_common()

if len(kv1)==len(kv2)==1 and kv1[0]==kv2[0]:
    print(N//2)
    exit()

ans1 = N
ans2 = N
for i in range(0,N//2-1):
    try:
        if kv1[0][0]!=kv2[i][0]:
            ans1 = min(ans1,N-(kv1[0][1]+kv2[i][1]))
        if kv1[i][0]!=kv2[0][0]:
            ans2 = min(ans2,N-(kv1[i][1]+kv2[0][1]))
    except:
        pass

print(min(ans1,ans2))
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
