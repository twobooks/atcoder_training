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

import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb,perm #permはnPk
# import networkx as nx
# G = Graph()

N = int(input())
que = deque()
for _ in range(N):
    que.append(input())

if N == 1:
    print(*que)
    exit()

# print(cnt,div2combs,mod2nums)
ans = [0]*N
left = 0
right = N-1
while len(que) > 0:  
    top = set(que.popleft())
    if len(que)>0:
        btm = set(que.pop())
    else:
        btm = top
    tmpset = top & btm
    if len(tmpset) == 0:
        print(-1)
        exit()
    else:
        lis = list(tmpset)
        ans[left] = lis[0]
        if ans[right] == 0:
            ans[right] = lis[0]
        else:
            pass
    left += 1
    right -= 1

print(*ans,sep="")
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
