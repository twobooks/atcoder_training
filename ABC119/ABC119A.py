# from math import factorial,sqrt,ceil
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter
from datetime import date
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix

# strlist = "abcdefghijklmnopqrstuvwxyz"
y,m,d = map(int,input().split("/"))
S = date(y,m,d)
F = date(2019,4,30)

ans = "TBD"
if S<=F:
    ans = "Heisei"

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
