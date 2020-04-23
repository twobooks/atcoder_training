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
N = int(input())
arrA = np.array(input().split(),dtype=np.int64)
bins = np.array([400,800,1200,1600,2000,2400,2800,3200,4801])
arr = np.digitize(arrA,bins)
ans = np.bincount(arr,minlength=9)
ans1 = len(ans[:-1][ans[:-1]>0])
ans2 = ans1 + ans[-1]
if ans1 == 0:
    ans1 = 1
print(ans1,ans2)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
