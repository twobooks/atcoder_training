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
N,P = map(int,input().split())
# arrA = list(map(int,input().split()))
arrA = np.array(input().split(),dtype=np.int64)

A = arrA % 2
if not (1 in A):
    if P == 1:
        print(0)
        exit()
    else:
        print(2**N)
        exit()

even = 1
odd = 1
for i in sorted(A)[::-1][1:]:
    if i == 0:
        even *= 2
        odd *= 2
    else:
        even,odd = odd + even , odd + even
if P==0:
    print(even)
else:
    print(odd)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
