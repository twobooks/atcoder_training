# from math import factorial,sqrt,ceil,gcd
# from itertools import permutations as permus
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix

# strlist = "abcdefghijklmnopqrstuvwxyz"
N = int(input())
arrA = np.array(input().split(),dtype=np.int64)

def check():
    temp = arrA % 2
    if 1 in temp:
        return False
    return True

ans = 0
while check():
    arrA = arrA // 2
    ans += 1

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
