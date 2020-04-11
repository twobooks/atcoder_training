# from math import factorial,sqrt
# from itertools import permutations as permus
# from fractions import gcd
# from collections import deque,Counter
# from decimal import Decimal, getcontext
# # getcontext().prec = 1000
# # eps = Decimal(10) ** (-100)

# import numpy as np
# from scipy.sparse.csgraph import shortest_path, dijkstra, floyd_warshall, bellman_ford, johnson
# from scipy.sparse import csr_matrix

# strlist = "abcdefghijklmnopqrstuvwxyz"

rows = [int(input()) for _ in range(5)]

lis = []
for num in rows:
    if num%10 == 0:
        lis.append(num)
    else:
        num = (num//10 + 1)*10
        lis.append(num)

snum = sum(lis)
ans = snum
for i in range(5):
    var = snum - lis[i] + rows[i]
    ans = min(ans,var)

print(ans)
# print(*ans)   # unpackして出力。間にスペースが入る
# for row in board:
#     print(*row,sep="")    #unpackして間にスペース入れずに出力する
# print("{:.10f}".format(ans))
# print("{:0=10d}".format(ans))
