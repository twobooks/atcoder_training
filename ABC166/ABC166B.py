# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations,combinations,combinations_with_replacement
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
N,K = map(int,input().split())
Nset = set(list(range(1,N+1)))
okasi = []
shojisha = []
for _ in range(K):
    okasi.append(int(input()))
    shojisha.append(list(map(int,input().split())))

for lis in shojisha:
    Nset = Nset - set(lis)

print(len(Nset))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
