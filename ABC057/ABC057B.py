# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
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
times = N
AB = []
for _ in range(times):
    AB.append(list(map(int,input().split()))) # 行列の場合
times = M
CD = []
for _ in range(times):
    CD.append(list(map(int,input().split()))) # 行列の場合

AB = np.array(AB)
CD = np.array(CD)
for ab in AB:
    arr = np.sum(abs(ab-CD),axis=1)
    # print(arr)
    print(np.argmin(arr)+1)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
