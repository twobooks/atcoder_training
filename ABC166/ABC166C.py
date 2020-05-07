# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations,combinations,combinations_with_replacement
# from collections import deque,Counter
# import re
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

import numpy as np
# import networkx as nx
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb

# slist = "abcdefghijklmnopqrstuvwxyz"
N,M = map(int,input().split())
lisH = [0] + list(map(int,input().split()))
lisAB = lisH.copy()
for i in range(M):
    A,B = map(int,input().split())
    if lisH[A] > lisH[B]:
        lisAB[B] = 0
    elif lisH[A] < lisH[B]:
        lisAB[A] = 0
    else:
        lisAB[A] = 0
        lisAB[B] = 0
        
ans = 0
for i in range(1,N+1):
    if lisH[i] == lisAB[i]:
        ans += 1

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
