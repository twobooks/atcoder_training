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
n,m,c = map(int,input().split())
B = np.array(input().split(),dtype=np.int64)
times = n
table = []
for _ in range(times):
    table.append(list(map(int,input().split()))) # 行列の場合
A = np.array(table)

lis = np.dot(A,B) +c
anslis = np.bincount(lis > 0,minlength=2)
ans = anslis[1]

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
