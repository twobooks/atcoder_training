# from math import factorial,sqrt,ceil
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix

# strlist = "abcdefghijklmnopqrstuvwxyz"
n,m = map(int,input().split())
# arrX = list(map(int,input().split()))
X = np.array(input().split(),dtype=np.int64)

X.sort()
X = np.diff(X)
X.sort()

if n>=m:
    ans = 0
elif n == 1:
    ans = X.sum()
else:
    ans = X[:-(n-1)].sum()

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
