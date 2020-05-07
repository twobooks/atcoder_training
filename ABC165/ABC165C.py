# from math import factorial,sqrt,ceil,gcd
from itertools import permutations,combinations,combinations_with_replacement
# from collections import deque,Counter
# import re
# from functools import lru_cache # 簡単メモ化 @lru_cache(maxsize=1000)
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# import networkx as nx
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix
# from scipy.special import comb

# slist = "abcdefghijklmnopqrstuvwxyz"
N,M,Q = map(int,input().split())
times = Q
abcds = []
for _ in range(times):
    abcds.append(list(map(int,input().split()))) # 行列の場合
AnoMoto = list(range(1,M+1))
# print(AnoMoto)
# lenA = len(arrA)
ans = 0
for lisA in combinations_with_replacement(AnoMoto,N):
    # print(lisA)
    num = 0
    for abcd in abcds:
        a,b,c,d = abcd
        if lisA[b-1] - lisA[a-1] == c:
            num += d
        ans = max(ans,num)

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
