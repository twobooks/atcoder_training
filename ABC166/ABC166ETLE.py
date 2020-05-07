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
N = int(input())
lisA = list(map(int,input().split()))
# arrA = np.array(input().split(),dtype=np.int64)

ans = 0
for i in range(1,N):
    for j in range(0,N-i):
        if lisA[j]+lisA[j+i]==i:
            ans += 1
print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
