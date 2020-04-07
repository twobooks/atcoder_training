# from math import factorial,sqrt
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
# 配列入力の受け取り
# arrA = list(map(int,input().split()))
arrA = np.array(input().split(),dtype=np.int64)

arrA.sort()
arrA = arrA[::-1]
total = arrA.sum()

if arrA[m-1] >= total/(4*m):
    ans = "Yes"
else:
    ans = "No"

print(ans)
# print("{:.10f}".format(ans))
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する